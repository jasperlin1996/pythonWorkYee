from decimal import Decimal as dec

def calcualte():
	m = dec(input('本金: '))
	r = dec(input('利率: '))
	y = dec(input('存幾年: '))
	print("和: {}".format(m*(1+r)**y))

if __name__ == '__main__':
	calcualte()