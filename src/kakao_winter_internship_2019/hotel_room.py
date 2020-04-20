def solution(k, room_number):
    answer = []

    check = {}

    for r in room_number:
    	

    	if r in check.keys():
    		parent = check[r]
    		path_list = list()
    		path_list.append(r)
    		
    		while True:
    			if parent in check.keys():
    				path_list.append(parent)
    				parent = check[parent]
    			else:
    				check[parent] = parent+1
    				answer.append(parent)
    				break

    		for p in path_list:
    			check[p] = parent+1

    	else:
    		check[r] = r+1
    		answer.append(r)

    return answer
    	

print(solution(10, [1,3,4,1,3,1]))