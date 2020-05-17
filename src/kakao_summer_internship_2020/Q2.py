def solution(expression):
    answer = 0
    operator_list = list()
    number_list = list()
    number = ""
    for i in range(0, len(expression)):
    	if expression[i] == "*" or expression[i] == "-" or expression[i]== "+":
    		operator_list.append(expression[i])
    		number_list.append(number)
    		number = ""
    	else:
    		number += expression[i]

    	if i==len(expression)-1:
    		number_list.append(number)

    
    case_list = [['*', '-', '+'], ['*', '+','-'], ['-','*',  '+'], ['-','+','*'], ['+', '-', '*'], ['+', '*', '-']]

    for case in case_list:
    	copy_op_list = list()
    	copy_nb_list= list()
    	
    	for o in operator_list:
    		copy_op_list.append(o)
    	for n in number_list:
    		copy_nb_list.append(n)


    	for op in case:
    		if op not in copy_op_list:
    			continue

    		index = 0

    		while index < len(copy_op_list):
    			if copy_op_list[index] == op:
    				value = eval(copy_nb_list[index]+op+copy_nb_list[index+1])
    				copy_nb_list.pop(index+1)
    				copy_nb_list.pop(index)
    				copy_nb_list.insert(index, str(value))
    				copy_op_list.pop(index)
    			else:
    				index += 1
    	tmp_answer= abs(int(copy_nb_list[0]))
    	answer = max(tmp_answer, answer)


    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))