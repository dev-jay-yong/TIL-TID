### 링크드 리스트 (Linked List)

링크드 리스트 (Linked List) 구조 특징
- 연결 리스트라고도 함
- 배열은 순차적으로 연결된 공간에 데이터를 나열하는 데이터 구조
- 링크드 리스트는 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조
- 본래 C언어에서는 주요한 데이터 구조이지만, 파이썬은 리스트 타입이 링크드 리스트의 기능을 모두 지원함


- 링크드 리스트 기본 구조와 용어
    - 노드(Node): 데이터 저장 단위 (데이터 값, 포인터)로 구성
    - 포인터(pointer): 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간

![image](https://user-images.githubusercontent.com/96015600/200331578-e01aeeb0-7589-43f5-b680-d80ae974de1b.png)
<br>(출처 - [wikipedia](https://ko.wikipedia.org/wiki/%EC%97%B0%EA%B2%B0_%EB%A6%AC%EC%8A%A4%ED%8A%B8))


### 링크드 리스트 예시
Node 구현
- 보통 파이썬에서 링크드 리스트 구현시, 파이썬 클래스 활용

```python
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
def add(node, data):
    while node.next:
        node = node.next
    node.next = data


first_node = Node(1)
second_node = Node(2)
third_node = Node(3)
print(first_node.data) # 1
add(first_node, second_node)
print(first_node.next.data) # 2
add(first_node, third_node)
print(first_node.next.next.data) # 3

while first_node.next:
    print(first_node.data)
    first_node = first_node.next
print(first_node.data)

```


