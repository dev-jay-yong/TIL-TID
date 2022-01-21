def solution(progresses, speeds):

    count = 0
    answer = []

    while progresses:
        for index, value in enumerate(progresses):
            progresses[index] += speeds[index]
            if progresses[index] >= 100:
                count += 1
                del progresses[index]
                del speeds[index]
                if index == 0:
                    answer.append(count)
                    count = 0
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

# 아직 미완성 => 세번째 작업 완료 후 첫번째 작업 완료 되면 2번째 작업이 완료되지 않았음에도 카운팅 됨
