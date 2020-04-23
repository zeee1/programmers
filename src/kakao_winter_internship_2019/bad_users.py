import re
import sys

def solution(user_id, banned_id):
	answer = 0
	check = list()
	for bid in banned_id:
		tmplist = list()

		for uid in user_id:
			if compareCheck(uid, bid):
				tmplist.append(uid)
		check.append(tmplist)

	print(check)
	print(len(check))
	answer = combination(check, set())

	return answer

def compareCheck(uid, bid):
	if len(uid) != len(bid):
		return False

	for i in range(0, len(uid)):
		if bid[i] == "*":
			continue
		else:
			if uid[i] != bid[i]:
				return False

	return True

def combination(check_list, candidate_set):
	print("candidate_set : ", candidate_set)
	print("depth : ", len(candidate_set))
	answer = 0
	depth = len(candidate_set)
	copy_set = candidate_set

	if depth == len(check_list):
		print("hi")
		return 1

	index_list = check_list[depth]
	for i in range(0, len(index_list)):
		if index_list[i] in candidate_set:
			continue
		copy_set.add(index_list[i])
		answer += combination(check_list, copy_set)
		copy_set = candidate_set
	return answer





print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
#print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
#print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))