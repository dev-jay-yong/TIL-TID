명절이되어 본가에 내려와 오랜만에 mac으로 시계열 인공지능 모델 공부를 해보려고 하던 찰나에 문제가 발생했다..
<br> 단순히 import 후 버전을 출력하는 아래 코드가 실행하자마자 꺼져버리는 것이다..! 확인해보니 tensorflow를 import하는 부분의 문제 인 거 같아 구글링해보니 <b>m1 에서의 문제라고 한다</b> ~~하아... 역시 m1으로 바꾼뒤에 셋팅 프로세스가 평균적으로 한개 이상 더 늘었다.~~
```python
import tensorflow as tf
import keras

print("hi")
print(f"tensorflow : {tf.__version__}")
print(f"keras : {keras.__version__}")

# 실행 결과 : Process finished with exit code 132 (interrupted by signal 4: SIGILL)
```


귀찮았지만 우선 이게 되야 시작을 하기에(+ 재발 방지) 찾아본 결과를 기록해두고자 한다.

#### 파이썬 설치
당연한걸 왜 설명하느냐 라고 묻는다면 tensorflow가 지원하는 python 버전이 생각보다 까다롭기 때문이다.
tensorflow는 3.6과 3.9 버전을 지원하지 않는다. 그렇기 때문에 이 글에서는 3.8 버전의 파이썬을 통해 모든 코드를 구현하였다. ~~필자는 멍청해서 파이썬을 총 세번 깔았다..~~

#### tensor flow 설치
``` bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/apple/tensorflow_macos/master/scripts/download_and_install.sh)"
```
위 명령어를 실행 한 후 최종적으로 설치하고자 하는 가상환경 경로까지 적어준다면 아주 간단하게 tensorflow를 설치 할 수 있다.
하지만 이 방법의 치명적인 문제가 있으니 <b>머신 러닝에 필요한 필수적인 다른 패키지들인 scikit-learn, pandas, matplotlib, JupyterLab등을 별도로 설치해주어야 한다! </b>~~그냥 Conda로 깔자..~~

참고로 아래 라이브러리들은 같이 설치가 되니 참고 바란다.
```
numpy-1.18.5, grpcio-1.33.2, h5py-2.10.0, scipy-1.5.4
``` 

분명.. stack overflow 와 매우 똑똑해보이시는 개발자분은 이렇게해서 성공을 했는데...
나는 왜인지 <b>실패</b>했다 ㅠㅠㅠㅠ

~~우선 오늘은 서울에서 광주까지 내려오는데 체력을 너무 많이 썻으므로 이 문제는 내일의 용은재에게 맡기는걸로..~~

출처1 - [tensorflow git](https://github.com/tensorflow/tensorflow/issues/46628) <br>
출처2 - [ashcode](https://hashcode.co.kr/questions/12647/m1-%EB%A7%A5%EB%B6%81-%ED%8C%8C%EC%9D%B4%EC%B0%B8%EC%97%90-python-tensorflow%EC%84%A4%EC%B9%98-%EB%B2%84%EC%A0%84-%EB%AC%B8%EC%9D%98) <br>
출처3 - [CPUU님 개발블로그](https://cpuu.postype.com/post/9091007/) <br>
