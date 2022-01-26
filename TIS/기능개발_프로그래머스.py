def solution(progresses, speeds):

    count = 0
    answer = []

    while progresses: # progress 리스트 요소가 있는동안 계속 돔
        for index, value in enumerate(progresses):
            progresses[index] += speeds[index] # progress 진행
            
        if progresses[0] >= 100: # 첫번째 progress가 100을 넘었을때
            del progresses[0]
            del speeds[0]

            count += 1
            for temp in progresses: # 이후 progress 중 100넘은게 있는지 체크
                if progresses[0] < 100:
                    break
                else:
                    progresses.pop(0)
                    speeds.pop(0)
                    count += 1
        if count > 0: # progress가 진행된경우마다 count ++
            answer.append(count)
            count = 0
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]	))

# 어떤 이유에서인지 테스트에서 몇개가 실패함 이유 찾아야함 생각보다 어려운 문제엿음...
