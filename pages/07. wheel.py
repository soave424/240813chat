import streamlit as st

# 페이지 타이틀
st.title("360도 회전하는 화살표")

# CSS와 HTML을 사용하여 회전 애니메이션 구현
st.markdown("""
    <style>
    .rotate {
        display: block;
        margin: 0 auto;
        width: 150px;
        height: 150px;
        animation: spin 4s linear infinite;
    }

    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    </style>
    <div>
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Green_Arrow_Up.svg/1024px-Green_Arrow_Up.svg.png" class="rotate" alt="Rotating Arrow">
    </div>
""", unsafe_allow_html=True)
