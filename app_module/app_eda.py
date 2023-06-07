import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

def run_app_eda():
        st.subheader('데이터 분석')
        df1= pd.read_csv(r"data\who_suicide_statistics.csv")
        df = pd.read_csv(r"data\who_suicide_statistics.csv")
        if st.checkbox('데이터 프레임 원본 보기', value=True) :
            st.dataframe(df1)
            st.markdown("""<span style='color:#006494; font-size:18px;'>데이터 출처:<br></span>
                <span style='color:#BA4160; font-size:15px; font-weight:bold;'>
                https://www.kaggle.com/datasets/vishaljiodedra/university-ranking-in-the-uk?select=uni_dataset.csv</span>
                """, unsafe_allow_html=True)
        
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
        # 비교할 때 사용하기 위해 한국 데이터만 따로 변수에 저장
        df_kor = df.groupby('country').get_group('Republic of Korea')
        df_kor.reset_index(drop=True, inplace=True)
                
        
        if st.checkbox('데이터 전처리 보기') :
            st.dataframe(df)
            st.text('전처리 설명')

        if st.checkbox('기본 통계 데이터 보기') :
            st.dataframe(df.describe(include="all"))
        
        if st.checkbox('데이터 내의 나라들 보기'):
            st.dataframe(df['country'].unique())

        if st.checkbox('데이터 내의 연령대 보기'):
            st.dataframe(df['age'].unique())

        st.subheader('내가 원하는 국가 데이터 보기')
        df_country = df['country'].unique()
        df_country = ['"Select Country"'] + list(df_country)
        sel_country = st.selectbox('국가를 선택하세요', df_country)
        if sel_country != '"Select Country"':
            filtered_df = df[df['country'] == sel_country]
            st.dataframe(filtered_df)
                    
        if st.checkbox('Top 10 자살률 국가 그래프 보기'):                
            # 자살 건수가 많은 나라 Top10
            df_sui_n=pd.DataFrame(df.groupby(['country'])['suicides_no'].sum().reset_index())
            df_sui_n.sort_values(by=['suicides_no'],ascending=False,inplace=True)

            fig_bar,ax = plt.subplots()
            type_colors = ['#5D6D7E',  # Grass
                                '#633974',  # Fire
                                '#E74C3C',  # Water
                                '#283747',  # Bug
                                '#F4D03F',  # Normal
                                '#0B5345',  # Poison
                                '#154360',  # Electric
                                '#7B7D7D',  # Ground
                                '#229954',  # Fairy
                                '#641E16',  # Fighting
                            ]
            fig_bar.set_size_inches(25.15, 10,20)
            sns.set_context("paper", font_scale=1)

            f=sns.barplot(x=df_sui_n["country"].head(10),
                        y=df_sui_n['suicides_no'].head(10),
                        palette= type_colors)
            plt.xticks(fontsize=11)
            plt.yticks(fontsize=11)
            f.set_title('Top 10 Countries having highest no. suicides', fontsize=30)
            f.set_xlabel("Country",fontsize=25)
            f.set_ylabel("Suicides",fontsize=25)
            st.pyplot(fig_bar)
        
        if st.checkbox(' 나이별 자살률 그래프 보기'):  
            # 나이 자살 비교
            fig_age = go.Figure(data=[
                go.Pie(labels=df['age'], values=df['suicides_no'], textinfo='label+percent',
                    name='world_age', domain={'x': [0, 0.45]}),
                go.Pie(labels=df_kor['age'], values=df_kor['suicides_no'], textinfo='label+percent',
                    name='kor_age', domain={'x': [0.55, 1]})
            ])

            fig_age.update_layout(
                title={'text': "나이별 자살률", 'y': 0.95, 'x': 0.5, 'xanchor': 'right', 'yanchor': 'top'},
                annotations=[dict(text="""<span style='font-weight: bold; color: #B3A7DC'>↙World
                                  <span style='font-weight: bold; color: #84A7D3'>     Korea↘</span>""",
                                x=0.5, y=0.95, font_size=25, showarrow=False)])

            st.plotly_chart(fig_age)
       
        
        if st.checkbox( '남녀 자살률 비교 '):
            # 남녀 자살 비교, 세계 : 한국
            fig_sex = go.Figure(data=[
                go.Pie(labels=df['sex'], values=df['suicides_no'], textinfo='label+percent',
                    name='world_sex', domain={'x': [0, 0.45]},
                    marker=dict(colors=['hotpink', 'purple'])),
                go.Pie(labels=df_kor['sex'], values=df_kor['suicides_no'], textinfo='label+percent',
                    name='kor_sex', domain={'x': [0.55, 1]},
                    marker=dict(colors=['hotpink', 'purple']))])

            fig_sex.update_layout(
                title={'text': "sex suicides", 'y': 0.95, 'x': 0.5, 'xanchor': 'right', 'yanchor': 'top'},
                annotations=[dict(text="""<span style='font-weight: bold; color: #B3A7DC'>↙World
                                  <span style='font-weight: bold; color: #84A7D3'>     Korea↘</span>""",
                                x=0.5, y=0.95, font_size=25, showarrow=False)])

            st.plotly_chart(fig_sex)


        if st.checkbox('World & Korea 자살 비교'):
            # 세계 데이터 평균과 한국 데이터 연도별 자살 비교
            fig_world_korea, ax = plt.subplots()
            sns.lineplot(data=df, x='year', y='suicides_no', color='r', label='World')
            sns.lineplot(data=df_kor, x='year', y='suicides_no', color='black', label='Korea')
            ax.set_title('World & Korea', fontsize=25, color='#959EA2')
            ax.legend()

            # Display the figure in Streamlit
            st.pyplot(fig_world_korea)