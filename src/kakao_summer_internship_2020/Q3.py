def solution(gems):
    answer = []
    unique_items = list(set(gems))
    item_maps = {}
    min_count = 100000

    for i in range(0, len(gems)):
    	i_list = list()
    	i_list.append(gems[i])
    	count = 1

    	for j in range(i, len(gems)):
    		
    		if gems[j] not in i_list:
    			i_list.append(gems[j])

    		if len(i_list) == len(unique_items):
    			if min_count > count:
    				min_count = count
    				answer = [i, j]
    			break

    		count += 1

    		

    answer[0] += 1
    answer[1] += 1

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))