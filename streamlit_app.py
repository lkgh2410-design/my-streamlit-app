

import streamlit as st
import pandas as pd
import numpy as np

# 1. [텍스트] 제목 및 목표 설정
st.title("🎸 Music Practice Tracker")
st.markdown("매일의 기타 연습과 음악 이론 공부 시간을 기록하고 관리합니다.")

# --- 데이터 준비 (하드코딩된 커리큘럼) ---
practice_list = {
    "구분": ["기타 연주", "기타 연주", "음악 이론", "음악 이론"],
    "항목": ["스케일/코드", "자유 곡 연주", "화성학", "청음/리듬"],
    "권장 시간(분)": [30, 60, 40, 20]
}
df_plan = pd.DataFrame(practice_list)

# 2. [위젯] 사이드바에서 오늘 공부/연주 내용 입력
st.sidebar.header("오늘의 연습 기록")
category = st.sidebar.radio("어떤 연습을 하셨나요?", ["기타 연주", "음악 이론"])
study_time = st.sidebar.slider("연습 시간 (분)", 0, 180, 60, step=10)

# 3. [상호작용] 목표 달성률 계산
# 목표 시간을 100분이라고 가정했을 때의 달성률
goal_time = 100
achievement_rate = (study_time / goal_time) * 100

# 4. [데이터] 지표(Metric) 및 테이블 표시
st.header(f"오늘의 {category} 리포트")
col1, col2 = st.columns(2)

with col1:
    # 실시간으로 변하는 연습 시간과 달성률 표시
    st.metric(label="총 연습 시간", value=f"{study_time} 분", delta=f"{study_time - goal_time} (목표 대비)")

with col2:
    # 연습 권장 가이드 표 표시
    st.write("권장 연습 가이드")
    st.dataframe(df_plan[df_plan["구분"] == category])

# 5. [차트] 주간 연습 추이 (가상 데이터)
st.header("이번 주 연습 통계")
# 오늘 입력한 시간에 따라 차트의 마지막 값이 변하도록 설정
weekly_data = pd.DataFrame({
    "요일": ["월", "화", "수", "목", "금", "토", "일"],
    "연습시간(분)": [45, 80, 30, 90, 60, 120, study_time] 
})

# 선 그래프 또는 영역 그래프로 시각화
st.area_chart(weekly_data.set_index("요일"))

st.success(f"오늘도 {study_time}분 동안 멋진 연주를 하셨네요! 계속 정진하세요. 🔥")
