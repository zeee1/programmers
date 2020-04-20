import re

def solution(words, queries):
	answer = list()
	reg = "[a-z]+"
	p = re.compile(reg)
	words = list(set(words))

	for query in queries:
		count = 0

		fixed_word = p.findall(query)
		if len(fixed_word) > 0:
			fixed_word = fixed_word[0]
		else:
			fixed_word = ""

		wildcard_length = len(query) - len(fixed_word)

		if query.startswith(fixed_word):
			reg_ex = fixed_word+"[a-z]{"+str(wildcard_length)+"}"
		else:
			reg_ex = "[a-z]{"+str(wildcard_length)+"}"+fixed_word

		p2 = re.compile(reg_ex)

		for word in words:
			if p2.match(word) is not None and len(word) == len(query):
				count += 1
				 	
		answer.append(count)

	return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["??????","????o", "fr???", "fro???", "pro?"]))