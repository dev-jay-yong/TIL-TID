# Feature Engineering
작년 면접 질문 중 "Feature Engineering에 대해서 설명해주실 수 있으신가요?"라는 질문을 받았었다.
아무래도 AI 회사에서 백엔드 엔지니어로 있다보니 받았던 질문이었던거 같다. 이때 명확하게 대답을 못하고 
"학습 성능을 높이기 위해 새로운 Feature를 만들거나 변형하는 과정입니다" 라고 대답했었다. 틀린 답변은 아니었지만 너무 추상적으로 답변을
했었던 거 같아 나중에 꼭 다시 찾아서 공부해야지 라고 생각하던 것을 이번에 공부하게 되었다.

---

## Garbage in, garbage out
위 문구는 Feature Engineering을 잘 표현한 문장이다. 쓰레기 데이터를 사용하게 될 경우 학습된 모델이 뱉어내는 결과물(예측값)또한 쓰레기라는 것이다.
즉 데이터 분석 및 데이터 정제가 매우 중요하다는 것을 나타내며 Feature Engineering은 데이터 분석 시 많은 지분을 차지한다.

![머신러닝 개발 시간](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FmiIy7%2FbtqTcRcaYiB%2Fe5nsYv7tJBGKnzMtVGVvi0%2Fimg.jpg)
위 그래프를 한 번 확인해보자. 머신러닝을 개발 할 때 사용되는 시간을 평균적으로 계산하여 표현해준 원형 그래프이다. 
놀랍게도 모델링의 시간보다 훨씬 많은 비중을 차지하는 데이터 전처리 및 준비 작업인 것을 확인 할 수 있다.
그렇다면 이때 사용하는 Feature Engineering이란 무엇일지 알아보자.

## Feature Engineering 정의

