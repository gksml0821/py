#문자열 - 자가진단 7 (15)
'''h, m = map(int, input().split())

if h >= 12:
if h > 12:
h = h - 12
if h == 0:
h = 12
ampm = "PM"
else:
if h == 0:
h = 12
ampm = "AM"

if h < 10:
hs = "0" + str(h)
else:
hs = str(h)

if m < 10:
ms = "0" + str(m)
else:
ms = str(m)

print(hs + " : " + ms + " " + ampm)
'''
