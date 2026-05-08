import streamlit as st
import pandas as pd
import numpy as np

# ── 여기서부터 자유롭게 수정하세요 ───────────────

st.title("📈 내 주식 포트폴리오 시뮬레이터")   # ← 앱 제목을 주식 테마로 수정

# ── 사이드바 ──────────────────────────────────
st.sidebar.title("설정")

chart_type = st.sidebar.radio(
    "차트 유형",
    ["꺾은선 그래프", "막대 그래프", "면적 그래프"]   
)

n = st.sidebar.slider(
    "데이터 개수",
    min_value=10,    
    max_value=100,   
    value=30
)

# ── 메인 화면 ─────────────────────────────────
st.write("가상의 주식 3종목에 대한 가격 변동 추이를 확인해보세요.")   # ← 설명을 테마에 맞게 수정

data = pd.DataFrame(
    np.random.randn(n, 3),
    columns=['삼성전자', '애플', '테슬라']   # ← 'A', 'B', 'C' 였던 컬럼 이름을 주식 종목으로
)

if chart_type == "꺾은선 그래프":
    st.line_chart(data)
elif chart_type == "막대 그래프":
    st.bar_chart(data)
else:
    st.area_chart(data)

st.dataframe(data.head(5))

# ── 여기까지 ──────────────────────────────────
