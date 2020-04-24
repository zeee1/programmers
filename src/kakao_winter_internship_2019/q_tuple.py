def solution(s):
    answer = []

    s = s[1:len(s)-1]
    splited = s.split("},")

    s_list = list()
    for i in splited:
    	tmp_list = list()
    	i = i[1:]

    	split_by_comma = i.split(",")

    	for c in split_by_comma:
    		if "}" in c:
    			c = c[:len(c)-1]
    		tmp_list.append(int(c))
    	s_list.append(tmp_list)

    
    s_list.sort(key = len)

    for i in range(0, len(s_list)):
    	if i == 0:
    		answer += s_list[i]
    		continue

    	diff = list(set(s_list[i])-set(s_list[i-1]))[0]
    	answer.append(diff)



    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))