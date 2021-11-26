n = int(input())
num = 1
print(" ")
while n >= num:
    if num % 3 == 0 or num % 10 == 3 or "3" in str(num):
        print(num,end=" ")
    num+=1