from sys import stdin, setrecursionlimit
setrecursionlimit(100000)

def which_operator(operator, operated1, operated2):
	if operator == "+": return operated1 + operated2
	if operator == "-": return operated1 - operated2
	if operator == "*": return operated1 * operated2
	if operator == "//": 
		if operated1 < 0: 
			return -1 * ((-1 * operated1) // operated2)
		return operated1 // operated2


def calculate(n_idx, available, res):
	if n_idx >= n-1:
		available.append(res)
		return 

	for op_idx in range(4):
		if operator_val[op_idx] > 0:
			operator_val[op_idx] -= 1
			new_res = which_operator(operator_arr[op_idx], res, n_arr[n_idx+1])
			calculate(n_idx+1, available, new_res)
			operator_val[op_idx] += 1

	return available


n = int(stdin.readline().rstrip())
n_arr = list(map(int, stdin.readline().rstrip().split(" ")))
operator_arr = ["+", "-", "*", "//"]
operator_val = list(map(int, stdin.readline().rstrip().split(" ")))

available = calculate(0, [], n_arr[0])

print(max(available))
print(min(available))


