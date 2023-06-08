import plotly.express as px
import pandas as pd 
import streamlit as st
import plotly.io as pio
import numpy as np
import time
def run_app_map():

    with st.spinner('🗺️ 지도를 그리는 중.. ☠️☠️'):
        time.sleep(1.5)

        df = pd.read_csv('https://raw.githubusercontent.com/the9world/My_Study/main/data/Z_running_file/who_suicide_statistics.csv')
        df.fillna(0, inplace=True) # suicides_no 열의 결측치를 min 값으로 대체
        df.reset_index(drop=True, inplace=True) # 인덱스 재정의, 기존 인덱스를 제거하고 새로 인덱스를 부여
        
        df= df.loc[df['year']<2016] # 2016년도 데이터 다른 년도 데이터보다 1/10 밖에 안되기 때문에, 2016 데이터는 제외
        df= df.loc[df['year']>=1985]
        
        df['age'] = df['age'].str.replace(' years', '')
        df['age'] = df['age'].replace('5-14', '05-14')
        age_order = ['05-14', '15-24', '25-34', '35-54', '55-74', '75+']  # 원하는 정렬 순서 지정
        df['age'] = pd.Categorical(df['age'], categories=age_order, ordered=True)  # 정렬 순서 적용
        
        df.sort_values(['age', 'country', 'year'], inplace=True)
        df.reset_index(drop=True,inplace=True)

        df.drop('population', axis=1, inplace=True)
        
        count_max_sui=pd.DataFrame(df.groupby(['year','country'])['suicides_no'].sum().reset_index())

        fig4 = px.choropleth(count_max_sui.sort_values("year"), 
                                locations = 'country',
                                color = "suicides_no",
                                color_continuous_scale = 'bluyl',
                                locationmode='country names',
                                animation_frame= 'year')
        fig4.update_layout( title=
                        {'text': 'World Suicides Map',
                            'y': 1.0,
                            'x': 0.15,
                            'yanchor': 'top',
                            'font': {'size': 45}        }     )
        st.plotly_chart(fig4)
        st.text('''지도를 확대, 축소, 이동이 가능합니다.
                재생을 누르거나 슬라이더를 움직여서 연도별로 지도를 확인하세요''')


        st.subheader('👨‍👩‍👧‍👦 대한민국 10년간 자살현황')
        st.text(""" 
        2021년 자살사망자 수는 13,352명으로 전년 대비 157명(1.2%) 증가하였고,
        1일 평균 자살사망자 수는 36.5명입니다.
        자살률(인구 10만 명당)은 26.0명으로 전년 대비 0.3명(1.2%) 증가하였습니다.
        연령별 자살률을 살펴보면 10~30대, 70대의 경우 전년도보다 증가하였으며,
        40~60대, 80세 이상은 전년도 보다 감소하였습니다. 
        성별 자살률을 살펴보면 남자는 35.9명(1.2%)으로 전년도 보다 증가하였고,
        여자는 16.2명(1.4%)으로 전년도 보다 증가하였습니다.
        남녀 간 자살률 성비는 10대가 1.1배로 가장 낮았으며,
        80세 이상이 3.7배로 가장 높게 나타났습니다.
                                                -⚖️한국생명존중희망재단⚖️-""")