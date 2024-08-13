from urllib import response
from requests import session
import streamlit as st
from langchain_core.messages.chat import ChatMessage
from langchain_openai import ChatOpenAI
from langchain_teddynote import logging
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.output_parsers import StrOutputParser
import datetime

today = datetime.date.today()
from dotenv import load_dotenv
import os

# API KEY 정보로드
#load_dotenv()

# 캐시 디렉토리 생성
if not os.path.exists(".cache"):
    os.mkdir(".cache")

# 파일 업로드 전용 폴더
if not os.path.exists(".cache/files"):
    os.mkdir(".cache/files")

if not os.path.exists(".cache/embeddings"):
    os.mkdir(".cache/embeddings")

st.title("대화내용을 기억하는 챗봇 💬")

# 처음 1번만 실행하기 위한 코드
if "messages" not in st.session_state:
    # 대화기록을 저장하기 위한 용도로 생성한다.
    st.session_state["messages"] = []

if "store" not in st.session_state:
    st.session_state["store"] = {}

# 모델 선택 메뉴
selected_model = st.selectbox("LLM 선택", ["gpt-4o", "gpt-4o-mini"], index=0)

# 세션 ID를 지정하는 메뉴
session_id = st.text_input("세션 ID를 입력하세요.", "abc123")

# 화면에 날짜 선택 메뉴 추가
st.header("날짜 선택")
selected_date = st.date_input("날짜를 선택하세요", today)

# 날짜에 대한 기념일 정보를 확인
if st.button("기념일 확인"):
    date_str = selected_date.strftime("%Y-%m-%d")
    question = f"{date_str}는 어떤 기념일인가요?"

    # GPT 모델을 사용하여 답변을 생성합니다.
    chain = st.session_state.get("multiturn_chain")
    if chain is None:
        chain = create_chain(model_name=selected_model)
        st.session_state["multiturn_chain"] = chain

    try:
        response = chain.run({"question": question, "configurable": {"session_id": session_id}})
        st.write(f"📅 {date_str}: {response}")
    except AttributeError as e:
        st.error(f"체인 실행 중 오류가 발생했습니다: {str(e)}")
    except Exception as e:
        st.error(f"알 수 없는 오류가 발생했습니다: {str(e)}")

# 이전 대화를 출력
def print_messages():
    for chat_message in st.session_state["messages"]:
        st.chat_message(chat_message.role).write(chat_message.content)
