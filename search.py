from random import randint

N = 10 # N = len(a)
a = []
while len(a)!=N: # цикл для присваивания значений эл-там 
    a.append(randint(1, 10))
    a=list(dict.fromkeys(a))
print(a)
m=0
b = int(input())
for i in range(0,N):
    if a[i] == b:
        m = i
if m!=0:
    print('Индекс искомого элемента =',i)
else:
    print('Такого элемента нет в списке')