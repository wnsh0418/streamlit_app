import streamlit as st

# ---------------------------
# 기본 설정
# ---------------------------
st.set_page_config(page_title="진로 추천 앱", layout="wide")

# ---------------------------
# CSS (카드 UI 핵심)
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
# 데이터
# ---------------------------
career_data = {
    "의사": [
        {"name": "생명과학Ⅰ", "level": "중", "category": "과학", "reason": "인체 이해"},
        {"name": "생명과학Ⅱ", "level": "상", "category": "과학", "reason": "심화 생명과학"},
        {"name": "화학Ⅰ", "level": "중", "category": "과학", "reason": "약물 이해"},
        {"name": "화학Ⅱ", "level": "상", "category": "과학", "reason": "심화 화학"}
    ],
    "개발자": [
        {"name": "미적분Ⅰ", "level": "중", "category": "수학", "reason": "알고리즘 기초"},
        {"name": "확률과 통계", "level": "중", "category": "수학", "reason": "데이터 분석"},
        {"name": "프로그래밍", "level": "중", "category": "정보", "reason": "코딩"},
        {"name": "인공지능수학", "level": "상", "category": "수학", "reason": "AI 이해"}
    ],
    "디자이너": [
        {"name": "미술", "level": "중", "category": "예술", "reason": "표현력"},
        {"name": "디자인 일반", "level": "중", "category": "예술", "reason": "디자인 기초"},
        {"name": "영상 제작", "level": "중", "category": "예술", "reason": "콘텐츠 제작"}
    ]
}

# ---------------------------
# UI - 사이드바 필터
# ---------------------------
st.sidebar.title("⚙️ 필터")

career = st.sidebar.selectbox("진로 선택", list(career_data.keys()))

difficulty = st.sidebar.multiselect(
    "난이도 선택",
    ["하", "중", "상"],
    default=["하", "중", "상"]
)

category_filter = st.sidebar.multiselect(
    "과목군 선택",
    ["과학", "수학", "정보", "예술"],
    default=["과학", "수학", "정보", "예술"]
)

# ---------------------------
# 필터 적용
# ---------------------------
filtered = []
for subj in career_data[career]:
    if subj["level"] in difficulty and subj["category"] in category_filter:
        filtered.append(subj)

# ---------------------------
# 카드 UI 함수
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
# 메인 UI
# ---------------------------
st.title("🎓 진로 기반 과목 추천")

st.subheader(f"📌 {career} 추천 과목")

if filtered:
    cols = st.columns(3)
    for i, subj in enumerate(filtered):
        with cols[i % 3]:
            render_card(subj)
else:
    st.warning("조건에 맞는 과목이 없습니다.")

# ---------------------------
# 추가 UX 요소
# ---------------------------
st.markdown("---")

st.info("💡 Tip: 난이도와 과목군을 조합해서 최적의 선택을 찾아보세요.")
