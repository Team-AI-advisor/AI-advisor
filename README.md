![image](https://github.com/Team-AI-advisor/AI-advisor/assets/124342239/877805bb-c567-4cf0-a49e-8baaa4174f03)

<br/>
사용자들의 더 나은 의사결정을 위한 친절한 데이터 분석 도구
<br/><br/><br/>

## 프로젝트 소개
빅데이터 분석 및 인공지능 기술의 발달 속도와 그에 적응하는 대중의 속도 간 차이는 점점 벌어지고 있습니다. <br/><br/>
IT 분야에 관심이 크거나 직업인이 아닌 이상 해당 기술을 일상 속에서 활용하기에는 아직까지 인식적인 진입장벽이 높습니다. <br/><br/>
AI-advisor는 사람들이 기술 발달의 호혜를 편히 누릴 수 있도록 프로그램이자 플랫폼 서비스입니다.<br/><br/>
전문적인 데이터 과학자나 분석가의 도움 없이도 자신의 데이터에 대한 통찰력을 얻을 수 있는 서비스 제공해줍니다.

<br/><br/>

## 프로젝트 주요기능 
1)	자동 데이터 분석 및 시각화
2)	데이터 분석 및 시각화 결과를 통한 인사이트 제안
3)	대화형 시각화 도구

<br/><br/>

## 시스템 아키텍처
![arc](https://github.com/Team-AI-advisor/AI-advisor/assets/90888774/2abb8b4e-2a8b-4dea-97f5-95a72ab3d948)

<br/><br/>

## 실행 방법
1. python version: 3.9.17<br/>
2. pip install -r requirements.txt<br/>
3. api.yaml에 api key 입력<br/>
4. streamlit run app.py<br/>
<br/>

## 🛠 Tools
구분|내용
---|---
프로그래밍 언어|	Python
데이터 분석 및 시각화 라이브러리|	Pandas, numpy, matplotlib, seaborn, scipy
AI 라이브러리|	OpenAI, PandasAI
웹 앱 패키지|	streamlit
기타|	Git, GitHub, VSCode, Chrome, Windows 10

<br/><br/>


## 서비스 구성 및 기능

## 1단계

<br/>
사용자가 CSV 파일을 업로드합니다.<br/><br/>

### ▼ 사진으로 확인하기

---

![image](https://github.com/Team-AI-advisor/AI-advisor/assets/124342239/874262aa-8724-4b61-9f96-20686bdea5ce)

<br/>

## 2단계

<br/>
데이터셋 개요를 설명하는 통계치가 출력됩니다. 
또한 출력된 통계치는 문장으로 바뀌어 chatGPT API를 통해 Advice가 도출됩니다. <br/><br/>

### ▼ 사진으로 확인하기

---

![image](https://github.com/Team-AI-advisor/AI-advisor/assets/124342239/6164983e-9619-4fac-b6b8-71793a2ffe0a)


<br/>

## 3단계

<br/>

각 변수 별로 변수 분포를 설명하는 통계치와 그에 해당하는 그래프가 출력됩니다. <br/>
이 때 통계치는 자동으로 범주형 혹은 수치형으로 구분됩니다. <br/>
또한 출력된 통계치는 문장으로 바뀌어 chatGPT API를 통해 Advice가 도출됩니다.<br/><br/>

### ▼ 사진으로 확인하기

---

![image](https://github.com/Team-AI-advisor/AI-advisor/assets/124342239/89e67c25-b09c-46e8-a874-87ecaa171173) <br/>
![image](https://github.com/Team-AI-advisor/AI-advisor/assets/124342239/2d899d1b-c3f1-4c59-870c-ca6288a7ef18) <br/>
![image](https://github.com/Team-AI-advisor/AI-advisor/assets/124342239/108c7054-4aee-4a30-bf2a-74ebde7dacbd) <br/>


<br/><br/>

## 4단계

<br/>

상관관계를 보여주는 히트맵 그래프가 출력됩니다.
상관관계에서 유의미한  변수 쌍과 상관관계 강도는 문장으로 바뀌어  chatGPT API를 통해 Advice가 도출됩니다.<br/><br/>

### ▼ 사진으로 확인하기

---

![image](https://github.com/Team-AI-advisor/AI-advisor/assets/124342239/8ae005cf-2295-4d77-8297-80b9f69a3164)


<br/><br/><br/>

## 5단계

<br/>
시각화 도구 단계입니다. <br/>
사용자가 생성하고 싶은 차트에 대한 설명을 입력하면 Pandas AI가 맞춤형 그래프와 그에 대한 설명을 도출합니다. <br/>
이후 chatGPT API를 통해 해당 그래프를 기반으로 Advice가 도출됩니다.

### ▼ 사진으로 확인하기

---

![image](https://github.com/Team-AI-advisor/AI-advisor/assets/124342239/cc2ae787-cebf-4290-994b-5b8058603a92) <br/><br/>
![image](https://github.com/Team-AI-advisor/AI-advisor/assets/124342239/c2473663-b650-4db0-83ba-1caae7bbeaf2)


<br/><br/>
#### ※ 모든 단계의 Advice는 개발자가 미리 지정한 프롬프트를 기반으로 출력됩니다. 

<br/><br/>

---

## 🎲 pre-commit
1. pip install pre-commit<br>
2. git clone 진행한 directory로 이동<br>
3. pre-commit install<br>
4. 코드 정상 실행된 경우 git add, commit, push 진행

<br/><br/>

## 📜 Commit Type
- feat : 새로운 기능 추가, 기존의 기능을 요구 사항에 맞추어 수정
- fix : 기능에 대한 버그 수정
- build : 빌드 관련 수정
- chore : 패키지 매니저 수정, 그 외 기타 수정 ex) .gitignore
- ci : CI 관련 설정 수정
- docs : 문서(주석) 수정
- style : 코드 스타일, 포맷팅에 대한 수정
- refactor : 기능의 변화가 아닌 코드 리팩터링 ex) 변수 이름 변경
- test : 테스트 코드 추가/수정
- release : 버전 릴리즈
