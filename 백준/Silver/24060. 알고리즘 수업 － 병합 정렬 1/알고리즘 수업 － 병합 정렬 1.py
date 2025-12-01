from sys import stdin

def merge_sort(a, p, r):
	if p < r:
		q = (p+r)//2
		merge_sort(a, p, q)
		merge_sort(a, q+1, r)
		merge(a, p, q, r)
	

def merge(a, p, q, r):
	global cnt, k, result

	i, j, t = p, q+1, 0
	tmp = [0 for i in range(r-p+1)]

	while (i <= q and j <= r):
		if a[i] <= a[j]:
			tmp[t] = a[i]
			t+=1
			i+=1
		else: 
			tmp[t] = a[j]
			t+=1
			j+=1

		cnt += 1
		if cnt == k: result = tmp[t-1]

	while(i<=q): 
		tmp[t] = a[i]
		t+=1
		i+=1
		cnt += 1
		if cnt == k: result = tmp[t-1]

	while(j<=r): 
		tmp[t] = a[j]
		t+=1
		j+=1
		cnt += 1
		if cnt == k: result = tmp[t-1]

	for idx in range(r - p + 1):
		a[p + idx] = tmp[idx]
	

n, k = map(int, stdin.readline().rstrip().split(" "))
a = list(map(int, stdin.readline().rstrip().split(" ")))
cnt, result = 0, -1

merge_sort(a, 0, n-1)
print(result)