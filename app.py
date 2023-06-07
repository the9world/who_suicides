# # 한글 깨짐 방지 ( VS code )
from matplotlib import font_manager, rc

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.io as pio
from IPython.display import HTML
from app_module.app_home import run_app_home
from app_module.app_eda import run_app_eda
from app_module.app_ml import run_app_ml
from app_module.app_map import run_app_map
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)




def main():
    menu= ['Home', 'EDA', 'ML', 'Map']
    choice = st.sidebar.selectbox('메뉴', menu)
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
        st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
        st.text('좋은 서비스를 제공하겠습니다.')
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