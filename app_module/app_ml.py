import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from prophet import Prophet
import warnings

def run_app_ml():
        st.title('미래예측')
    # 세계예측2 (1985~2015 데이터)
    # 한국이 1985년도부터 데이터가 있어서 한국과 비교를 위해 해당 데이터를 1985부터 사용
        tab1, tab2= st.tabs(["World, predict the future ", "Korea, predict the future"])
        # 데이터 로딩 함수는 여기에!
        with tab1:
            st.success('World 미래예측 완료☠️')
            
            dateparse = lambda dates: pd.to_datetime(dates, format='%Y')
            data = pd.read_csv('https://raw.githubusercontent.com/the9world/My_Study/main/data/Z_running_file/who_suicide_statistics.csv', parse_dates=['year'], index_col='year', date_parser=dateparse)
            data.drop('population', axis=1, inplace=True)
            data.fillna(0, inplace=True)
            data = data.loc[(data.index >= '1985-01-01') & (data.index < '2016-01-01')]
            data = data.reset_index()
            data = pd.DataFrame(data.groupby(['year'])['suicides_no'].sum()).reset_index()
            data = data.sort_values(by=['suicides_no'], ascending=False)
            data = data.set_index('year')

            df_prophet = data.copy()
            df_prophet.reset_index(drop=False, inplace=True)
            df_prophet.columns = ['ds', 'y']
            df_prophet = df_prophet[:]

            m = Prophet()
            m.fit(df_prophet)
            future = m.make_future_dataframe(periods=5, freq='Y')
            forecast = m.predict(future)
            
            fig = m.plot(forecast)
            plt.title('World 미래예측 그래프', x=0.5, y=1.05, fontsize=30)
            st.pyplot(fig)
            
            fig_components = m.plot_components(forecast)
            fig_components.suptitle('World 미래예측 구성 요소', x=0.5, y=1.05, fontsize=25)
            st.pyplot(fig_components)

  
        with tab2:
            # 한국 미래 예측
            st.success('Korea 미래예측 완료☠️')
            
            dateparse_korea = lambda dates: pd.to_datetime(dates, format='%Y')
            data_korea= pd.read_csv('https://raw.githubusercontent.com/the9world/My_Study/main/data/Z_running_file/who_suicide_statistics.csv', parse_dates=['year'], index_col='year',date_parser=dateparse_korea)
            data_korea.fillna(data_korea.mean(),inplace=True)
            data_korea= data_korea.reset_index()
            data_korea= pd.DataFrame(data_korea.groupby(['country','year'])['suicides_no'].sum()).reset_index()
            data_korea= data_korea.sort_values(by=['suicides_no'],ascending=False)
            
            data_korea= data_korea.loc[data_korea['country']=='Republic of Korea']
            data_korea.drop('country',axis=1,inplace=True)
            data_korea= data_korea.set_index('year')

            df_prophet_korea= data_korea.copy()
            df_prophet_korea.reset_index(drop=False,inplace=True)
            df_prophet_korea.columns = ['ds','y']
            df_prophet_korea= df_prophet_korea[:]
            
            m_korea = Prophet()
            m_korea.fit(df_prophet_korea)
            future_korea = m_korea.make_future_dataframe(periods=5, freq='Y')
            forecast_korea = m_korea.predict(future_korea)
            
            fig_korea = m_korea.plot(forecast_korea)
            plt.title('Korea 미래예측 그래프', x=0.5, y=1.05, fontsize=30)
            st.pyplot(fig_korea)
            
            fig_korea_components = m_korea.plot_components(forecast_korea)
            fig_korea_components.suptitle('Korea 미래예측 구성 요소', x=0.5, y=1.05, fontsize=25)
            st.pyplot(fig_korea_components)

