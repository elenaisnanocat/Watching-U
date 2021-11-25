# Watching U

> Django + Vanilla.js

#### :punch: ​팀원

* 윤혜윤 (팀장)
  * ERD 모델링
  * 기본 및 추가 기능 구현
  * API 활용 (TMDB, youtube)
  * 크롤링 (naver movie)
  * Wordcloud
  * PPT 및 영상 제작
* 박유정 (팀원)
  * 기본 기능 구현
  * 홈 페이지 디테일 구현
  * 홈 페이지 구상
  * 일정 관리
  * 시연 및 발표 촬영
  * 서비스 배포

#### :punch: ​계획 및 일정

![image-20211125174819607](C:\Users\HOME\Desktop\관통\restart-project-code\README.assets\image-20211125174819607.png)

#### :punch: PJT 목표 및 실제 구현 개요

* 영화 정보 제공 (관리자 권한)
* 커뮤니티 (user 리뷰, 댓글 CRUD)
* 추천 알고리즘 
* 회원가입, 로그인, 로그아웃
* 리뷰 좋아요
* 영화 보고싶어요, 별점
* 검색 (영화 제목, 감독 필터)
* 워드클라우드
* 별점 분포 그래프
* 총 영화 감상 시간 
* 예고편
* Oauth (google, github)
* 반응형 웹

#### :punch: ERD

![image-20211125215043074](C:\Users\HOME\Desktop\관통\restart-project-code\README.assets\image-20211125215043074.png)

#### :punch: ​프로젝트 기능 및 구현

> Home

![image-20211125215342978](C:\Users\HOME\Desktop\관통\restart-project-code\README.assets\image-20211125215342978.png)

![image-20211125215351360](C:\Users\HOME\Desktop\관통\restart-project-code\README.assets\image-20211125215351360.png)

![image-20211125215400303](C:\Users\HOME\Desktop\관통\restart-project-code\README.assets\image-20211125215400303.png)

![image-20211125215405937](C:\Users\HOME\Desktop\관통\restart-project-code\README.assets\image-20211125215405937.png)

![image-20211125215414776](C:\Users\HOME\Desktop\관통\restart-project-code\README.assets\image-20211125215414776.png)

![image-20211125215421533](C:\Users\HOME\Desktop\관통\restart-project-code\README.assets\image-20211125215421533.png)

* 영화 제목 및 감독 이름 검색 및 결과
* 전체 영화 목록 (TMDB API)
* 보고싶어요 버튼
* User들의 평균 평점 계산
* 영화 예고편 (Youtube API)
* User 리뷰 목록

> Community

![image-20211125215544190](C:\Users\HOME\Desktop\관통\restart-project-code\README.assets\image-20211125215544190.png)

![image-20211125215549565](C:\Users\HOME\Desktop\관통\restart-project-code\README.assets\image-20211125215549565.png)

* 전체 유저들의 영화 평가 리뷰 
* 리뷰 좋아요 버튼
* 마우스 오버 시 해당 영화의 키워드들을 한 눈에 파악할 수 있는 워드클라우드
* 리뷰 상세 페이지와 댓글

> My page

![image-20211125215657950](C:\Users\HOME\Desktop\관통\restart-project-code\README.assets\image-20211125215657950.png)

![image-20211125215704133](C:\Users\HOME\Desktop\관통\restart-project-code\README.assets\image-20211125215704133.png)

![image-20211125215725788](C:\Users\HOME\Desktop\관통\restart-project-code\README.assets\image-20211125215725788.png)

* 프로필 수정 (프로필 사진 및 상태메시지)

* 팔로우 기능

* 리뷰, 팔로우, 팔로잉 수

* 평가한 영화의 총 runtime

![image-20211125215757681](C:\Users\HOME\Desktop\관통\restart-project-code\README.assets\image-20211125215757681.png)

![image-20211125215803778](C:\Users\HOME\Desktop\관통\restart-project-code\README.assets\image-20211125215803778.png)

* 평가 리뷰글, 댓글, 좋아한 리뷰 목록

* User가 평가한 별점 분포

* User가 보고싶어요를 누른 영화 목록 

> Recommend

![image-20211125215837164](C:\Users\HOME\Desktop\관통\restart-project-code\README.assets\image-20211125215837164.png)

![image-20211125215843565](C:\Users\HOME\Desktop\관통\restart-project-code\README.assets\image-20211125215843565.png)

![image-20211125215848495](C:\Users\HOME\Desktop\관통\restart-project-code\README.assets\image-20211125215848495.png)

1. 모든 User들이 보고싶어요를 많이 누른 영화 순

(모든 유저)

2. User가 가장 높은 별점을 준 영화의 장르들 중 랜덤으로 뽑은 장르의 영화 목록

(평가를 했을 시)

3. User의 팔로우들이 가장 높은 별점을 준 영화 목록

(팔로우를 했을 시)
