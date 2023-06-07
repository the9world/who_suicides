import streamlit as st
import numpy as np
import pandas as pd
from streamlit_extras.let_it_rain import rain

def run_app_home():
        
    # st.title("University Ranking in the UK")University Ranking in the UK
    st.markdown("""<span style='color:#31B675; font-size:50px; font-weight:bold;'> 🏴WHO </span>
                <span style='color:black; font-size:30px;'> Suicides </span>
                <span style='color:#31B675; font-size:50px; font-weight:bold;'>  Statistics </span>""", unsafe_allow_html=True)
    

    st.video('https://www.youtube.com/watch?v=CckoVylNr1o')
    st.markdown("""<span style='color:#006494; font-size:20px;'>✨보건복지상담센터  </span>
                <span style='color:#BA4160; font-size:25px; font-weight:bold;'>  📞129 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
                <span style='color:#006494; font-size:20px;'>✨자살예방상담전화  </span>
                <span style='color:#BA4160; font-size:25px; font-weight:bold;'>  📞1393  </span>""", unsafe_allow_html=True)
    st.markdown("""<span style='color:#006494; font-size:20px;'>✨생명의전화  </span>
                <span style='color:#BA4160; font-size:25px; font-weight:bold;'>  📞1588-9191&nbsp;&nbsp;</span>
                <span style='color:#006494; font-size:20px;'>✨정신건강위기상담전화  </span>
                <span style='color:#BA4160; font-size:25px; font-weight:bold;'>  📞1577-0199</span>""", unsafe_allow_html=True)
    st.markdown("""<span style='color:#006494; font-size:20px;'>✨여성긴급전화  </span>
                <span style='color:#BA4160; font-size:25px; font-weight:bold;'>  📞1366&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
                <span style='color:#006494; font-size:20px;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✨학교폭력예방 상담전화  </span>
                <span style='color:#BA4160; font-size:25px; font-weight:bold;'>  📞117</span>""", unsafe_allow_html=True)


    rain(
        emoji=" /            /               /                    /",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )
    
    # new_title = '<p style="font-family:sans-serif; color:pink; font-size: 50px;">gggggggggggg</p> '
    # st.markdown(new_title, unsafe_allow_html=True)