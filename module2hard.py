import random
number = random.randint(3,21)
result = ''
print('result for', number,':')
for i in range(1,number):
    for j in range(i +1, number + 1):
        if number % (i + j) == 0:
            result += (str(i) + str(j))
print(result)



