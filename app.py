import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="Gemini와 삼성의 콜라보",
    page_icon="✨",
    layout="wide"
)

# 제목 및 부제목
st.title("✨ Gemini와 삼성의 콜라보")
st.markdown("### 삼성의 혁신 기술과 구글 Gemini의 만남")
st.write("---")

# 소개 섹션
st.header("1. 혁신을 주도하는 두 거인")
st.write("""
**구글의 Gemini**는 멀티모달(Multimodal) 능력을 갖춘 **최첨단 AI 모델**로, 텍스트, 이미지, 오디오, 비디오 등 다양한 형태의 정보를 동시에 이해하고 처리할 수 있습니다. 
반면, **삼성**은 전 세계 스마트폰, 가전, 반도체 시장을 선도하는 **글로벌 기술 리더**입니다. 
이 두 거인의 협력은 단순한 파트너십을 넘어, **일상생활의 혁신을 가속화**할 새로운 가능성을 열고 있습니다.
""")

# 주요 협력 사례 섹션
st.header("2. 주요 협력 사례")
st.markdown("---")

# 갤럭시 S24 시리즈
st.subheader("갤럭시 AI: 온디바이스 AI의 시작")
st.image("https://images.samsung.com/is/image/samsung/assets/global/about-us/gemini/galaxy-ai/galaxy-s24.png", caption="갤럭시 S24 시리즈", use_column_width=True)
st.write("""
삼성 **갤럭시 S24 시리즈**에 탑재된 **'갤럭시 AI'**는 Gemini의 기술을 활용해 혁신적인 온디바이스 AI 경험을 제공합니다. 
주요 기능으로는 **실시간 통역 통화**, **'서클 투 서치'**, **생성형 편집** 등이 있습니다. 
특히, 기기 자체에서 AI 기능을 처리하는 **온디바이스 AI**는 개인정보 보호와 빠른 응답 속도 면에서 큰 장점을 가집니다.
""")

st.write("---")

# 그 외 협력 분야
st.subheader("그 외 협력 분야")
st.markdown("##### 💡 삼성전자 기기에 Gemini Pro 탑재")
st.write("스마트폰, 태블릿 등 다양한 삼성 기기에서 Gemini Pro 모델을 활용해 AI 기능을 구현합니다.")

st.markdown("##### 💡 AI 가전과 스마트홈")
st.write("Gemini를 활용해 스마트 가전이 사용자의 생활 패턴을 학습하고, 더욱 개인화된 서비스를 제공할 수 있습니다.")

st.markdown("##### 💡 반도체 기술 협력")
st.write("삼성의 고성능 반도체(NPU, 신경망 처리 장치)와 Gemini AI 모델의 최적화를 위한 기술 협력도 활발히 진행됩니다.")

st.write("---")

# 결론 섹션
st.header("3. 미래를 향한 기대")
st.write("""
Gemini와 삼성의 협력은 단순한 제품 기능을 넘어, **사용자의 삶을 더욱 스마트하고 편리하게** 변화시키는 것을 목표로 합니다. 
이러한 협업은 앞으로 AI 기술이 우리 일상에 어떻게 녹아들지 보여주는 중요한 이정표가 될 것입니다.
""")

st.write("---")

# 푸터
st.markdown("© 2025 Powered by Gemini & Samsung Collaboration")
