char_dict = {"(":1, "[":3, "{":2}

def solution(input):
    answer = True

    char_list = list()

    for i in input:
    	if i == "[" or i == "(" or i == "{" or i == "}" or i == "]" or i == ")":
    		char_list.append(i)

    answer = check(char_list)

    return answer

def check(prior_list):
	answer = True

	stack_list = list()

	for i in range(0, len(prior_list)):
		if prior_list[i] == "(" or prior_list[i] == "{" or prior_list[i] == "[":
			if len(stack_list) == 0:
				stack_list.append(prior_list[i])
			else:
				peek_value = stack_list[-1:][0]
				peek_value = char_dict[peek_value]
				input_value = char_dict[prior_list[i]]

				if peek_value <= input_value:
					answer = False
					break
				else:
					stack_list.append(prior_list[i])
		else:
			if len(stack_list) > 0:
				popped_value = stack_list.pop()

				if prior_list[i] == "}" and popped_value != "{":
					answer = False
					break
				if prior_list[i] == ")" and popped_value != "(":
					answer = False
					break
				if prior_list[i] == "]" and popped_value != "[":
					answer = False
					break
			else:
				answer = False
				break
		if i == len(prior_list)-1 and len(stack_list)>0:
			answer = False

	return answer

print(solution("3+[(5+1)-1]"))
print(solution("3+([5+1])"))
print(solution("3+{(5+1}"))
print(solution("3+[{(5+1)-1}+3]"))