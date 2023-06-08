# # 한글 깨짐 방지 ( VS code )
from matplotlib import font_manager, rc

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# import plotly.io as pio
from IPython.display import HTML
from app_module.app_home import run_app_home
from app_module.app_eda import run_app_eda
from app_module.app_ml import run_app_ml
from app_module.app_map import run_app_map
import platform # 폰트용
from matplotlib import rc
import matplotlib.pyplot as plt

plt.rcParams['font.family'] ='NanumGothic'
plt.rcParams['axes.unicode_minus'] =False
plt.rcParams['axes.unicode_minus'] = False
# rc('font', family=font_name)
if platform.system()=='Linux':
    rc('font', family= 'NanumGothic')

def main():

    with st.sidebar:
        # img_url= 'https://cphoto.asiae.co.kr/listimglink/1/2016090911072745990_1.jpg'
        # st.image(img_url)
        
        st.sidebar.image('https://cdn.newspost.kr/news/photo/202109/94483_96057_3538.jpg')
        menu= ['🏚️ Home', '📊E D A (탐색적 데이터 분석)', '🧭 Predict The Future (미래예측)', '🗺️ World Map Chart (세계지도)']
        choice = st.sidebar.selectbox('메뉴', menu)
        st.sidebar.image('https://cdn.swupress.swu.ac.kr/news/photo/202109/10830_10662_2056.jpg')
        st.sidebar.image('https://img.hankyung.com/photo/202102/AD.25367487.1.jpg')
        st.markdown("""
                    <span style='color:#31B675; font-size:15px; font-weight:bold;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;그림 by.연작가 </span>""", unsafe_allow_html=True)
        st.markdown(""" <style> [class^="st-b"] { color: red; } </style>""",
                    unsafe_allow_html=True )
        
        st.markdown(
            """
            <style>
            body {
                background-color: #f1f1f1;
            }
            </style>
            """,
            unsafe_allow_html=True)
        
        
    # # st.title("University Ranking in the UK")University Ranking in the UK
    # st.markdown("""<span style='color:#31B675; font-size:50px; font-weight:bold;'> WHO Suicides </span>
    #             <span style='color:black; font-size:20px;'> ( 세계보건기구 자살데이터 )</span>""", unsafe_allow_html=True)

    # st.video('https://www.youtube.com/watch?v=CckoVylNr1o')
    # st.markdown("""<span style='color:#006494; font-size:20px;'>보건복지상담센터  </span>
    #             <span style='color:#BA4160; font-size:30px; font-weight:bold;'>  129 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
    #             <span style='color:#006494; font-size:20px;'>자살예방상담전화  </span>
    #             <span style='color:#BA4160; font-size:30px; font-weight:bold;'>  1393  </span>""", unsafe_allow_html=True)
    # st.markdown("""<span style='color:#006494; font-size:20px;'>생명의전화  </span>
    #             <span style='color:#BA4160; font-size:30px; font-weight:bold;'>  1588-9191&nbsp;&nbsp;</span>
    #             <span style='color:#006494; font-size:20px;'>정신건강위기상담전화  </span>
    #             <span style='color:#BA4160; font-size:30px; font-weight:bold;'>  1577-0199</span>""", unsafe_allow_html=True)
    # st.markdown("""<span style='color:#006494; font-size:20px;'>여성긴급전화  </span>
    #             <span style='color:#BA4160; font-size:30px; font-weight:bold;'>  1366&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
    #             <span style='color:#006494; font-size:20px;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;학교폭력예방 상담전화  </span>
    #             <span style='color:#BA4160; font-size:30px; font-weight:bold;'>  117</span>""", unsafe_allow_html=True)
    
    # new_title = '<p style="font-family:sans-serif; color:pink; font-size: 50px;">gggggggggggg</p> '
    # st.markdown(new_title, unsafe_allow_html=True)
    # menu= ['Home', 'EDA', 'ML']
    # choice = st.sidebar.selectbox('메뉴', menu)
    
    if choice == menu[0] :
        run_app_home()

        # st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
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


        # img_url= 'https://www.irishtimes.com/resizer/pPJML7tkKkfBuXUYNfRzjnQxqjI=/1600x0/filters:format(jpg):quality(70)/cloudfront-eu-central-1.images.arcpublishing.com/irishtimes/XPHTWNJW3THZZ3UTNI3RDXXOPE.jpg'
        # st.image(img_url)
    
    elif choice == menu[1] :
        run_app_eda()

    
    elif choice == menu[2]:
        run_app_ml()
        
    else:
        run_app_map()


if __name__=='__main__':
    main()