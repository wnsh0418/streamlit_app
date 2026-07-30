import streamlit as st

# -------------------------------
# 1. 기본 설정
# -------------------------------
st.set_page_config(page_title="진로 기반 과목 추천", layout="centered")

st.title("🎓 진로 기반 선택과목 추천")
st.markdown("2022 개정 교육과정 기준으로 진로에 맞는 과목을 추천합니다.")

# -------------------------------
# 2. 데이터 (핵심)
# -------------------------------

career_data = {
    "의사": {
        "skills": ["생명과학 이해", "화학 지식", "문제 해결력"],
        "subjects": [
            {"name": "생명과학Ⅰ", "level": "중", "reason": "인체 구조와 생명 원리를 이해하는 데 필수"},
            {"name": "생명과학Ⅱ", "level": "상", "reason": "심화 생명과학 지식 학습"},
            {"name": "화학Ⅰ", "level": "중", "reason": "약물과 생체 반응 이해"},
            {"name": "화학Ⅱ", "level": "상", "reason": "의학 관련 심화 화학 개념"}
        ]
    },

    "개발자": {
        "skills": ["논리적 사고", "수학적 사고", "프로그래밍"],
        "subjects": [
            {"name": "미적분Ⅰ", "level": "중", "reason": "알고리즘 이해에 필요한 수학 기초"},
            {"name": "확률과 통계", "level": "중", "reason": "데이터 분석 기초"},
            {"name": "인공지능수학", "level": "상", "reason": "AI 및 머신러닝 이해"},
            {"name": "정보", "level": "중", "reason": "프로그래밍 및 컴퓨팅 사고력"}
        ]
    },

    "디자이너": {
        "skills": ["창의성", "시각 표현", "디자인 사고"],
        "subjects": [
            {"name": "미술", "level": "중", "reason": "기초 표현 능력 향상"},
            {"name": "디자인 일반", "level": "중", "reason": "디자인 원리 학습"},
            {"name": "미술 창작", "level": "상", "reason": "실제 작품 제작 경험"},
            {"name": "영상 제작", "level": "중", "reason": "디지털 콘텐츠 제작 능력"}
        ]
    },

    "경영": {
        "skills": ["경제 이해", "의사소통", "분석력"],
        "subjects": [
            {"name": "경제", "level": "중", "reason": "시장 구조와 경제 원리 이해"},
            {"name": "정치와 법", "level": "중", "reason": "사회 구조 이해"},
            {"name": "사회·문화", "level": "중", "reason": "사회 현상 분석"},
            {"name": "독서와 작문", "level": "하", "reason": "의사소통 능력 강화"}
        ]
    }
}

# -------------------------------
# 3. 사용자 입력
# -------------------------------

career = st.selectbox(
    "희망 진로를 선택하세요",
    list(career_data.keys())
)

difficulty = st.radio(
    "선호 난이도 선택",
    ["전체", "하", "중", "상"]
)

# -------------------------------
# 4. 추천 로직
# -------------------------------

def get_recommendations(career, difficulty):
    subjects = career_data[career]["subjects"]

    if difficulty == "전체":
        return subjects
    else:
        return [s for s in subjects if s["level"] == difficulty]

recommended = get_recommendations(career, difficulty)

# -------------------------------
# 5. 결과 출력
# -------------------------------

st.subheader(f"📌 '{career}' 진로 추천 과목")

# 필요 역량
st.markdown("### 🔎 필요한 역량")
for skill in career_data[career]["skills"]:
    st.write(f"- {skill}")

st.markdown("---")

# 과목 추천
st.markdown("### 📚 추천 과목")

if recommended:
    for subj in recommended:
        st.markdown(f"""
        **✔️ {subj['name']}**  
        - 난이도: {subj['level']}  
        - 이유: {subj['reason']}
        """)
else:
    st.warning("선택한 난이도에 해당하는 과목이 없습니다.")

# -------------------------------
# 6. 추가 추천 (확장 기능)
# -------------------------------

st.markdown("---")
st.markdown("### 🔁 유사 진로 추천")

similar_map = {
    "의사": ["약사", "간호사"],
    "개발자": ["데이터 분석가", "AI 엔지니어"],
    "디자이너": ["영상 편집자", "UX/UI 디자이너"],
    "경영": ["마케팅 전문가", "회계사"]
}

for s in similar_map[career]:
    st.write(f"- {s}")

# -------------------------------
# 7. 푸터
# -------------------------------
st.markdown("---")
st.caption("© 2026 진로 추천 앱 | 2022 개정 교육과정 기반")
