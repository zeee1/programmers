def solution(snapshots, transactions):
    answer = list()

    t_log_map = {}
    account_map = {}
    for a in snapshots:
    	account_map[a[0]] = int(a[1])

    for t in transactions:
    	if t[0] in t_log_map.keys():
    		continue
    	t_log_map[t[0]] = True
    	
    	function = t[1]
    	account = t[2]
    	price = int(t[3])

    	if function == "SAVE":
    		if account in account_map.keys():
    			account_map[account] += price
    		else:
    			account_map[account] = price

    	if function == "WITHDRAW":
    		if account in account_map.keys():
    			account_map[account] -= price
    		
    sortmap = sorted(account_map.items())
    for i in range(0, len(sortmap)):
    	answer.append([sortmap[i][0], str(sortmap[i][1])])
    
    return answer

print(solution([["ACCOUNT1", "100"], ["ACCOUNT2", "150"]], [["1", "SAVE", "ACCOUNT2", "100"],["2", "WITHDRAW", "ACCOUNT1", "50"],["1", "SAVE", "ACCOUNT2", "100"],["4", "SAVE", "ACCOUNT3", "500"],["3", "WITHDRAW", "ACCOUNT2", "30"]]))