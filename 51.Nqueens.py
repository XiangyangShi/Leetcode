def conflict(state,nextX):
	nextY = len(state)
	for i in range(nextY):
		if abs(state[i]-nextX) in (0,nextY-i):
			return True
	return False

def queens(num=8,state=()):
	for position in range(num):
		if not conflict(state,position):
			if len(state)==num-1:
				yield (position,)
			else:
				for result in queens(num,state+(position,)):
					yield (position,)+result

return queens()
