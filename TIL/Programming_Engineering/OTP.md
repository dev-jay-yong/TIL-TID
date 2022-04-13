### OTP 인증 구현하기

네이버나 금융어플을 쓰다보면 2차인증으로 OTP인증을 할 수 있는경우들이 있다. 오늘은 이 OTP 인증에 대해서 알아본 뒤 구현해보자.

### OTP (One-time Password)
OTP란 무작위 번호약속 알고리즘에 따라 매 시간마다 변경되는 추정 할 수 없는 비밀번호 생성을 이용하는 보안시스템이다.
아이디어 자체는 100년이 넘었어도 현재까지 사용될 정도로 검증되어 있는 기술이다. 주로 다중 인증 체계의 인증 요소 중 하나로 사용된다.
네이버, 구글, 블리자드등이 2차 인증으로 OTP를 사용하고 있다. ~~귀찮다~~

OTP 발생기를 발급하여 사용하는 하드웨어 OTP도 존재하지만 본 글에서는 소프트웨어로만 구성되어 있는 모바일 OTP만 취급하도록 하겠다.

### 모바일 OTP
모바일 OTP는 외부와 완전히 독립적인 장치인 OTP 토큰과 달리 휴대폰이나 PC에 OTP 프로그램 (google OTP 등)을 설치하여 번호를
생성하는 방식을 이용한다.

대한민국에서 모바일 OTP 토큰이 보안계의 무적과 같은 위력을 가져온다는 사실이 퍼지게되어 본격적으로 도입된 이후부터 대부분의 온라인 프로그램(넥슨 게임, 네이버 및 금융사 등)
들의 로그인 메뉴에서 OTP 로그인 서비스를 찾아볼 수 있으며 금융사에서도 도입되어 대부분의 금융기관에서도 지원하고 있다.

금융권 밖에서는 구글의 OTP 앱이 잘 알려져 있으며, RFC 6238이라는 TOTP 공개 표준을 사용하기 때문에 호환되는 타사 생성기(Authy나 마이크로 소프트 인증기 등)도 존재한다.
이때 구글 인증기가 아닌 앱을 쓸 경우 조심해야 하는데, 신뢰성 있는 앱이 아닌 이상 절대 깔아서 쓰면 안된다.

하지만 OTP만으로 보안 문제가 해결되지는 않는데, 소프트웨어적인 OTP는 독립된 하드웨어 토큰에 비해 시드가 외부로 유출되기 대단히 쉽기 때문에 보안상 매우 취약하게 된다.
따라서 금융 거래시 PC 및 휴대폰용 모바일 OTP 프로그램은 사용하지 않으며 사이트 로그인 시 2단계 인증을 주로 사용하게 된다.

스마트폰 OTP 프로그램의 경우에는 운영체제 업데이트만 잘 해주면 시드가 해킹 당할 위험이 매우 적다. 안드로이드 계열은 iOS에 비해 약간 더 신경을 써야 하지만, 크게 걱정할 수준은 아니며 관리만 잘 해주면 안전한 편이다.
PC 운영체제의 경우 스마트폰 보다 권한 관리가 느슨하기 때문에 OTP 프로그램의 시드를 읽어내어 해킹하는 등의 위험이 존재한다. 즉 본인의 컴퓨터를 평소 잘 관리해놓아야 한다. 마지막으로 비밀번호를 맞게 쳤음에도 접속이 안 되는 단점도 존재한다.

아래는 모바일 OTP의 간단한 장단점 정리이다.
* 장점 : 물리적 매체가 필요없어 매우 편리하며 이는 모바일 금융 시대에 매우 적합하다. 발급비용이 거의 무료이며 사용기간이 사실상 반영구적이다. 모방이로도 발급이 가능하여 영업점 방문이 필요없다.
* 단점 : 물리적 매체에 비해 보안성이 다소 취약하여 해킹 등의 위험이 존재한다. 각 금융사마다 자사의 모바일 OTP를 가지고 있어 서로 호환되지 않거나, 
  공용 모바일 OTP의 경우 아직까지는 일부 금융사들만 지원하고 있어 호환성 문제가 혈되지 않았다. 휴대전화가 고장나거나 초기화될 경우 OTP 정보가 지워질 수 있다.
  

### 구글 OTP(RC 6238) 직접 사용해보기
지겨운 OTP의 이론적 설명이 드디어 끝났다!
그럼 바로 실습으로 넘어와 python과 pyotp, qrcode 두 라이브러리를 활용하여 구현해보겠다.

```python
import pyotp
import qrcode

key = pyotp.random_base32()
totp = pyotp.TOTP(key)
```
우선 ```pyotp.random_base32()```를 통해 랜덤으로 seed를 생성해준다. 이때 key의 값은 <b>절대로</b> 타인에게 공유되어서는 안된다.
구글이나 마이크로 소프트와 같은 OTP 앱은 위와같이 생성된 16자리 seed를 기반으로 한다. 하지만 16진수 기반의 인코딩 기법으로 생성하여 사용하는 경우도 존재하는데
이때는```pyotp.random_hex()```를 사용하여 생성해주면 된다. 이후 우리는 시간 기반인 TOTP(RC 6238) 방식을 사용할 것이기 때문에 TOTP 메소드를 사용하여 seed를 넘겨주어
otp 클래스를 생성하게 된다.

```python
url = totp.provisioning_uri(name='jayyong.dev@gmail.com', issuer_name='Jay')

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
img.save('qrcode.png')
```
이후 위 코드와 같이 생성된 otp 클래스로 otp를 등록할 수 있는 url을 발급 받은 후 qr 코드로 만들면 구글OTP 어플을 활용하여 바로 등록이 가능하다.
이때 처음 발급받은 seed key를 직접 입력해서도 가능하므로 참고바란다.

OTP 발급부터 QR코드 변환까지를 전부하면 아래와 같다.
```python
import pyotp
import qrcode

key = pyotp.random_base32()
totp = pyotp.TOTP(key)

url = totp.provisioning_uri(name='jayyong.dev@gmail.com', issuer_name='Jay')

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
img.save('qrcode.png')
```
위와 같이 간단한 방식으로 OTP 서비스를 사용해 볼 수 있으니 참고해서 본인의 개인프로젝트나 서비스에 도입해보자!
