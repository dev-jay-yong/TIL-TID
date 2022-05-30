## Tensorflow protobuf 버전 에러 해결
열심히 tensorflow 에러를 고쳤더니 2022년 05월 29일자 기준 아래와 같은 에러가 발생했다.. ㅠㅠ
```shell
TypeError: Descriptors cannot not be created directly.
If this call came from a _pb2.py file, your generated code is out of date and must be regenerated with protoc >= 3.19.0.
If you cannot immediately regenerate your protos, some other possible workarounds are:
 1. Downgrade the protobuf package to 3.20.x or lower.
 2. Set PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python (but this will use pure-Python parsing and will be much slower).

More information: https://developers.google.com/protocol-buffers/docs/news/2022-05-06#python-updates
```

이게 갑자기 무슨 날벼락인가 싶어 가상환경을 다시 셋팅하거나 tensorflow 관련 라이브러리를 다시 지웟다 깔아봤는데도 동일한 현상이 지속되었다.
하지만 에러문구를 자세히 봐보니 <b>"1. Downgrade the protobuf package to 3.20.x or lower."</b> 문구가 보였고 설마하고 다시 버전을 낮춰서 깔아보니 해결이 되었다!

갑자기 4점대 버전으로 업그레이드 된게 문제인듯 하다. 아래 명령어를 실행하면 정상적으로 tensorflow 실행이 가능하다. 

```shell
pip uninstall protobuf
pip install protobuf==3.20.1
```

---
### 오늘의 교훈 - 에러문구를 잘 보자
