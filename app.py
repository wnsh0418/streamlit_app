import streamlit as st

# ---------------------------
# 기본 설정
# ---------------------------
st.set_page_config(page_title="진로 기반 과목 추천", layout="wide")

# ---------------------------
# 카드 UI 스타일
# ---------------------------
st.markdown("""
<style>
.card {
    background-color: #ffffff;
    padding: 18px;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 15px;
    transition: 0.2s;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 18px rgba(0,0,0,0.15);
}
.badge {
    display: inline-block;
    padding: 4px 10px;
    border-radius: 10px;
    font-size: 12px;
    margin-right: 5px;
    color: white;
}
.low { background-color: #4CAF50; }
.mid { background-color: #FF9800; }
.high { background-color: #F44336; }
.category {
    font-size: 13px;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# 과목 DB (2022 교육과정)
# ---------------------------
subjects_db = {
    "수학": ["대수", "미적분Ⅰ", "미적분Ⅱ", "확률과 통계", "기하", "인공지능수학"],
    "과학": ["물리학Ⅰ", "물리학Ⅱ", "화학Ⅰ", "화학Ⅱ", "생명과학Ⅰ", "생명과학Ⅱ"],
    "사회": ["경제", "정치와 법", "사회·문화"],
    "국어": ["독서와 작문", "문학"],
    "정보": ["정보", "프로그래밍", "데이터 과학"],
    "예술": ["미술", "디자인 일반", "영상 제작"]
}

# ---------------------------
# 진로 매핑 데이터
# ---------------------------
career_map = {
    "의사": ["생명과학Ⅰ", "생명과학Ⅱ", "화학Ⅰ", "화학Ⅱ"],
    "개발자": ["대수", "미적분Ⅰ", "확률과 통계", "프로그래밍", "인공지능수학"],
    "디자이너": ["미술", "디자인 일반", "영상 제작"],
    "경영": ["경제", "사회·문화", "정치와 법", "독서와 작문"]
}

# ---------------------------
# 과목 상세 정보 생성
# ---------------------------
def build_subject_list(career):
    result = []
    for subj in career_map[career]:
        for category, subs in subjects_db.items():
            if subj in subs:
                result.append({
                    "name": subs,
                    "category": category,
                    "level": assign_level(subj),
                    "reason": generate_reason(career, subj)
                })
    return result

# ---------------------------
# 난이도 자동 설정
# ---------------------------
def assign_level(subj):
    if "Ⅱ" in subj or "인공지능" in subj:
        return "상"
    elif "Ⅰ" in subj:
        return "중"
    else:
        return "하"

# ---------------------------
# 추천 이유 자동 생성
# ---------------------------
def generate_reason(career, subj):
    return f"{career} 진로에서 필요한 핵심 역량과 관련된 과목입니다."

# ---------------------------
# 카드 UI 렌더링
# ---------------------------
def render_card(subj):
    level_class = {
        "하": "low",
        "중": "mid",
        "상": "high"
    }[subj["level"]]

    st.markdown(f"""
    <div class="card">
        <h4>{subj['name']}</h4>
        <div class="category">{subj['category']}</div>
        <br>
        <span class="badge {level_class}">난이도: {subj['level']}</span>
        <p>{subj['reason']}</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------
# 사이드바 필터
# ---------------------------
st.sidebar.title("⚙️ 필터")

career = st.sidebar.selectbox("진로 선택", list(career_map.keys()))

difficulty_filter = st.sidebar.multiselect(
    "난이도 선택",
    ["하", "중", "상"],
    default=["하", "중", "상"]
)

category_filter = st.sidebar.multiselect(
    "과목군 선택",
    list(subjects_db.keys()),
    default=list(subjects_db.keys())
)

# ---------------------------
# 추천 결과 생성
# ---------------------------
subjects = build_subject_list(career)

filtered_subjects = [
    s for s in subjects
    if s["level"] in difficulty_filter and s["category"] in category_filter
]

# ---------------------------
# 메인 UI
# ---------------------------
st.title("🎓 진로 기반 선택과목 추천")
st.subheader(f"📌 {career} 추천 과목")

if filtered_subjects:
    cols = st.columns(3)
    for i, subj in enumerate(filtered_subjects):
        with cols[i % 3]:
            render_card(subj)
else:
    st.warning("조건에 맞는 과목이 없습니다.")

# ---------------------------
# 유사 진로 추천
# ---------------------------
st.markdown("---")
st.subheader("🔁 유사 진로")

similar_map = {
    "의사": ["약사", "간호사"],
    "개발자": ["데이터 분석가", "AI 엔지니어"],
    "디자이너": ["UX/UI 디자이너", "영상 편집자"],
    "경영": ["마케팅 전문가", "회계사"]
}

for s in similar_map[career]:
    st.write(f"- {s}")

# ---------------------------
# 푸터
# ---------------------------
st.markdown("---")
st.caption("© 2026 진로 추천 앱 | 2022 개정 교육과정 기반")
