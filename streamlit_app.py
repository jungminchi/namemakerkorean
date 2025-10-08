import streamlit as st
import random

st.set_page_config(page_title="한국식 이름 생성기", page_icon="🎎", layout="centered")

st.title("한국식 이름 생성기 🏷️")
st.write("성(한국에서 자주 쓰이는 여러 성)을 선택하고 성별을 지정하면, 한국식 이름(성 + 이름)을 무작위로 만들어 줍니다.")

surnames = [
    "김", "이", "박", "최", "정", "조", "강", "윤", "임", "한", "오", "서", "신", "권", "황", "안", "송", "전", "홍", "유"
]

surname = st.selectbox("성 선택", surnames)

gender = st.radio("성별 선택", ("남성", "여성", "랜덤"), index=2)

syllable_count = st.radio("이름 음절 수", (2, 1), index=0, format_func=lambda x: f"{x}음절")

male_syllables = [
    "민", "준", "현", "우", "승", "호", "영", "재", "석", "태", "상", "훈", "기", "혁", "율", "한", "진", "건", "성"
]

female_syllables = [
    "지", "은", "수", "예", "하", "윤", "라", "다", "나", "연", "솔", "유", "혜", "리", "경", "미", "아", "채", "빈"
]

with st.expander("원하는 음절을 추가하려면 클릭하세요 (쉼표로 구분)"):
    custom = st.text_input("추가 음절 (예: 진,성,아)")

if "history" not in st.session_state:
    st.session_state.history = []

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("생성"):

        if gender == "남성":
            pool = male_syllables.copy()
        elif gender == "여성":
            pool = female_syllables.copy()
        else:
            pool = male_syllables + female_syllables


        if custom:
            extra = [s.strip() for s in custom.split(",") if s.strip()]
            for e in extra:
                if e not in pool:
                    pool.append(e)

        if syllable_count == 1:
            given = random.choice(pool)
        else:
            given = "".join(random.sample(pool, 2))

        full_name = surname + given
        st.session_state.history.insert(0, full_name)
        st.success(f"생성된 이름: {full_name}")

with col2:
    if st.button("초기화"):
        st.session_state.history = []
        st.info("기록을 초기화했습니다.")

st.subheader("최근 생성된 이름")
if st.session_state.history:
    for i, name in enumerate(st.session_state.history[:20], 1):
        st.write(f"{i}. {name}")
else:
    st.write("아직 생성된 이름이 없습니다. '생성' 버튼을 눌러 이름을 만들어 보세요.")

st.write("---")
st.write("한국식 이름 생성기 — 확장된 성 목록과 성별 선택 기능이 포함되어 있습니다. 원하면 더 다양한 옵션(예: 한자, 세대별 이름 스타일 등)도 추가할 수 있습니다.")