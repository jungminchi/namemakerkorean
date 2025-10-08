import streamlit as st
import random

st.title("한국식 이름 생성기 🇰🇷")

surnames = [
    "김", "이", "박", "최", "정", "조", "강", "윤", "장", "임",
    "한", "오", "서", "신", "권", "황", "안", "송", "류", "홍"
]

male_names = [
    "민준", "서준", "도윤", "하준", "주원", "지호", "현우", "지훈", "준우", "유준",
    "건우", "우진", "선우", "연우", "시우", "예준", "민재", "은우", "지후", "서우"
]

female_names = [
    "서연", "하은", "지우", "서윤", "민서", "지유", "하윤", "윤서", "채원", "은서",
    "지민", "수아", "예은", "소율", "다은", "예린", "지원", "유나", "가은", "나은"
]

st.subheader("이름 생성 옵션")
selected_surname = st.selectbox("성을 선택하세요", surnames)
gender = st.radio("성별을 선택하세요", ("남성", "여성", "LGBTQ+"))

if st.button("이름 생성"):
    if gender == "남성":
        given_name = random.choice(male_names)
    elif gender == "여성":
        given_name = random.choice(female_names)
    else:
        given_name = random.choice(male_names + female_names)
    full_name = selected_surname + given_name
    st.success(f"당신의 이름은 **{full_name}** 입니다!")

if "generated_names" not in st.session_state:
    st.session_state["generated_names"] = []

if st.button("이름 저장"):
    if "full_name" in locals():
        st.session_state["generated_names"].append(full_name)
        st.info(f"{full_name} 이름이 저장되었습니다.")
    else:
        st.warning("먼저 이름을 생성하세요.")

if st.session_state["generated_names"]:
    st.subheader("지금까지 생성한 이름들")
    for name in st.session_state["generated_names"]:
        st.write(f"- {name}")