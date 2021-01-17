import math
import random

time = 0
hour = 0
sec = 0
i = 1

while hour == 0:
	nextTime = -math.log(random.random()) * 3
	nextTime = int(nextTime * 60)
	time = time + nextTime
	sec = str(time % 60)
	minute = str((time / 60) % 60)
	hour = (time / 60) / 60
	if hour == 0:
		ans = str(i)+" -> 00:"+minute.zfill(2)+':'+sec.zfill(2)
		print ans
		#print i,'-> 00:',minute.zfill(2),':',sec.zfill(2)
	i = i + 1

#print time