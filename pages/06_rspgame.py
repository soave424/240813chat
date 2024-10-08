import streamlit as st
import random
import time

# 이미지 파일 경로 설정
image_paths = {
    "가위": "images/002.png",  # 가위
    "바위": "images/001.png",  # 주먹
    "보": "images/003.png",   # 보
}

# 가위바위보 옵션
options = list(image_paths.keys())

# 페이지 타이틀
st.title("가위바위보 게임")

# 게임 시작 버튼
if st.button("게임 시작"):
    # 이미지 표시할 컨테이너
    image_slot = st.empty()

    # 3개의 이미지를 빠르게 전환하는 효과
    for i in range(10):  # 10번 정도 반복하며 이미지를 전환
        random_choice = random.choice(options)
        image_slot.image(image_paths[random_choice], width=200)
        time.sleep(0.3)  # 0.3초 동안 이미지 표시
        image_slot.empty()  # 이미지를 지우고 빈 화면으로 만듦
        time.sleep(0.1)  # 0.1초의 간격으로 이미지를 교체

    # 최종 선택된 결과
    final_choice = random.choice(options)
    image_slot.image(image_paths[final_choice], width=200)
    st.write(f"결과: {final_choice}!")
