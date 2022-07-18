password = list(map(int, input().split()))
last = 0

for i in password:
    last += i * i

last %= 10
print(last)
