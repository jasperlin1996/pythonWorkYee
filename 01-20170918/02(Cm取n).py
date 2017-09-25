C200 = 1
C100 = 1
C50 = 1
for i in range(100):
	C100 *= (i+1)
for i in range(50):
	C50 *= (i+1)
for i in range(200):
	C200 *= (i+1)
print("C(100,50) = " + str(C100//(C50*C50)))
print("C(200,100) = " + str(C200//(C100*C100)))