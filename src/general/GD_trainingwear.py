def solution(n, lost, reserve):
    answer = 0

    set_lost = set(lost)-set(reserve)
    set_reserve = set(reserve)-set(lost)

    answer = n - len(set_lost)

    for student in set_lost:
    	if student-1 in set_reserve:
    		answer +=1
    		set_reserve.remove(student-1)
    		continue

    	elif student+1 in set_reserve:
    		answer +=1
    		set_reserve.remove(student+1)
    		continue

    return answer

print(solution(5, [1,2], [1,3,5]))
print(solution(5, [1,2,3,4,5], [1]))
print(solution(5,[3,4,5],[3,4,5]))