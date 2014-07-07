
def common_prefix(a,b):
	i = 0
	for i, s in enumerate(a):
		if a[i]!=b[i]:
			break
	else:
		return a
	return a[:i]
