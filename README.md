# ☑️ WHO Suicides Statistics

1. 라이브러리
   - streamlit, matplotlib, pandas, seaborn, streamlit_extras,  
plotly, time, prophet
   - 폰트용 : platform  


2. 출처
   1.  사이드바 이미지출처: 연작가
   2.  데이터 출처 캐글, 


px(플로틀리익스프레스) choropleth 지도함수  

프로젝트 정보  
해당 프로젝트를 진행한 단체나 목적에 대해 소개하고, 개발 기간을 써준다.  

(5) 배포 주소  
프로젝트가 배포되어 있다면, 해당 주소를 기입해준다.  
(7) 프로젝트 소개
진행한 프로젝트에 대해 간단하게 5~10줄 정도 써준다.  

시작 가이드  
(1) 요구 사항
누군가가 이 프로젝트를 clone해서 실행하려고 할 때 필요한 요구사항들과 버전들을 적어준다.

(2) 설치 및 실행
Repository를 clone하고, 패키지 설치, 환경변수 설정, 실행하는 과정에 대한 내용들을 코드로 적어준다.  

화면 구성/API 주소  

<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/linux-FCC624?style=for-the-badge&logo=linux&logoColor=black">
<img src="https://img.shields.io/badge/amazonaws-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white">
<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
<img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">
<img src="https://img.shields.io/badge/googlecolab-F9AB00?style=for-the-badge&logo=git&logoColor=white">
<img src="https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=git&logoColor=white">
<img src="https://img.shields.io/badge/plotly-3F4F75?style=for-the-badge&logo=git&logoColor=white">
<img height="32" width="32" src="https://cdn.simpleicons.org/simpleicons/hotpink" />


[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=the9world)](https://github.com/the9world/github-readme-stats)

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=the9world&layout=pie)](https://github.com/the9world/github-readme-stats)  


|<img src="https://github.com/~~~.png" width="80">|<img src="https://github.com/~~~.png" width="80">|
|:---:|:---:|
|[](https://github.com/ImInnocent)|[](https://github.com/dearyeon)|
|블록체인|프론트엔드|

<h1 align="center"> 🛠 Tech Stack 🛠 </h1>
<h2 align="center"> 🛠 Tech Stack 🛠 </h2>
<h3 align="center"> 🛠 Tech Stack 🛠 </h3>
<h4 align="center"> 🛠 Tech Stack 🛠 </h4>
<h5 align="center"> 🛠 Tech Stack 🛠 </h5>
<h6 align="center"> 🛠 Tech Stack 🛠 </h6>   

```python
# 1. 에러가 떳었다 이유는 모른다.

st.subheader('내가 원하는 국가 데이터 보기')
df_country = df['country'].unique()
df_country = ['"Select Country"'] + list(df_country)
sel_country = st.selectbox('국가를 선택하세요', df_country)
       
        
if sel_country != '"Select Country"':
    filtered_df = df[df['country'] == sel_country]
    st.dataframe(filtered_df)
    st.text(filtered_df.shape)
```

```python
# 에러
        tab1, tab2 = st.tabs(df, df1)
        with tab1:
        with tab2:
# 베타 함수였어서 새로 바뀐거로 써야했다.
        col1, col2 = st.columns(2)
       
        with col1:
        with col2:
```

<details><summary>Python Error 해결
</summary>

```python
# 1. 미래예측 에러

data= pd.DataFrame(data.groupby(['year'])['suicides_no'].sum()).reset_index()
data= data.sort_values(by=['suicides_no'], ascending=False)
data= data.set_index('year')

df_prophet= data.copy()
df_prophet.reset_index(drop=False, inplace=True)
df_prophet.columns = ['ds', 'y']

m= Prophet()
m.fit(df_prophet)
future= m.make_future_dataframe(periods=5, freq='Y')
forecast= m.predict(future)

fig= m.plot(forecast)

""" 
Prophet을 활용한 미래예측에는 YY/MM/DD(년월일) 전부가 필요하지만,
who_suicides의 year column은 연도만 있는 데이터라서 Prophet에서 error가 발생,
데이터를 새로 불러서 기존 데이터에 year의 값을 "연도-01월-01일"으로 파싱하여 해결하였다.
"""

# 2. 해결

parse = lambda dates: pd.to_datetime(dates, format='%Y')
   data= pd.read_csv('https://raw.githubusercontent.com/the9world/My_Study/main/data/Z_running_file/who_suicide_statistics.csv',
   parse_dates=['year'], index_col='year', date_parser=parse)

   data= pd.DataFrame(data.groupby(['year'])['suicides_no'].sum()).reset_index()
   data= data.sort_values(by=['suicides_no'], ascending=False)
   data= data.set_index('year')

   df_prophet= data.copy()
   df_prophet.reset_index(drop=False, inplace=True)
   df_prophet.columns = ['ds', 'y']
   df_prophet= df_prophet[:]

   m= Prophet()
   m.fit(df_prophet)
   future= m.make_future_dataframe(periods=5, freq='Y')
   forecast= m.predict(future)
   
   fig= m.plot(forecast)
```

``` python
폰트에러 적어봅시다
```