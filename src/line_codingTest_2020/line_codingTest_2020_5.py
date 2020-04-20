def solution(dataSource, tags):
    answer = []

    doc_tag_map = {}

    for d in dataSource:
    	for t in tags:
    		if t in d:
    			if d[0] in doc_tag_map.keys():
    				doc_tag_map[d[0]] += 1
    			else:
    				doc_tag_map[d[0]] = 1

    values_list = list(set(doc_tag_map.values()))
    values_list.reverse()

    for i in range(0,len(values_list)):
    	targetNumber = values_list[i]

    	key_list = list()

    	for j in doc_tag_map.keys():
    		if doc_tag_map[j] == targetNumber:
    			key_list.append(j)
    	key_list.sort()
    	answer += key_list

    return answer

print(solution([
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"]
], ["t100"]))