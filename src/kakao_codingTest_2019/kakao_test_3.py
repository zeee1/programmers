def solution(key, lock):
	test = check(key, lock)
	if test[0] == True:
		return True

	if test[1] == 0:
		return False

	moved_key = movekey(key, "up")
	return solution(key, lock)
	moved_key = movekey(key, "down")
	return solution(key, lock)
	moved_key = movekey(key, "right")
	return solution(key, lock)
	moved_key = movekey(key, "left")
	return solution(key, lock)
	moved_key = rotatekey(key, "left")
	print(moved_key)
	return solution(key, lock)
	moved_key = rotatekey(key, "right")
	print(moved_key)
	return solution(key, lock)


	return False

def check(key, lock):
	blocked_lock_pos = []
	blocked_key_pos = []

	for i in range(0, len(lock)):
		for j in range(0, len(lock[i])):
			if lock[i][j] == 0:
				blocked_lock_pos.append((i, j))

	for i in range(0, len(key)):
		for j in range(0, len(key[i])):
			if key[i][j] == 1:
				blocked_key_pos.append((i, j))
	
	for i in range(0, len(lock)-len(key)+1):
		tmp_key_pos = list()
		for j in range(0, len(blocked_key_pos)):
			tmp_key_pos.append((blocked_key_pos[j][0]+i, blocked_key_pos[j][1]+i))

		if tmp_key_pos == blocked_lock_pos:
			return (True, len(tmp_key_pos))
	return (False, len(tmp_key_pos))

def movekey(key, direction):
	len_key = len(key)
	null_row = [0 for i in range(0, len_key)]

	if direction == "up":
		key = key[1:]
		key.append(null_row)
	if direction == "down":
		key = key[0:len_key-1]
		key.insert(0, null_row)
	if direction == "left":
		for i in range(0, len_key):
			key[i] = key[i][1:len_key]
			key[i].append(0)
	if direction == "right":
		for i in range(0, len_key):
			key[i] = key[i][0:len_key-1]
			key[i].insert(0, 0)

	return key

def rotatekey(key, direction):
	len_key = len(key)
	blocked_key_pos = list()
	moved_key_pos = list()


	if direction == "left":
		for i in range(0, len_key):
			for j in range(0, len_key):
				key[i][j] = key[j][len_key-1-i] 

	if direction == "right":
		for i in range(0, len_key):
			for j in range(0, len_key):
				key[len_key-1-i][j]=key[i][j] 

	return key

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
