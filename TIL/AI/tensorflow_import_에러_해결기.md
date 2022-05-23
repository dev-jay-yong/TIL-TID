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

~~우선 오늘은 서울에서 광주까지 내려오는데 체력을 너무 많이 썻으므로 이 문제는 내일의 용은재에게 맡기는걸로.. (1월 28일)~~

그렇다.. 오늘의 용은재(1월 30일)도 결국 해결하지 못했다.

우선 나와 동일한 이슈로 [apple/tensorflow](https://github.com/apple/tensorflow_macos/issues/270) 에 이슈를 남긴 것과 답변을 참고해서 수정을 해보았다.
1. version이 아닌 __version__ 호출하기 => 이미 그렇게 하고 있었으나 실패하였다.
2. [m1용 tensorflow를 설치하여 사용해보기](https://www.youtube.com/watch?v=6W8pjnW65Q8)

동영상에 나온데로 m1용 tensorflow를 설치한 결과 아래와 같이 import 에러가 발생한다. ~~다른 사람들은 저렇게 해결한거같은데 왜 나만 ㅠㅠ~~
```bash
/Users/yong-eunjae/Desktop/TimeseriesProject/venv/bin/python /Users/yong-eunjae/Desktop/TimeseriesProject/study/test0001.py
Traceback (most recent call last):
  File "/Users/yong-eunjae/Desktop/TimeseriesProject/venv/lib/python3.8/site-packages/tensorflow/python/pywrap_tensorflow.py", line 64, in <module>
    from tensorflow.python._pywrap_tensorflow_internal import *
ImportError: dlopen(/Users/yong-eunjae/Desktop/TimeseriesProject/venv/lib/python3.8/site-packages/tensorflow/python/_pywrap_tensorflow_internal.so, 6): no suitable image found.  Did find:
	/Users/yong-eunjae/Desktop/TimeseriesProject/venv/lib/python3.8/site-packages/tensorflow/python/_pywrap_tensorflow_internal.so: mach-o, but wrong architecture
	/Users/yong-eunjae/Desktop/TimeseriesProject/venv/lib/python3.8/site-packages/tensorflow/python/_pywrap_tensorflow_internal.so: mach-o, but wrong architecture

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/yong-eunjae/Desktop/TimeseriesProject/study/test0001.py", line 1, in <module>
    import tensorflow as tf
  File "/Users/yong-eunjae/Desktop/TimeseriesProject/venv/lib/python3.8/site-packages/tensorflow/__init__.py", line 41, in <module>
    from tensorflow.python.tools import module_util as _module_util
  File "/Users/yong-eunjae/Desktop/TimeseriesProject/venv/lib/python3.8/site-packages/tensorflow/python/__init__.py", line 39, in <module>
    from tensorflow.python import pywrap_tensorflow as _pywrap_tensorflow
  File "/Users/yong-eunjae/Desktop/TimeseriesProject/venv/lib/python3.8/site-packages/tensorflow/python/pywrap_tensorflow.py", line 83, in <module>
    raise ImportError(msg)
ImportError: Traceback (most recent call last):
  File "/Users/yong-eunjae/Desktop/TimeseriesProject/venv/lib/python3.8/site-packages/tensorflow/python/pywrap_tensorflow.py", line 64, in <module>
    from tensorflow.python._pywrap_tensorflow_internal import *
ImportError: dlopen(/Users/yong-eunjae/Desktop/TimeseriesProject/venv/lib/python3.8/site-packages/tensorflow/python/_pywrap_tensorflow_internal.so, 6): no suitable image found.  Did find:
	/Users/yong-eunjae/Desktop/TimeseriesProject/venv/lib/python3.8/site-packages/tensorflow/python/_pywrap_tensorflow_internal.so: mach-o, but wrong architecture
	/Users/yong-eunjae/Desktop/TimeseriesProject/venv/lib/python3.8/site-packages/tensorflow/python/_pywrap_tensorflow_internal.so: mach-o, but wrong architecture


Failed to load the native TensorFlow runtime.

See https://www.tensorflow.org/install/errors

for some common reasons and solutions.  Include the entire stack trace
above this error message when asking for help.

Process finished with exit code 1
```
이쯤되면 그냥 설날 끝나고 서울에 올라가서 데스크탑으로 마저 공부하는게 맞는 거 같지만.. 여기서 포기하기엔 내 자존심이 허락해주지 않기때문에 어떻게든 다시 방법을 찾아서 해결 할 것이다.
~~2일차 해결 일지 끝~~

---
#### 3일차 도전... 그리고 엔딩
3일차만에 드디어 성공을 했다. 우선 mac으로는 conda 없이 안될거 같아 결국 conda를 깔았다.. 그리고 아래의 동작들을 순서대로 수행해보았다.

---
* **install Xcode**
  * 앱스토어에서 Xcode를 다운받는다.
* **Miniforge3-MacOSX-arm64.sh 파일을 다운받는다**
  * 다운받는 곳 : [https://github.com/conda-forge/miniforge](https://github.com/conda-forge/miniforge)
* **Create Env (가상환경을 만들어준다.)**
  * conda create -n tensorflow_env python==3.9 -y
  * conda activate tensorflow_env
* **Install Tensorflow**
  * conda install -c apple tensorflow-deps
  * pip install tensorflow-macos
  * pip install tensorflow-metal

---
간단한 위 4개의 동작을 모두 수행한다면 놀랍게도 m1 mac에서도 tensorflow 호출이 매우 잘된다! ~~이걸 몰라서 그동안 허비한 시간이..~~
그래도 우여곡절끝에 해결해서 뿌듯하고 빨리 tensorflow 공부를 하고 싶다는 동기부여를 가진체 글을 마무리 해본다.


출처1 - [tensorflow git](https://github.com/tensorflow/tensorflow/issues/46628) <br>
출처2 - [ashcode](https://hashcode.co.kr/questions/12647/m1-%EB%A7%A5%EB%B6%81-%ED%8C%8C%EC%9D%B4%EC%B0%B8%EC%97%90-python-tensorflow%EC%84%A4%EC%B9%98-%EB%B2%84%EC%A0%84-%EB%AC%B8%EC%9D%98) <br>
출처3 - [CPUU님 개발블로그](https://cpuu.postype.com/post/9091007/) <br>
출처4 - [apple/tensorflow에 올라온 나와 동일 해보이는 이슈](https://github.com/apple/tensorflow_macos/issues/270) <br>
출처5 - [m1용 tensorflow 설치 하는 법](https://www.youtube.com/watch?v=6W8pjnW65Q8) <br>
출처6 - [멈춤보단 천천히라도님 기술블로그](https://webnautes.tistory.com/1639) <br>
출처7 - [v.esc님 기술블로그](https://velog.io/@esc/Mac-M1-Monterey-Tensorflow) <br>
