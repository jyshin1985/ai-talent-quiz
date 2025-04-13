
import streamlit as st

st.set_page_config(page_title="AI 시대 핵심 인재유형 진단", layout="centered")

st.title("✨ AI 시대, 당신은 어떤 핵심 인재인가요?")
st.subheader("총 5개의 질문에 답하고, 나만의 인재유형을 확인해보세요!")

questions = [
    {
        "question": "Q1. 새로운 AI 툴을 보면 나는?",
        "options": [
            ("바로 써본다", "Tool Master"),
            ("써본 친구의 리뷰를 먼저 듣는다", "Connector"),
            ("필요하면 쓰고, 안 쓰면 안 쓴다", "Doer"),
            ("낯설어서 일단 피한다", "Humanist"),
        ],
    },
    {
        "question": "Q2. 회의할 때 나는?",
        "options": [
            ("실행 방안을 바로 말한다", "Doer"),
            ("전체 그림을 먼저 그린다", "Visionary"),
            ("사람들 반응을 잘 살핀다", "Humanist"),
            ("정보를 모아 정리한다", "Synthesizer"),
        ],
    },
    {
        "question": "Q3. 사람들과 협업할 때 나는?",
        "options": [
            ("실행 속도로 리드한다", "Doer"),
            ("사람과 사람을 연결한다", "Connector"),
            ("데이터/정보 정리에 강하다", "Synthesizer"),
            ("공감과 배려로 분위기를 이끈다", "Humanist"),
        ],
    },
    {
        "question": "Q4. 콘텐츠나 기획을 할 때 나는?",
        "options": [
            ("도구나 기능을 먼저 떠올린다", "Tool Master"),
            ("누가 이걸 어떻게 쓸까 생각한다", "Connector"),
            ("왜 해야 하는지, 큰 그림을 그린다", "Visionary"),
            ("다양한 자료를 모아 정리한다", "Synthesizer"),
        ],
    },
    {
        "question": "Q5. 새로운 프로젝트가 시작되면 나는?",
        "options": [
            ("할 일을 빠르게 실행에 옮긴다", "Doer"),
            ("아이디어를 다양하게 연결해본다", "Connector"),
            ("사람들에게 의미를 전한다", "Humanist"),
            ("큰 방향성과 전략을 먼저 세운다", "Visionary"),
        ],
    },
]

# User answers
profile_scores = {
    "Tool Master": 0,
    "Connector": 0,
    "Doer": 0,
    "Humanist": 0,
    "Visionary": 0,
    "Synthesizer": 0,
}

for i, q in enumerate(questions):
    st.markdown(f"**{q['question']}**")
    selected = st.radio(f"question_{i}", [opt[0] for opt in q["options"]], index=0)
    for opt in q["options"]:
        if selected == opt[0]:
            profile_scores[opt[1]] += 1

if st.button("결과 확인하기"):
    result = max(profile_scores, key=profile_scores.get)

    descriptions = {
        "Tool Master": "새로운 도구를 빠르게 익히고 누구보다 잘 활용하는 실전형 인재!",
        "Connector": "사람, 아이디어, 도구를 유연하게 연결하는 네트워크 플레이어!",
        "Doer": "계획보다 행동! 빠르게 실행해서 변화를 이끄는 실천가!",
        "Humanist": "감정과 공감 능력으로 사람을 움직이는 진정한 사람 전문가!",
        "Visionary": "큰 그림을 그리고 전략을 제시하는 미래 설계자!",
        "Synthesizer": "정보를 모아 정리하고 통합해주는 조율자형 인재!",
    }

    st.success(f"당신의 인재유형은: **{result}**")
    st.markdown(f"**{descriptions[result]}**")
    st.markdown("---")
    st.markdown("결과를 캡처해서 인스타 스토리에 공유해보세요!")
