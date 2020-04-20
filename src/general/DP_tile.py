def solution(N):
	answer_list = [2, 4]

	for i in range(2, N+1):
		answer_list.append(answer_list[i-1]+answer_list[i-2])
	return answer_list[N]

print(solution(5))
print(solution(6))