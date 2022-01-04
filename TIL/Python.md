나는 파이썬 개발자이면서도 파이썬이라는 언어에 대해 지나치게 <b>무지</b> 했었던 것 같다.<br>
그래서 파이썬에 대해 정리하며 조금 친해지기 위한 노력을 해보려고 하는데 오늘은 파이썬의 특징에 대해 정리해보고자 한다.
다들 파이썬스러운 개발자(pythonic developer)가 되기위해 공부해보자.

## 파이썬의 디자인 철학
```가장 아름다운 하나의 답이 존재한다.``` <br>
위 문구는 파이썬의 기본 모토이다. 위 특징 때문인지 파이썬은 다른 언어와는 다르게 특정 기준(<b>PEP8</b>)에 부합하게 수렴진화 하는 성향이 있다. 
다른언어에서는 중괄호의 위치 및 표기 방법등에 대해 격렬하게 싸우지만 파이썬은 최대한 문법 구조를 단순화, 통일 시키는데에 초점을 맞추고 이때 아래 리스트들의 기준을 따라가다 
보니 다른 언어들처럼 개발자들의 취향에 따라 발산 진화하지 않는 것이다.

아래는 PEP20에서 제시된 파이썬 기본 철학 리스트이다.

1. 아름다운 것이 추한 것보다 낫다. (Beautiful is better than ugly.)
2. 명시적인 것이 암시적인 것보다 낫다. (Explicit is better than implicit.)
3. 간결한 것이 복합적인 것보다 낫다. (Simple is better than complex.)
4. 복합적인 것이 복잡한 것보다 낫다. (Complex is better than complicated.)
5. 수평적인 것이 내포된 것보다 낫다. (Flat is better than nested.)
6. 여유로운 것이 밀집한 것보다 낫다. (Sparse is better than dense.)
7. 가독성은 중요하다. (Readability counts.)
8. 특별한 경우들은 규칙을 어길정도로 특별하지 않다. (Special cases aren't special enough to break the rules.)
9. 허나 실용성은 순수성을 이긴다. (Although practicality beats purity.)
10. 오류는 절대로 조용히 지나가지 않는다. (Errors should never pass silently.)
11. 명시적으로 오류를 감추려는 의도가 아니라면. (Unless explicitly silenced.)
12. 모호함을 대할때, 이를 추측하려는 유혹을 거부하라. (In the face of ambiguity, refuse the temptation to guess.)
13. 명확한, 그리고 가급적이면 유일한 하나의 방법은 항상 존재한다. (There should be one-- and preferably only one --obvious way to do it.)
14. 비록 그 방법이 처음에는 명확해 보이지 않을지라도[10]. (Although that way may not be obvious at first unless you're Dutch.)
15. 지금 행동에 옮기는 것이 아예 안하는 것보다는 낫다. (Now is better than never.)
16. 비록 아예 안하는 것이 지금 *당장* 하는 것보다 나을때도 많지만. (Although never is often better than *right* now.)
17. 구현 결과를 설명하기 쉽지 않다면, 그것은 나쁜 아이디어이다. (If the implementation is hard to explain, it's a bad idea.)
18. 구현 결과를 설명하기 쉽다면, 그것은 좋은 아이디어일지도 모른다. (If the implementation is easy to explain, it may be a good idea.)
19. 네임스페이스를 사용하는 것은 완전 좋은 생각이다! (Namespaces are one honking great idea -- let's do more of those!)

## 권장 코드 스타일 규격
파이썬은 위 철학과 같은 이유로 문법을 굉장히 엄격하게 단속한다. 이는 파이참을 쓸때 뜨는 노란줄 만 봐도 알것이다..! 단어 사이 언더바는 물론 한줄의 최대 길이까지 정해져있다!
<br>이런 문법을 자세히 정리해두고 권장해둔 것이 파이썬 공식문서에 있는데 이것이 바로 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 이다


