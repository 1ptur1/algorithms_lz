from random import randint

"""N = int(input("Введите кол-во элементов ")) # N = len(a)
a = []
while len(a)<N: # цикл для присваивания значений эл-там 
    a.append(randint(1, 1000000))
    a=list(dict.fromkeys(a))
print(a)
m=0

b = int(input())
for i in range(0,N):
    if a[i] == b:
        m = i
if m!=0:
    print('Номер эл-та =',m + 1)
    print("Кол-во операций =", m + 1)
else:
    print('Такого элемента нет в списке')"""



N = int(input("Введите кол-во элементов ")) # N = len(a)
a = []
while len(a)<N: # цикл для присваивания значений эл-там 
    a.append(randint(1, 100))
print(a)
g1=0 # счетчик
i=0
while i < N - 1: # цикл для проверки по всей длинне исключая предыдущий элемент+
    m=i # присвоение минимального значения
    j = i # поиск следующего минимального через переменную j
    while j < N: # поиск через проверку каждого элемента
        if a[j] < a[m]: # условие
            m = j # присвоение пременно m значения новго минимального элемента
        g1 += 1 # счетчик
        j += 1 # переход к следуещему элементу
    a[i], a[m] = a[m], a[i] # обмен значений
    print(a)
    
    i += 1
print(a)
search_value = int(input("Введите искомое число "))
low = 0
high = len(a) - 1
mid = len(a) // 2
while a[mid] != search_value and low <= high:
    if search_value > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print('Нет такого элемента')
else:
    print('Индекс искомого элемента равен ', mid)