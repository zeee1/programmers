def solution(s):
	answer = 0
	answer_list = []

	i = 1

	while i <= len(s):
		tmp_answer = ""
		prev_cutted_str = ""
		repeated_num = 1

		for j in range(0, len(s), i):
			cutted_str = s[j:j+i]
			next_index = j+i

			if cutted_str == prev_cutted_str:
				repeated_num += 1
			elif prev_cutted_str != "":
				if repeated_num != 1:
					tmp_answer += str(repeated_num)
				tmp_answer += prev_cutted_str
				repeated_num = 1

			
			if next_index >= len(s):
				if repeated_num != 1:
					tmp_answer += str(repeated_num)
				tmp_answer += cutted_str
				break

			prev_cutted_str = cutted_str

		answer_list.append(len(tmp_answer))

		i += 1

	return min(answer_list)

print(solution("aabbaccc"))

print(solution("ababcdcdababcdcd"))

print(solution("abcabcdede"))

print(solution("a"))
print(solution("abcabcabcabcdededededede"))

print(solution("xababcdcdababcdcd"))
