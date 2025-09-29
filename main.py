import streamlit as st
from typing import Dict, List

st.set_page_config(page_title="MBTI 진로 추천 (중학생용)", page_icon="🧭", layout="centered")

# ------------------------------
# Data: MBTI → 3 Career ideas
# (중학생 눈높이+한국 맥락 / 고정관념 최소화 / 성별·계층 중립)
# ------------------------------
Career = Dict[str, List[Dict[str, str]]]
CAREERS: Career = {
    "ISTJ": [
        {"name": "공공행정·행정사무", "emoji": "🏛️", "why": "체계적이고 신뢰받는 실무를 좋아한다면 공공 데이터를 다루고 학교·지자체 행정을 지원하는 일에 강점!"},
        {"name": "회계·재무 기초", "emoji": "📊", "why": "규칙과 정확성을 중시하는 성향이 숫자 관리에 잘 맞아요."},
        {"name": "품질관리·안전관리", "emoji": "🧪", "why": "체크리스트로 꾸준히 점검하는 일이 잘 맞아 실험실·제조 현장 품질관리로 확장 가능."},
    ],
    "ISFJ": [
        {"name": "보건·간호 보조", "emoji": "🩺", "why": "배려심과 책임감으로 사람을 돕는 환경에 강점."},
        {"name": "학교상담·학생지원", "emoji": "🧑‍🏫", "why": "규칙적인 환경에서 또래를 돕고 기록을 정리하는 일에 적합."},
        {"name": "아동복지·돌봄", "emoji": "🧸", "why": "세심함과 인내심이 필요한 돌봄 직무에서 장점 발휘."},
    ],
    "INFJ": [
        {"name": "심리·상담·코칭", "emoji": "🧠", "why": "의미 중심 사고와 공감 능력이 청소년·가족 상담로 이어지기 좋아요."},
        {"name": "교육기획·커리큘럼", "emoji": "📚", "why": "가치와 비전을 설계하는 능력이 학습 프로그램 기획에 적합."},
        {"name": "사회혁신·비영리", "emoji": "🌍", "why": "가치 지향적 프로젝트에서 변화 촉진자로 활약."},
    ],
    "INTJ": [
        {"name": "데이터 분석·리서치", "emoji": "📈", "why": "구조화와 장기 전략 수립에 강해 연구·분석 직무와 궁합."},
        {"name": "제품전략·PM(초기)", "emoji": "🧩", "why": "문제 정의와 로드맵 수립을 즐기면 제품 기획으로 확장 가능."},
        {"name": "엔지니어링·알고리즘", "emoji": "🤖", "why": "논리적 최적화와 시스템 설계에 강점."},
    ],
    "ISTP": [
        {"name": "기계·드론·로보틱스", "emoji": "🛠️", "why": "손으로 직접 만지고 고치는 일, 실험이 즐겁다면 현장형 기술 진로에 적합."},
        {"name": "사이버보안 기초", "emoji": "🛡️", "why": "문제 분해·버그 헌팅을 좋아하는 성향과 잘 맞음."},
        {"name": "스포츠 과학·장비튜닝", "emoji": "🏃", "why": "도구 사용과 실전 최적화를 즐기는 강점 활용."},
    ],
    "ISFP": [
        {"name": "시각디자인·일러스트", "emoji": "🎨", "why": "감수성과 미적 감각을 표현하는 창작 직무에 적합."},
        {"name": "푸드스타일링·제과제빵", "emoji": "🧁", "why": "감각과 섬세함을 살려 결과물을 만드는 즐거움."},
        {"name": "문화예술·공예", "emoji": "🧵", "why": "손끝 기술과 개성이 강점인 분야."},
    ],
    "INFP": [
        {"name": "작가·에디터·콘텐츠", "emoji": "✍️", "why": "스토리·가치 중심 창작이 강점."},
        {"name": "아동·청소년 콘텐츠 기획", "emoji": "📖", "why": "공감과 상상력을 교육용 콘텐츠로 연결."},
        {"name": "사회복지·인권", "emoji": "🤝", "why": "이해와 배려를 바탕으로 변화를 만드는 역할."},
    ],
    "INTP": [
        {"name": "연구개발·과학", "emoji": "🔬", "why": "호기심·이론화·모형 만들기에 강점."},
        {"name": "소프트웨어·오픈소스", "emoji": "💻", "why": "문제 해결을 즐기고 자율적 탐구에 익숙."},
        {"name": "게임개발·시뮬레이션", "emoji": "🕹️", "why": "시스템 설계·논리 퍼즐을 좋아한다면 찰떡."},
    ],
    "ESTP": [
        {"name": "세일즈·마케팅 실전", "emoji": "📣", "why": "현장에서 바로 반응을 보고 조정하는 역동성에 강점."},
        {"name": "이벤트·스포츠 매니지먼트", "emoji": "🎪", "why": "순발력과 실행력이 필요한 운영에 적합."},
        {"name": "응급구조·안전", "emoji": "🚑", "why": "실전 대응력·침착함을 살릴 수 있음."},
    ],
    "ESFP": [
        {"name": "공연예술·댄스·연기", "emoji": "🎭", "why": "무대 체질·표현력·팀워크를 살릴 수 있음."},
        {"name": "관광·호스피탈리티", "emoji": "🏖️", "why": "사람과의 상호작용을 즐기고 분위기 메이킹 강점."},
        {"name": "유튜브·쇼츠 크리에이터", "emoji": "📱", "why": "센스있는 연출·트렌드 캐치를 살려 성장 가능."},
    ],
    "ENFP": [
        {"name": "브랜드·콘텐츠 기획", "emoji": "🌈", "why": "아이디어 발산·연결을 즐기는 성향에 찰떡."},
        {"name": "사회혁신 스타터", "emoji": "🚀", "why": "열정과 공감을 프로젝트로 실행."},
        {"name": "에듀테크·진로멘토", "emoji": "🧑‍💻", "why": "사람 성장과 아이디어를 연결하는 역할에 강점."},
    ],
    "ENTP": [
        {"name": "창업·신사업 기획", "emoji": "💡", "why": "새로운 것 시도·토론·피봇에 에너지 얻음."},
        {"name": "전략컨설팅(탐색)", "emoji": "🧭", "why": "가설 세우고 실험하며 논리로 설득."},
        {"name": "미디어·테크 저널리즘", "emoji": "📰", "why": "이슈를 해석하고 관점을 제시하는 데 강점."},
    ],
    "ESTJ": [
        {"name": "프로젝트 운영·관리", "emoji": "🗂️", "why": "기한·인력·예산을 조율하는 실무에 강점."},
        {"name": "공공안전·경찰(탐색)", "emoji": "👮", "why": "규칙 준수·리더십을 살릴 수 있음."},
        {"name": "유통·물류 관리", "emoji": "📦", "why": "프로세스 최적화·효율화에 즐거움."},
    ],
    "ESFJ": [
        {"name": "학교행정·학생지원", "emoji": "🏫", "why": "협력·소통과 실무 정리가 강점."},
        {"name": "행사기획·운영", "emoji": "🎉", "why": "사람과 사람을 연결하고 분위기를 만들기 좋음."},
        {"name": "의료서비스 코디", "emoji": "💟", "why": "배려와 조직화를 동시에 활용."},
    ],
    "ENFJ": [
        {"name": "교사·교육 리더", "emoji": "🧑‍🏫", "why": "동기부여·팀 빌딩·집단 성장에 강점."},
        {"name": "HR·조직문화", "emoji": "🤝", "why": "사람을 보고 성장 경로를 그리는 능력."},
        {"name": "커뮤니티 매니저", "emoji": "👥", "why": "집단을 조직하고 목표를 맞추는 역량."},
    ],
    "ENTJ": [
        {"name": "경영·사업 리더", "emoji": "📌", "why": "목표 설정·추진력·의사결정에 강점."},
        {"name": "제품·서비스 PM", "emoji": "🛠️", "why": "전략-실행을 잇고 팀을 조율."},
        {"name": "투자·비즈니스 분석", "emoji": "💼", "why": "수치·시장 관점을 바탕으로 확장 설계."},
    ],
}

# ------------------------------
# Helper functions
# ------------------------------

def render_result(mbti: str):
    st.subheader(f"{mbti} 유형을 위한 진로 아이디어 ✨")
    cols = st.columns(3)
    for i, job in enumerate(CAREERS[mbti]):
        with cols[i]:
            st.markdown(
                f"""
                <div style='padding:14px;border:1px solid #eee;border-radius:14px;'>
                    <div style='font-size:26px'>{job['emoji']}</div>
                    <div style='font-weight:700;margin-top:6px'>{job['name']}</div>
                    <div style='color:#555;margin-top:6px;font-size:14px'>{job['why']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    with st.expander("실천 팁 보기 🧰"):
        st.markdown(
            """
            - **동아리/활동**: 관심 분야 체험(예: 메이커·코딩·독서토론·봉사·영상제작).
            - **프로젝트**: 짧은 기간(2~4주) 목표를 정하고 **작은 포트폴리오** 만들기.
            - **기록**: 활동 일지·느낀 점·배운 점을 간단히 메모해 **성장 스토리**로 남기기.
            - **균형**: MBTI는 **참고용**이에요. 하고 싶은 일이 생기면 **직접 경험**해 본 뒤 조정해요.
            """
        )

# ------------------------------
# UI
# ------------------------------

st.title("중학생 MBTI 진로 추천 프로그램 🧭")
st.caption("청소년 상담 관점에서, 고정관념을 줄이고 **다양한 가능성**을 제안합니다. MBTI는 성격의 한 단면일 뿐이에요!")

left, right = st.columns([3, 2])
with left:
    mbti = st.selectbox(
        "MBTI를 선택하세요",
        options=sorted(CAREERS.keys()),
        index=sorted(CAREERS.keys()).index("ENFP") if "ENFP" in CAREERS else 0,
        help="선택 즉시 추천이 아래에 표시됩니다."
    )

with right:
    st.info("※ **주의**: MBTI는 과학적으로 고정된 직업 적성을 보장하지 않습니다. ")

render_result(mbti)

# 다운로드 기능
plan_text = f"[MBTI 진로 추천]\n유형: {mbti}\n추천 직업: " + ", ".join([j['name'] for j in CAREERS[mbti]]) + "\n메모: MBTI는 참고용이며, 실제 적합성은 경험과 학습에 따라 달라집니다."
st.download_button("추천 결과 TXT로 저장 📝", plan_text, file_name=f"mbti_{mbti}_careers.txt")

# 모든 유형 한눈에 보기
with st.expander("모든 MBTI 유형 추천 한눈에 보기 🗂️"):
    for t in sorted(CAREERS.keys()):
        st.markdown(f"### {t}")
        bullets = [f"{item['emoji']} {item['name']}" for item in CAREERS[t]]
        st.write(" • ".join(bullets))
        st.divider()

# 푸터
st.caption("© 2025 청소년 진로 상담 미니앱 – 고정관념을 피하고, 경험으로 탐색해요. 🌱")
