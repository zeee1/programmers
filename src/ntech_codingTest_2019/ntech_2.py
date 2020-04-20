def solution(n):
    tmplist = list()

    strN = str(n)

    for i in strN:
    	tmpI = int(i)

    	if tmpI == 0:
    		continue

    	if n%tmpI == 0 and tmpI not in tmplist:
    		tmplist.append(tmpI)

    answer = len(tmplist)

    return answer


print(solution(2232))
print(solution(1234))