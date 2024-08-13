import streamlit as st
import random
import time
from PIL import Image, ImageDraw, ImageFont

# 제목 입력
st.title("모서리 게임")

# 사용자로부터 제목 입력받기
game_title = st.text_input("게임 제목을 입력하세요:")

# 교실 모형 만들기
st.header(game_title)

# 교실 모형 이미지 생성
def create_classroom_image():
    img_size = 600
    img = Image.new("RGB", (img_size, img_size), color="white")
    draw = ImageDraw.Draw(img)

    # 칠판
    draw.rectangle([(50, 50), (550, 100)], fill="green")
    draw.text((275, 70), "칠판", fill="white", anchor="mm")

    # 창문
    draw.rectangle([(50, 100), (100, 550)], fill="skyblue")
    draw.text((75, 325), "창문", fill="white", anchor="mm", angle=90)

    # 복도
    draw.rectangle([(500, 100), (550, 550)], fill="gray")
    draw.text((525, 325), "복도", fill="white", anchor="mm", angle=270)

    # 모서리 번호 (1, 2, 3, 4)
    draw.text((75, 75), "1", fill="black", anchor="mm")
    draw.text((525, 75), "2", fill="black", anchor="mm")
    draw.text((75, 525), "3", fill="black", anchor="mm")
    draw.text((525, 525), "4", fill="black", anchor="mm")

    return img

# 이미지 표시
img = create_classroom_image()
st.image(img)

# 게임 시작 버튼
if st.button("게임 시작"):
    st.session_state['start_game'] = True

# 게임이 시작된 경우
if 'start_game' in st.session_state and st.session_state['start_game']:
    st.write("각 모서리에 들어갈 요소를 입력하세요:")

    # 각 모서리에 들어갈 내용 입력
    corner1 = st.text_input("1번 모서리:")
    corner2 = st.text_input("2번 모서리:")
    corner3 = st.text_input("3번 모서리:")
    corner4 = st.text_input("4번 모서리:")

    if st.button("입력 완료"):
        st.session_state['corners'] = [corner1, corner2, corner3, corner4]
        st.write("내용이 입력되었습니다. 2분 타이머를 시작합니다.")
        st.session_state['timer_started'] = True
        st.session_state['start_time'] = time.time()

# 타이머 로직
if 'timer_started' in st.session_state and st.session_state['timer_started']:
    elapsed_time = time.time() - st.session_state['start_time']
    remaining_time = 120 - elapsed_time

    if remaining_time > 0:
        st.write(f"남은 시간: {int(remaining_time)}초")
    else:
        st.session_state['timer_started'] = False
        st.session_state['timer_done'] = True

# 결과 보기 버튼
if 'timer_done' in st.session_state and st.session_state['timer_done']:
    if st.button("결과 보기"):
        st.session_state['result_shown'] = True
        chosen_corner = random.choice([1, 2, 3, 4])
        st.session_state['chosen_corner'] = chosen_corner

# 결과 표시 및 다시 하기 버튼
if 'result_shown' in st.session_state and st.session_state['result_shown']:
    chosen_corner = st.session_state['chosen_corner']
    st.write(f"선택된 번호는: {chosen_corner}번 입니다!")
    st.write(f"내용: {st.session_state['corners'][chosen_corner-1]}")
    if st.button("다시 하기"):
        st.session_state.clear()
        st.experimental_rerun()
