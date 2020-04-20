def solution(p):
	answer = ""

	if len(p) == 0:
		return ""

	if is_correct(p) == True:
		return p

	splited_str = split_to_balanced_str(p)
	u = splited_str[0]
	v = splited_str[1]

	if is_correct(u):
		answer = u + solution(v)

	else:
		answer += "("
		answer += solution(v)
		answer += ")"

		u = u[1:len(u)-1]
		for i in range(0, len(u)):
			if u[i] == "(":
				answer += ")"
			else:
				answer += "("

	return answer
	

def is_balanced(p):
	count_dict = {"(":0, ")":0}

	for i in range(0, len(p)):
		if p[i] == "(":
			count_dict["("] += 1
		elif p[i] == ")":
			count_dict[")"] += 1

	if count_dict["("] == count_dict[")"]:
		return True

	return False

def split_to_balanced_str(p):
	if len(p) <= 2:
		return (p, "")

	for i in range(2, len(p)+1, 2):
		u = p[0:i]
		v = p[i:len(p)]

		if is_balanced(u) == True and is_balanced(v) == True:
			return (u, v)



def is_correct(p):
	stack_list = list()

	for i in range(0, len(p)):
		i_char = p[i]

		if i_char == "(":
			stack_list.append(i_char)

		if i_char == ")":
			if len(stack_list) > 0:
				stack_list.pop()
			else:
				return False

	if len(stack_list) > 0:
		return False
	return True

"""
print(solution("(()())()"))
print(solution(")("))

print(solution("()))((()"))
"""
print(solution("((()))()((())()))(()))(("))