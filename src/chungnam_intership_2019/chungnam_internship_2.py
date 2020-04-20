
def solution(N):
	answer = []

	alist = ["("]*N
	blist = [")"]*N

	answer_list = list()  
	solve([], alist, blist, N, answer_list)

	for answer_l in answer_list:
		answer_str = ""
		for c in answer_l:
			answer_str += c
		answer.append(answer_str)

	return answer

def solve(prior_list, alist, blist, N, answer_list):
	if len(prior_list) == 2*N:
		if check(prior_list) == True:
			answer_list.append(prior_list)
			return

	if len(alist) > 0:
		apop = alist.pop()
		solve(prior_list+[apop], alist, blist, N, answer_list)
		alist.append(apop)

	if len(blist) > 0:
		bpop = blist.pop()
		solve(prior_list+[bpop], alist, blist, N, answer_list)
		blist.append(bpop)

def check(prior_list):
	answer = True

	stack_list = list()

	for i in range(0, len(prior_list)):
		if prior_list[i] == "(":
			stack_list.append(prior_list[i])
		else:
			if len(stack_list) > 0:
				stack_list.pop()
			else:
				answer = False
				break
		if i == len(prior_list)-1 and len(stack_list)>0:
			answer = False

	return answer

#print(check(["(", "(", ")", ")"]))
#print(check([")", ")", "(", "("]))
print(solution(2))
print(solution(3))