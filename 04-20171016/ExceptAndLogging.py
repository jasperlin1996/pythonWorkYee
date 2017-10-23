import logging
logging.basicConfig(filename="ExceptAndLogging.log", level=logging.ERROR)
try:
	with open('ch6ex1.txt','r') as f:
		for i in f:
			line = i.split(',')
			if len(line) != 4:
				logging.error("Invalid syntax: ")
			for j in line:

except (FileNotFoundError):
	print("QQ file no found")