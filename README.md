![header](https://capsule-render.vercel.app/api?section=footer&type=slice&reversal=true&color=gradient&height=170&text=WHO%20Suicides%20Statistics&animation=twinkling&fontSize=53&fontColor=fed&fontAlign=50&fontAlignY=50&textBg=true&&rotate=-3&desc=the9world&descSize=20&descAlign=50&descAlignY=15&stroke=9F1FF0&strokeWidth=1&)

# ☑️ WHO Suicides Statistics
<br><br>
![2023-10-19 16 59 39 home](https://github.com/the9world/who_suicides/assets/130967390/7aa1278a-3f41-438c-9373-66d61fdfb93b)

## 1. 프로젝트 정보  
✔ 과거 WHO Suicidies 데이터를 토대로 predict the future 결과와  
현시점 실제 자살률 데이터와 비교하여 어느정도 예측이 정확한지,  
예측 데이터와 현재 데이터를 비교하여 예측 값에 오차가 있다면,  
어떤 요인들이 오차에 영향을 끼쳤는지 그 요인들을 분석하여,  
자살률 감소에 도움이 될 수 있는지 알아보고자 WHO Suicides 데이터를 분석하였음.


## 2. 프로젝트 소개  
✔ 분석한 데이터는 1979년 ~ 2016년 국가별, 연령대별, 남녀별 자살률 데이터로  
Kaggle에서 수집하여 Python으로 Pandas를 사용하여 데이터를 분석하고,  
Seaborn, Matplotlib, Plotly 등을 사용하여 그래프 시각화 하였고,  
FaceBook Prophet을 사용하여 미래 예측하였으며,  
Streamlit과 AWS EC2 Anaconda 가상환경에서 테스트 및 배포하였음.

## 3. Progress period  
✔ 기간 : 2023-06-05 ~ 2023-06-07 (3일)  
1일차 : 데이터 분석, 시각화 및 미래예측  
2일차 : streamlit 코드 작성 및 Test & AWS EC2 가상환경에서 TEST  
3일차 : EC2 최종점검 및 README.MD 작성

## 4. 배포 주소(URL)  
✔ http://ec2-15-165-74-90.ap-northeast-2.compute.amazonaws.com:9999/  

## 5. Layout
WHO Suicdes 내용이 다소 네거티브하고 무거운 주제의 데이터인 만큼  
페이지를 전체적으로 다채롭고 다양한 색상의 플롯들과  
포지티브한 이미지를 조합하여 밝은 분위기를 연출하였습니다.  

## 6. Skills
### ✔ Platforms  
<img src="https://img.shields.io/badge/windows-0078D6?style=for-the-badge&logo=windows&logoColor=white"><img src="https://img.shields.io/badge/linux-FCC624?style=for-the-badge&logo=linux&logoColor=black"><img src="https://img.shields.io/badge/ANACONDA-44A833?style=badge&logo=anaconda&logoColor=white"><img src="https://img.shields.io/badge/AMAZON-AWS-232F3E?style=badge&logo=amazonaws&logoColor=white"><img src="https://img.shields.io/badge/GITHUB-181717?style=badge&logo=github&logoColor=white">

### ✔ Languages & Tools & Library  
<img src="https://img.shields.io/badge/PYTHON-3776AB?style=for-the-badge&logo=python&logoColor=white"><img src="https://img.shields.io/badge/GIT-F05032?style=badge&logo=git&logoColor=white"><img src="https://img.shields.io/badge/GOOGLE-COLAB-F9AB00?style=badge&logo=googlecolab&logoColor=white"><img src="https://img.shields.io/badge/STREAMLIT-FF4B4B?style=badge&logo=streamlit&logoColor=white"><img src="https://img.shields.io/badge/PLOTLY-3F4F75?style=badge&logo=plotly&logoColor=white"><br><img src="https://img.shields.io/badge/SEABORN-150458?style=badge&logoColor=white"><img src="https://img.shields.io/badge/MATPLOTLIB-D70F64?style=badge&logoColor=white"><img src="https://img.shields.io/badge/PANDAS-E40000?style=badge&logoColor=white"><img src="https://img.shields.io/badge/PROPHET-FF7300?style=badge&logoColor=white">
<br><br>
<img alt="Html" src ="https://img.shields.io/badge/Python-3.9.16-red&logo=ff&logoColor=fed"/>

- 출처<br>
  1.  사이드바 이미지출처:  
  연작가 : https://www.instagram.com/yeon.writer.1983/
  2.  데이터 출처 :  
  Kaggle : https://www.kaggle.com/
<br><br>


<span style="color:white; font-weight:400;font-size:18px">
URL Sample Image</span>
<details><summary> 
<span style="color:#2D57A9;font-weight:400;font-size:15x">
☑️[Click : 펼치기 / 접기]</span>
</summary>

<img src="https://github.com/the9world/who_suicides/assets/130967390/a093298e-cf26-4361-917d-cdb31310e944" width="330" height="480"/>
<img src="https://github.com/the9world/who_suicides/assets/130967390/ad8cada5-b6c1-42bc-9550-7f6593dd2ff4" width="330" height="480"/>
<img src="https://github.com/the9world/who_suicides/assets/130967390/fbb962e1-3a04-453f-9e1e-2bb6b8b00676" width="330" height="480"/>
</details>
<br>

<span style="color:white; font-weight:400;font-size:18px">
Sample Image의 Map Code</span>
<details><summary> 
<span style="color:#2D57A9;font-weight:400;font-size:15x">
☑️[Click : 펼치기 / 접기]</span>
</summary>
<br>

seaborn과 plotly를 활용하여 파이차트와 lineplot등을 생성
```python


        if st.checkbox( '남녀 자살률 비교 ', value=True):
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

        with col2:
            st.subheader("2️⃣World & Korea 자살 비교")
            # 세계 데이터 평균과 한국 데이터 연도별 자살 비교
            fig_world_korea, ax = plt.subplots()
            sns.lineplot(data=df, x='year', y='suicides_no', color='r', label='World')
            sns.lineplot(data=df_kor, x='year', y='suicides_no', color='black', label='Korea')
            ax.set_title('World & Korea', fontsize=25, color='#959EA2')
            ax.legend()

            st.pyplot(fig_world_korea)
```

  
plotly express의 px.choropleth 함수 사용

```python
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
```

</details>
<br>
<br>
<br>
<details>  </details>


<span style="color:red; font-weight:600;font-size:30px">
Python Error, Debuging
</span>
<details><summary>
<span style="color:#2D57A9;font-weight:500;font-size:16px">
☑️[Click : 펼치기 / 접기]</span>
</summary>

```python
# tab 기능 Warning message
tab1, tab2 = st.tabs(df, df1)
   with tab1:
   with tab2:
"""
Streamlit의 st.tab을 사용하면
대시보드에서 st.tab은 beta 기능이라는 Warning 메세지가 출력되어
비슷한 기능인 st.columns로 대체하였음.
"""
col1, col2 = st.columns(2)
   with col1:
   with col2:
```

```python
# 1. 미래예측 에러

df_prophet= df.copy()
df_prophet.reset_index(drop=False, inplace=True)
df_prophet.columns = ['ds', 'y']
df_prophet= df_prophet[:]

m= Prophet()
m.fit(df_prophet)
future= m.make_future_dataframe(periods=5, freq='Y')
forecast= m.predict(future)

fig= m.plot(forecast)

""" 
Prophet을 활용한 미래예측에는 YY/MM/DD(년월일) 전부가 필요하지만,
who_suicides의 year column은 "연도" 뿐인 데이터라서 Prophet에서 error가 발생,
기존 데이터 year column의 값 "연도"에 +"-01-01"을 추가하여 해결하였다.
"""

# 2. 해결

df['year'] = df['year'].astype(str) + '-01-01'

df_prophet= df.copy()
df_prophet.reset_index(drop=False, inplace=True)
df_prophet.columns = ['ds', 'y']
df_prophet= df_prophet[:]

m= Prophet()
m.fit(df_prophet)
future= m.make_future_dataframe(periods=5, freq='Y')
forecast= m.predict(future)

fig= m.plot(forecast)
```
</details>

---
<br>
<span style="color:red;font-weight:600;font-size:30px">
EC2 가상환경 Font Error</span>  

<span style="color:#000000;font-weight:600;font-size:16px">
(출처: https://luvris2.tistory.com/119)
</span>
<details><summary>
<span style="color:#2D57A9;font-weight:500;font-size:16px">
☑️[Click : 펼치기 / 접기]</span>
</summary>  

   - 폰트 관리 유틸리티 설치
```
sudo yum install fontconfig
```

   - 네이버 나눔 폰트 다운로드 후 압축 풀기
```
curl -o nanumfont.zip http://cdn.naver.com/naver/NanumFont/fontfiles/
NanumFont_TTF_ALL.zip 

sudo unzip -d /usr/share/fonts/nanum nanumfont.zip
```

  - 시스템 내 폰트의 캐쉬 정보 업데이트 (-f:강제생성, -v:진행도보기)
```
sudo fc-cache -f -v
```

   - 폰트 리스트 확인
```
fc-list
```

1. 리눅스(linux) 운영체제에서 matplotlib 한글 사용하기  
   - 한글폰트 유무 확인
fontconfig 를 이용하여 사용할 한글 폰트 확인  
저는 나눔고딕체를 사용할 예정이며, 리눅스 폰트 폴더에 설치해둔 상태입니다.  

- 터미널에서 fc-list 명령어 실행
     - 설치된 한글 폰트의 이름 확인
```
fc-list
```

- 한글폰트 설정
python을 입력하여 아래의 코드를 한 줄 한 줄 쳐서 확인  
파이썬의 버전과 설치 위치, 캐시 정보가 담긴 폴더의 이름을 알기 위함  
```
# 터미널에 입력
python
```
```
# 파이썬 에디터에 입력
import matplotlib
print(matplotlib.__version__) # matplotlib 버전확인
print(matplotlib.__file__) # 설치 폴더 경로 확인
print(matplotlib.get_cachedir()) # 캐시 폴더 경로 확인
```
- matplotlib에 한글 폰트 추가
  - 위에서 확인한 자신의 설치 폴더 경로에 맞게 폰트를 복사해줍니다.
  - 그 후 matplotlib의 폰트 캐시를 삭제합니다.  
      이는 새로 설치한 폰트를 업데이트해주는 역할을 합니다.
  - 저는 폰트 폴더에 모든 파일을 복사해서 넣어주었습니다.

```
# 터미널에 입력
#sudo cp -r /usr/share/fonts/truetype/nanum/Nanum* 아까 확인한 설치 폴더 위치+mpl-data/fonts/ttf/

sudo cp -r /usr/share/fonts/* /home/ec2-user/anaconda3/envs/streamlit3.7/lib/python3.7/site-packages/matplotlib/mpl-data/fonts/ttf/

rm -rf /home/ec2-user/.cache/matplotlib/*
```

- matplotlib에 한글 폰트 확인
  - python을 입력하여 아래의 코드를 한줄한줄 쳐서 확인해봅니다.
  - 이는 matplotlib에 추가한 한글 폰트가 정상적으로 추가되었는지 확인하기 위함입니다.
  - 코드 입력시 리스트가 보인다면 성공적으로 한글 폰트가 추가된 것입니다.
```
# 터미널에 입력
python
```

```
# 파이썬 에디터에 입력
import matplotlib
import matplotlib.font_manager

# 폰트 전체 리스트 확인
[i.fname for i in matplotlib.font_manager.fontManager.ttflist]

# 나눔 폰트 설치 확인
[f.name for f in matplotlib.font_manager.fontManager.ttflist if 'Nanum' in f.name]
```
</details>  

---  
