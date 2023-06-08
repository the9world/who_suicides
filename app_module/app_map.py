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

