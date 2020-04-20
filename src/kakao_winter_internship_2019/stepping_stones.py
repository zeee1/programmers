def solution(stones, k):
    left = 1
    right = 200000001 

    while left <= right:
    	mid = int((left+right)/2)

    	if isPossible(stones, k, mid):
    		left = mid+1
    	else:
    		right = mid-1

    return left

def isPossible(stones, k, mid):
	count = 0
	for i in range(0, len(stones)):
		if stones[i] -mid <= 0:
			count += 1

			if count == k:
				return False
		else:
			count = 0

	return True




print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))