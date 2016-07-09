x = [1,1]

m1 = [1,2]
m2 = [2,1]
m3 = [2,-1]
m4 = [1,-2]
m5 = [-1,-2]
m6 = [-2,-1]
m7 = [-2,1]
m8 = [-1,2]

moves = [m1, m2, m3, m4, m5, m6, m7, m8]

def find_end_pos(start, move):
	end_pos = []
	end_pos.append(start[0]+move[0])
	end_pos.append(start[1]+move[1])
	return end_pos

def find_legal_moves(start, moves):
	legal_moves = []
	
	for m in moves:
		end_pos = find_end_pos(start, m)
		if end_pos[0]>=1 and end_pos[0]<=8 and end_pos[1]>=1 and end_pos[1]<=8:
			legal_moves.append(end_pos)
		else:
			continue

	return legal_moves

paths = []

terminate = False

while terminate = False:

	


print(find_legal_moves(x, moves))

print(find_legal_moves([4,4], moves))