def solution(board, moves):
    answer = 0

    stack = list()
    N = len(board)
    stack_top = -1

    for m in moves:
    	# compute target doll
    	# change target doll to 0
    	for i in range(0, N):
    		if board[i][m-1] != 0:
    			if board[i][m-1] == stack_top:
    				stack.pop()

    				if len(stack) == 0:
    					stack_top = -1
    				else:
    					stack_top = stack[-1:][0]
    				answer += 2
    			else:
    				stack.append(board[i][m-1])
    				stack_top = board[i][m-1]
    			
    			board[i][m-1] = 0
    			break
    	
    	# input target doll to stack
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))