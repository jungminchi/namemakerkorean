import streamlit as st
import random

st.title("한국식 이름 생성기 🇰🇷")

surnames = [
    "김", "이", "박", "최"
]

male_names = [
    "민준", "서준", "도윤", "하준", "주원", "지호", "현우", "준서", "예준", "시우",
    "건우", "우진", "선우", "연우", "시윤", "민재", "태윤", "유준", "지후", "하율",
    "윤호", "수호", "준호", "민성", "시헌", "도현", "재윤", "성민", "현민", "승현",
    "지환", "준혁", "태현", "하온", "진우", "도하", "유찬", "하민", "시온", "라온",
    "현수", "민호", "재민", "태민", "예찬", "승우", "준영", "형준", "현준", "영준",
    "민석", "정우", "지혁", "인호", "재호", "동현", "민기", "수민", "우빈", "지훈",
    "현진", "성훈", "준원", "하성", "경민", "태우", "시완", "지성", "윤재", "병준",
    "동윤", "재욱", "도경", "원준", "승민", "우성", "진혁", "기현", "현오", "태원",
    "재원", "민욱", "창현", "정훈", "재현", "성우", "시훈", "동우", "재석", "태경",
    "준민", "영호", "병훈", "진서", "성진", "민우", "도원", "지완", "현태", "재광"
]

female_names = [
    "서연", "하은", "지우", "서윤", "민서", "지유", "하윤", "윤서", "채원", "은서",
    "지민", "수아", "예은", "소율", "다은", "예린", "지원", "유나", "가은", "나은",
    "다윤", "서아", "시은", "수빈", "유진", "아린", "하린", "민지", "연우", "지안",
    "유빈", "소연", "채은", "예원", "하영", "지현", "서희", "서윤", "은빈", "하경",
    "수연", "유나", "예진", "민아", "채린", "연서", "지유", "소윤", "서현", "다연",
    "세은", "유경", "하민", "지율", "예서", "서은", "유진", "다빈", "민서", "서영",
    "연지", "하영", "수민", "채원", "지우", "아윤", "윤아", "하린", "서아", "소민",
    "예빈", "연우", "지민", "하연", "수빈", "민지", "서현", "지안", "유빈", "다율",
    "채아", "소율", "예린", "유서", "서연", "하은", "민서", "지유", "연서", "하윤",
    "서우", "지안", "윤서", "채은", "아린", "수아", "예원", "소연", "지현", "민아"
]

st.subheader("이름 생성 옵션")
selected_surname = st.selectbox("성을 선택하세요", surnames)
gender = st.radio("성별을 선택하세요", ("남성", "여성", "LGBTQ"))

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