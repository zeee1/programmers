def solution(monster, S1, S2, S3):
    answer = -1

    sorted(monster)

    sum_list = list()
    list_count = 0
    for i in range(1, S1+1):
    	for j in range(1, S2+1):
    		for k in range(1, S3+1):
    			sum_list.append(i+j+k)
    			list_count += 1

    avoidance = 0
    for move in sum_list:
    	player_loc = 1+move

    	if player_loc not in monster:
    		avoidance+= 1

    answer = int((avoidance/list_count)*1000)
    return answer

print(solution([4,9,5,8], 2,3,4))
print(solution([4,9,5,8], 2,3,3))