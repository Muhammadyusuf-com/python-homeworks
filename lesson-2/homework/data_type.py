# 1
a = float(input())
a = round(a, 2)
# 2
d, b, c = map(int, input().split())
print(max(d, b, c))
print(min(d, b, c))
# 3
km = 10
m = km * 1000
cm = m * 100
# 4
n1,n2 = map(int,input().split())
print(n1//n2)
print(n1%n2)
# 5
celcius = 18
farenheit = (celcius * 9 / 5) + 32
# 6
n = input()
print(n[-1])
# 7
n = input()
if n % 2:
    print("The number is odd")
else:
    print("The number is even")
