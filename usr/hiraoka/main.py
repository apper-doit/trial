import time
from clsled import cgpio
anos = [11,12,13,14,15]
cathos = [21,22,23,24,25]

char1 = [[ 0 for i in range(8)] for j in range(8)]
char1[0] = [1,1,1,1,1,1,1,1]
#for v in char1:
#	print(v)

try:
	cgpio = cgpio(anos,cathos)
	while True:

		ret = input("???:")
		if ret == "show":
			cgpio.show_box(char1)

		elif ret == "clear":
			cgpio.show_clear()
		else:
			print("unknown:%s" % ret)

		time.sleep(3)

except KeyboardInterrupt:
	print("exit")

