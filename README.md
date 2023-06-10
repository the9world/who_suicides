![header](https://capsule-render.vercel.app/api?type=cylinder&height=150&text=WHO%20Suicides%20Statistics&fontAlign=50&stroke=FF0000&strokeWidth=2)



# ☑️ WHO Suicides Statistics
<br><br>

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


1. 프로젝트 Description (설명서:기재 사항)

✔ 프로젝트명: WHO Suicides 데이터 분석 및 시각화<br>
✔ 어떤 프로젝트인지 소개:  
WHO Suicides 데이터를 분석하고 시각화 하여 향후 전망을 예측한다.  <br>
✔ 디렉토리 구조<br>

2. 프로젝트 정보

✔ 설치방법 (Getting Started: 시작 / Installation: 설치)  
✔ 컴파일 방법, 사용 환경, 브라우저 서포트, 개발스택, 구현 목록(명세)  
✔ 간단한 사용 방법 및 예제:<br>

3. 프로젝트 결과물

✔ 기능별 사진 / 영상:<br>
✔ 코드설명, 후기(짧고 간결하게 써야함, 내용이 길어질 경우 블로그에 작성한뒤 링크로 연결해주는게 좋다)<br>
<span style="color:white; font-weight:400;font-size:18px">
URL Sample Image</span>
<details><summary> <span style="color:#2D57A9;font-weight:400;font-size:15x">☑️[Click : 펼치기 / 접기]</span>
</summary>

![](2023-06-11-01-13-29.png)
</details>
<br>

<span style="color:white; font-weight:400;font-size:18px">
Sample Image의 Map Code</span>
<details><summary> <span style="color:#2D57A9;font-weight:400;font-size:15x">☑️[Click : 펼치기 / 접기]</span>
</summary>
<br>
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


4. Contribute (기여자)

✔ 다른 사람들이 코드에 Contribute하기 쉽도록 방법 설명  
✔ 어떤 류의 Contribute를 원하는지 또는 Contributing 규칙 등을 적을 수도 있다.

5. LICENSE

✔ 라이선스 : 저작물의 수정 배포에 대한 권한이나 저작권들에 대한 조항들  
✔ 보통 MIT License를 많이 사용하고 BSD 라이선스도 많이 사용한다

6. 외부리소스 정보

✔ 프로젝트에 포함된 외부 코드나 리소스 정보(각각의 출처 및 배포 라이선스):  
배포 URL: http://ec2-15-165-74-90.ap-northeast-2.compute.amazonaws.com:9999/  
7. Code Status

✔ Shield라는 것을 사용하여 [build | passing]과 같은 정보를 줄 수 있다.  
✔ 프로젝트가 커질수록 도움이 되는 부분  
<br><br>

## Skills
## Platforms
<img src="https://img.shields.io/badge/windows-0078D6?style=for-the-badge&logo=windows&logoColor=white">
<img src="https://img.shields.io/badge/linux-FCC624?style=for-the-badge&logo=linux&logoColor=black">
<img src="https://img.shields.io/badge/ANACONDA-44A833?style=badge&logo=anaconda&logoColor=white">
<img src="https://img.shields.io/badge/AMAZON-AWS-232F3E?style=badge&logo=amazonaws&logoColor=white">
<img src="https://img.shields.io/badge/GITHUB-181717?style=badge&logo=github&logoColor=white">

##  Languages & Tools & Library
<img src="https://img.shields.io/badge/PYTHON-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/GIT-F05032?style=badge&logo=git&logoColor=white">
<img src="https://img.shields.io/badge/GOOGLE-COLAB-F9AB00?style=badge&logo=googlecolab&logoColor=white">
<img src="https://img.shields.io/badge/STREAMLIT-FF4B4B?style=badge&logo=streamlit&logoColor=white">
<img src="https://img.shields.io/badge/PLOTLY-3F4F75?style=badge&logo=plotly&logoColor=white">
<img src="https://img.shields.io/badge/SEABORN-150458?style=badge&logo=기술스택아이콘&logoColor=white">
<img src="https://img.shields.io/badge/MATPLOTLIB-D70F64?style=badge&logo=기술스택아이콘&logoColor=white">
<img src="https://img.shields.io/badge/PANDAS-E40000?style=badge&logo=기술스택아이콘&logoColor=white">
<img src="https://img.shields.io/badge/PROPHET-FF7300?style=badge&logo=기술스택아이콘&logoColor=white">
<br><br>

- 출처<br>
  1.  사이드바 이미지출처:  
  연작가 : https://www.instagram.com/yeon.writer.1983/
  2.  데이터 출처 :  
  Kaggle : https://www.kaggle.com/
<br><br>


<span style="color:red; font-weight:600;font-size:30px">
Python Error, Debuging
</span>
<details><summary> <span style="color:#2D57A9;font-weight:500;font-size:16px">☑️[Click : 펼치기 / 접기]</span>
</summary>

```python
# Streamilt st.tab 기능 error
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
</details>

---
<br>
<span style="color:red;font-weight:600;font-size:30px">
EC2 가상환경 Font Error</span>  

<span style="color:#000000;font-weight:600;font-size:16px">
(출처: https://luvris2.tistory.com/119)
</span>
<details><summary> <span style="color:#2D57A9;font-weight:500;font-size:16px">☑️[Click : 펼치기 / 접기]</span>
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
