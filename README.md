# 협업필터링기반 맥주 추천 시스템
![main](https://user-images.githubusercontent.com/78454586/130912924-88866c38-c1f0-4f9c-a240-b27bd49c0dd1.JPG)

<div align="center"> <h1>BEER CRAFT</h1> </div>

[LIKELION & K-DIGITAL] Team1의 파이널 프로젝트 - 협업 필터링 기반 맥주 추천 시스템

<br>

#### 🛠 환경
- python3.8
- vscode
- 그 외 라이브리러 requirements.txt 참고


#### 🎨 화면 구성
- 워드클라우드로 보는 '맥주' 트렌드 키워드
<img width="1439" alt="스크린샷 2021-08-13 오후 4 01 41" src="https://user-images.githubusercontent.com/50325009/129317700-e8dc9b1e-13b5-473b-9b8a-47a49b80d99d.png">

- 다양한 추천 시스템
<img width="1440" alt="스크린샷 2021-08-13 오후 4 13 12" src="https://user-images.githubusercontent.com/50325009/129318996-e1e01f4c-c59f-4e2d-ab0a-1053a8cc1707.png">

- 국산 수제 맥주 리뷰
<img width="1440" alt="스크린샷 2021-08-13 오후 4 12 17" src="https://user-images.githubusercontent.com/50325009/129318896-abe1b04a-6765-46f6-ab68-709b74dafbfb.png">


<br>

#### 💻 상세 기능 안내
- 모든 기능은 로그인 후 사용 가능
- 사용자 평점을 값으로 맥주간 코사인 유사도 기반, 가장 선호하는 맥주와 중요하게 생각하는 요인을 고려하여 맥주 추천
- 맥주경험이 없는 사용자를 위한 추천 시스템, 평가 요인의 순위를 정해 이에 가중치를 부여하여 가장 평균 평점이 높은 맥주 추천
- 나의 과거 경험(맥주에 대한 평점)을 반영하여 새로운 맥주에 대한 평점 계산, 가장 높은 평점을 받을 것으로 예상되는 맥주 추천
- Pytorch & CNN & 전이학습 이용한 맥주 이미지 라벨링(현재 5개의 맥주 구별 가능)
- 국내 수제 맥주 상세 페이지에서 리뷰 및 댓글 작성

#### 📌 진행 과정 및 코드 안내
- 블로그 포스팅 https://juran-devblog.tistory.com/127?category=871212
- 깃허브 https://github.com/ijo0r98/likelion-kdigital/tree/main/final-project

#### 👯‍♂️ 팀원
- 임주란 https://github.com/ijo0r98/
- 이용석 https://blog.naver.com/flowermisty
- 박건우 https://cottonwood-moa.tistory.com/
- 강원석 https://github.com/kang1seok
- 주리아 https://github.com/Riah0987
