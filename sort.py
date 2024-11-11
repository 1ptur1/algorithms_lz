from random import randint

N = 100 # N = len(a)
a = []
for i in range(1, N+1):
    a.append(randint(1, 1_000_000))

g=0 #счетчик

for i in range(0, len(a)-1):
    f = False
    for j in range(0,len(a)- 1 - i):
        if a[j] > a[j+1]:
            a[j], a[j+1]=a[j+1], a[j]
            f = True
            print(a) #названия переменных, выход из цикла
        g +=1
    if not f:
        break
print('Счетчик =', g)

N = 100 # N = len(a)
a = [] 
for i in range(N):
    a.append(randint(1, 1_000_000))
g1=0
i=0
while i < N - 1:
    m=i
    j = i 
    while j < N:
        if a[j] < a[m]:
            m = j
        g1 += 1
        j += 1
    a[i], a[m] = a[m], a[i]
    print(a)
    
    i += 1
print(a)
print('кол-во сравнений при сортировке пузырьком =', g)
print('кол-во сравнений при сортировке выбором =', g1)