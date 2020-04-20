def solution(a, b, budget):
    answer = 0

    if budget%a ==0:
    	answer += 1

    if budget%b == 0:
    	answer += 1

    budget -= a
    
    while True:
    	if budget < b:
    		break

    	if budget%b == 0:
    		answer+=1

    	budget -= a

    return answer

print(solution(3000, 5000, 23000))