from itertools import permutations

def solution(n, k):
    answer = 0

    loc_list = []

    for i in range(0, n):
    	for j in range(0, n):
    		loc_list.append(str(i)+"_"+str(j)+" ")

    total_case = list(map(''.join, permutations(loc_list, k)))
    
    drop_duplitcated = drop_duplitcased(total_case, k)
    for i in drop_duplitcated:
    	if is_vaild(i) == True
    		answer+= 1
    return answer

def drop_duplitcased(total_case, k):
	drop_duplitcased_case = list()
	for case in total_case:
		splited_case = case.split()

		case_list = list()

		for i in range(0, k):
			loc = splited_case[i].split("_")
			tmp_list = []

			for j in range(0, 2):
				tmp_list.append(int(loc[j]))

			case_list.append(tmp_list)

		case_list = sorted(case_list)

		if case_list not in drop_duplitcased_case:
			drop_duplitcased_case.append(case_list)

	return drop_duplitcased_case

def is_vaild(case, k):
	for i in range(0, k):
		i_loc = case[i]

		for j in range(i, k):
			j_loc = case[j]

			if i_loc[0] == j_loc[0]:
				return False
			elif i_loc[1] == j_loc[1]:
				return False
	return True


print(solution(2,2))
#print(solution(3,2))