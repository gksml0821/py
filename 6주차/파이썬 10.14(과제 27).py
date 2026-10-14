#문자열 - 연습문제 1 (1)
'''A = input()

for x in A:
    print(x, end=" ")'''
#문자열 - 자가진단 1-1 (2)
'''s = input()

for i in range(0, len(s), 2):
    print(s[i], end=" ")'''
#문자열 - 자가진단 1-2 (3)
'''s = input()

for i in range(len(s) - 1, -1, -1):
    print(s[i], end="")'''
#문자열 - 연습문제 2 (4)
'''print("It's an apple.")
print('He said "Hello!" to me')'''
#문자열 - 자가진단 2 (5)
'''str1 = 'My name is "Hong Gildong"'
str2 = "I'm 15 years old"

print(str1)
print(str2)'''
#문자열 - 연습문제 3 (6)
'''A = "apple orange banana"
B = "   Hello world!   "
words = A.split()
words.reverse()
print(" ".join(words))
print(B)
print(B.strip())'''
#문자열 - 자가진단 3 (7)
'''word1, word2 = input().split()
print(word2, word1 + word2)'''
#문자열 - 연습문제 4 (8)
'''name = input()
age = input()
print(f"{name} is {age} years old.")'''
#문자열 - 자가진단 4 (9)
'''name1, age1 = input().split()
name2, age2 = input().split()

print(f"{name1}'s age - {name2}'s age = {int(age1) - int(age2)}")'''
#문자열 - 연습문제 5 9 (10)
'''
pi = 3.14
r = int(input())
area = r * r * pi

print("PI =", format(pi, ".2f"))
print("Area =", r, "*", r, "*", pi, "=", round(area, 1))'''
#문자열 - 자가진단 5 (11)
'''n = int(input())
result = n / 3

print(f"{result:.2f}")'''
#문자열 - 연습문제 6 (12)
'''print(" ITEM      PRICE")
print(" shoe         75")
print("  bag         230")'''
#문자열 - 자가진단 6 (13)
'''print(" item count price rate")
print(" pen 20 100 50.5")
print(" note 5 95 35.3")
print(" eraser 110 97 14.2")
'''
#문자열 - 연습문제 7 (14)
'''h = int(input())
m = int(input())

print("%02d:%02d" % (h, m))
'''
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
#문자열 - 연습문제 8 (16)
'''
text = input()
result = ",".join(text)

print(result)
'''
#문자열 - 자가진단 8-1 (17)
'''a = input()
b = input()
c = input()

print(a + "-" + b + "-" + c)'''
#문자열 - 자가진단 8-2 (18)
'''year, month, day = input().split()

print(year + "/" + month + "/" + day)'''
#문자열 - 연습문제 9 (19)
'''a, b = input().split()

i = a * 3

if b in i:
    print(a + b)
else:
    print(b * 2)'''
#문자열 - 자가진단 9 (20)
'''a = input()
b = input()

c = b * 5

if a in c:
    print("YES")
else:
    print("NO")''' 
#문자열 - 형성평가 1 (21)
'''t = input()
rev = t[::-1]
result = "-".join(rev)

print(result)'''
#문자열 - 형성평가 2 (22)
'''name = input()

print(name + "'s score 'perfect'")'''
#문자열 - 형성평가 3 (23)
'''w = float(input())
h = float(input())

area = (w * h) / 2

print(f"{area:.1f}")'''
#문자열 - 형성평가 4 (24)
'''
print(f"{'name':>10}{'subject':>10}")
print(f"{'minsoo':>10}{'math':>10}")
print(f"{'chulsoo':>10}{'science':>10}")'''
#문자열 - 형성평가 5 (25)
'''name, height, weight = input().split()

print("NAME:", name)
print("HEIGHT:", height + "cm")
print("WEIGHT: %.2fkg" % float(weight))'''
#문자열 - 형성평가 6 (26)
'''s = input()
print(".".join(s))'''
#문자열 - 형성평가 7 (27)
'''s = input()

print(s[::-1])
print(s)'''
