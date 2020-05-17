def solution(food_times, k):
    answer = 0
    
    sort_food_times = food_times
    sort_food_times.sort()
    index_map = {}

    while len(food_times) > 0:
    	popped = food_times.pop()

    	index_map[len(food_times)] = popped

    

    return answer

#print(solution([3,1,2], 5))
#print(solution([100], 5))
print(solution([3,2,1,1,3], 7))