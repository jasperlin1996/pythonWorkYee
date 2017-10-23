import sys

def mergesort(split_list):
	if len(split_list) > 1:
		left = mergesort(split_list[0:len(split_list)//2])
		right = mergesort(split_list[len(split_list)//2:])
		left.append(sys.maxsize)
		right.append(sys.maxsize)
		mergelist = []
		i = j = 0
		for k in range(len(left)+len(right)-2):
			if left[i] > right[j]:
				mergelist.append(right[j])
				j += 1
			else:
				mergelist.append(left[i])
				i += 1
		print(mergelist)
		return mergelist
	print(split_list)
	return split_list

print(mergesort([int(x) for x in input().split()]))