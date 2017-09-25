import sys

num_list = list()
for line in sys.stdin:
	num_list.append(int(line))
odd_sum = 0
even_sum = 0
for num in num_list:
	if num % 2 == 1:
		odd_sum += num
	else:
		even_sum += num
print("odd_sum:{}\neven_sum:{}".format(odd_sum,even_sum))
