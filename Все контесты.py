#Все контесты

#Контест 1

#A Сумма двух чисел (0/10)
x = input()
for i in range(len(x)):
    if x[i] == ' ':
        z = int(x[0:i])
        y = int(x[i + 1:len(x)])
print(z + y)

#B Больше или меньше? (0/10)
x = int(input())
y = input()
z = int(input())
if y == '<':
    if (x < z):
        print('YES')
    else:
        print('NO')
else:
    if (x > z):
        print('YES')
    else:
        print('NO')

#C Определение типа треугольника (3/10)
a = int(input())
b = int(input())
c = int(input())

if (a >= b + c) or (b >= a + c) or (c >= b + a):
    print('impossible')
elif (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == b**2 + a**2):
    print('right')
elif (a**2 > b**2 + c**2) or (b**2 > a**2 + c**2) or (c**2 > b**2 + a**2):
    print('obtuse')
else:
    print('acute')

#D Сумма чисел (0/10)
x = int(input())
s = 0.0
while x > 0:
    a = float(input())
    s += a
    x -= 1
print(round(s, 4))

#E Размен животными (1/10)
x = int(input())
y = input()
if y == 'parrot':
    if (x // 10) > 0:
        print(x // 10)
    else:
        print(1)
elif y == 'monkey':
    if (x // 90) > 0:
        print(x // 90)
    else:
        print(1)
elif y == 'elephant':
    if (x // 300) > 0:
        print(x // 300)
    else:
        print(1)

#Контест 2

#A Високосный год (0/10)
n = int(input())
if n % 4 == 0 and not n % 100 == 0 or n % 400 == 0:
    print('YES')
else:
    print('NO')

#B Сумма чисел трехзначного числа (0/10)
x = input()
print(int(x[0]) + int(x[1]) + int(x[2]))

#C Сумма введенной последовательности (0/10)
s = []
s.append(int(input()))
summa = 0
while s[len(s) - 1] != 0:
    s.append(int(input()))
for i in range(len(s)):
    summa += s[i]
print(summa)

#D Длина последовательности (0/10)
s = []
s.append(int(input()))
summa = 0
while s[len(s) - 1] != 0:
    s.append(int(input()))
print(len(s) - 1)

#E Максимум последовательности (0/10)
s = []
s.append(int(input()))
while s[len(s) - 1] != 0:
    s.append(int(input()))
print(max(s))

#F Точная степень двойки (1/10)
N = int(input())
copy = N
while copy % 2 == 0:
    copy = copy // 2
if N == 2 or N == 4 or N == 8 or N == 16 or N == 32 or N == 64 or N == 128 or N == 256 or N == 512 or N == 1024 or N == 2048 or N == 5096 or N == 1:
    print('YES')
else:
    print('NO')

#G Кол-во элементов, равных максимуму (0/10)
s = []
s.append(int(input()))
while s[len(s) - 1] != 0:
    s.append(int(input()))
print(s.count(max(s)))

#H Сумма чисел, следующих за нечетным (1/10)
s = []
a = []
s.append(int(input()))
summa = 0
while s[len(s) - 1] != 0:
    s.append(int(input()))
for i in range(1, len(s)):
    if s[i - 1] % 2 == 1:
        a.append(s[i])
for i in range(len(a)):
    summa += a[i]
if len(s) < 2:
    print(-1)
elif len(a) == 0:
    print(-1)
else:
    print(summa)

#Контест 3

#A Произведение чисел в строке
x = input()
umn = 1
if len(x) == 1:
    povt = 0
else:
    povt = 1
for i in range(len(x)):
    if x[i].isdigit() and (not x[i - 1].isdigit()
                           or i == 0) and not (i + povt) > len(x) - 1:
        while x[i + povt].isdigit():
            povt += 1
            if (i + povt > len(x) - 1):
                break
        umn = umn * int(x[i:i + povt])
    povt = 1
if x[len(x) - 1].isdigit() and not x[len(x) - 2].isdigit():
    umn = umn * int(x[len(x) - 1])
print(umn)

#B Статистика потока пациентов (1/10)
n = int(input())
x = []
temp = 0.0
count = 0
for i in range(n):
    x += input().split()

for i in range(0, len(x), 4):
    if int(x[i]) >= 60 or (int(x[i + 1]) - int(x[i + 2])
                           > 110) or (int(x[i + 1]) - int(x[i + 2]) < 90):
        temp += float(x[i + 3])
        count += 1
if count == 0:
    print(0)
else:
    print(round((temp / count), 5))

#C Разложение числа по степеням (1/10)
n = int(input())


def zifra(t, x):
    t = str(t)
    return t[len(t) - 1 - x]


s = ''
for i in range(len(str(n)) - 1, -1, -1):
    s += (str(zifra(n, i) + '*10^' + str(i) + ' + '))
s = s[:len(s) - 3]
print(s)


#D НЕГА-ПОЗИЦИОННАЯ Система счисления (1/10)
def zifra(t, x):
    t = str(t)
    return int(t[len(t) - 1 - x])


n = int(input())
s = 0
for i in range(len(str(n)) - 1, -1, -1):
    s += zifra(n, i) * ((-10)**i)
print(s)

#E Система счисления МАЙЯ (1/10)
x = input().split()
povt = 0
for i in range(len(x)):
    x[i] = (x[i].count('.') + x[i].count('|') * 5 +
            x[i].count('@') * 0) * (20**(len(x) - 1 - i))
print(sum(x))

#F ВАВИЛОНСКАЯ Система счисления (2/10)
x = input().split('.')
povt = 1
for i in range(len(x)):
    if x[i] == '':
        x[i] = 0
    if x[i] != 0:
        x[i] = (x[i].count('<') * 10 + x[i].count('v')) * (60**(len(x) - povt))
    povt += 1
print(sum(x))

#G ВАВИЛОНСКАЯ Система счисления(обратно) (4/10)
n = int(input())
ans = str("")
flag = int(0)
n_max = 1
while flag == 0:
    #print(60 ** n_max)
    if 60**n_max > n:
        flag = 1
        n_max -= 1
    else:
        n_max += 1
#print(n_max)
while n_max != -1:
    a = n // (60**n_max)
    #print(a)
    x = a // 10
    y = (a % 10)
    for i in range(0, x, 1):
        ans += "<"
    for i in range(0, y, 1):
        ans += "v"
    n = n - (n // (60**n_max)) * (60**n_max)
    #print(n)
    n_max -= 1
    if n_max != -1:
        ans += "."

print(ans)

#Контест 4

#A Поиск НОД чисел по Алгориму Евклида (2/10)
x = int(input())
y = int(input())
while x != y:
    if x > y:
        x = x - y
    elif y > x:
        y = y - x
print(x)


#B Тест простоты числа (1/10)
def is_prime(x):
    d = 2
    while d != x:
        if x % d == 0:
            return 0
        elif x % d != 0 and d == x - 1:
            return 1
        elif x % d != 0:
            d += 1


#C Факторизация числа(разложение на простые множители) (2/10)
x = int(input())
s = []
d = 2
while x != 1:
    if x % d == 0:
        s.append(d)
        x = x // d
        d = 2
    elif x % d > 0:
        d += 1
for i in range(len(s)):
    print(s[i])


#D Генерация n-го простого числа (2/10)
def is_prime(x):
    d = 2
    while d != x:
        if x % d == 0:
            return False
        elif x % d != 0 and d == x - 1:
            return True
        elif x % d != 0:
            d += 1


x = int(input())
povtor = 0
copy = 2
while povtor != x:
    if povtor == x - 1 and is_prime(copy):
        povtor += 1
    elif is_prime(copy) or copy == 2:
        povtor += 1
        copy += 1
    else:
        copy += 1
print(copy)

#E Представление числа в виде суммы двух кубов (3/10)
x = int(input())
s = []
for i in range(round(float(x)**(1 / 3)) + 1):
    if len(s) != 0:
        break
    for j in range(round(float(x)**(1 / 3)) + 1):
        if len(s) != 0:
            break
        elif x == i**3 + j**3 and len(s) == 0:
            s.append(i), s.append(j)
            for k in range(len(s)):
                print(s[k], end=' ')
if x != 1 and len(s) == 0:
    print('impossible')
elif x == 1:
    print(0, 1)

#F Число нулей факториала числа (2/10)
x = int(input())
s5 = []
umn = 1
for i in range(4, x, 5):
    s5.append(i + 1)
x = 0
for i in range(len(s5)):
    umn = 2 * umn * s5[i]
umn = str(umn)
while umn[len(umn) - 1] == '0':
    x += 1
    umn = umn[:-1]
print(x)

#G Минимальное число, для которого заданы: 1) сумма цифр, 2) количество цифр, 3) цифры должны быть упорядочены по неубыванию (1/10)
z = input().split()
x = int(z[0])
y = int(z[1])
s = [1]
if x > y * 9 or x < y:
    print('impossible')
else:
    for i in range(y - 1):
        s.append(1)
    for i in range(len(s) - 1, 0, -1):
        if sum(s) == x:
            break
        else:
            while s[i] != 9:
                s[i] = s[i] + 1
                if sum(s) == x:
                    break
    for i in range(len(s)):
        print(s[i], end='')

#Контест 5

#A Количество элементов, превосходящих опорный (1/10)
n = int(input())
s = []
k = 0
for i in range(n):
    s.append(int(input()))
base = int(input())
for i in range(n):
    if s[i] > s[base]:
        k += 1
print(k)


#B Циклический сдвиг (0/10)
def cycle_shift(arr, N):
    x = arr[0]
    for i in range(N - 1):
        arr[i] = arr[i + 1]
    arr[N - 1] = x
    return arr


#C Переворот массива (0/10)
def reverse_array(arr, N):
    if len(arr) != 1 and N != 0:
        arr[:N] = arr[N - 1::-1]
    return arr


#D Скалярное произведение двух векторов (0/10)
def dot_product(N, vector1, vector2):
    s = 0
    for i in range(N):
        s += vector1[i] * vector2[i]
    return s


#E Поиск локальных экстремумов (1/10)
n = int(input())
s = input().split()
k = []
for i in range(1, len(s) - 1):
    if (int(s[i - 1]) < int(s[i]) > int(s[i + 1])) or (int(s[i - 1]) > int(
            s[i]) < int(s[i + 1])):
        k.append(i)
for i in range(len(k)):
    print(k[i], end=' ')

#F Решето Эратосфена (простые числа до n) (2/10)
n = int(input())
a = []
for i in range(n + 1):
    a.append(i)
a[1] = 0
i = 2
while i <= n:
    if a[i] != 0:
        j = i + i
        while j <= n:
            a[j] = 0
            j = j + i
    i += 1
for i in range(a.count(0)):
    a.remove(0)
for i in a:
    print(i, end=' ')

#G Наибольшее число повторений в массиве (0/10)
n = int(input())
s = []
used = []
m = 1
for i in range(n):
    s.append(int(input()))
for i in s:
    if i not in used:
        if s.count(m) < s.count(i):
            m = i
        used.append(i)
print(m)

#H Треугольник Паскаля (1/10)
n = int(input())
for i in range(1, n + 2):
    s = [[0] * i for i in range(1, i + 1)]
s[0][0] = 1
if n >= 1:
    for i in range(2):
        s[1][i] = 1
for i in range(2, n + 1):
    for j in range(i + 1):
        if j == i or j == 0:
            s[i][j] = 1
        else:
            s[i][j] = s[i - 1][j - 1] + s[i - 1][j]
for i in range(len(s)):
    for j in range(len(s[i])):
        print(s[i][j], end=' ')
    print()

#Контест 6

#A Сортировка выбором (2/10)       O(n^2)
s = list(map(int, input().split()))
res = s.copy()
if s == sorted(s):
    print()
else:
    s = sorted(s)
    k = []
    for i in range(len(s)):
        k.append(0)
    for i in range(len(s)):
        if res[i] != s[i]:
            res[res.index(s[i])] = res[i]
            res[i] = s[i]
            for i in range(len(k)):
                print(res[i], end=' ')
            print()

#B Сортировка вставками (2/10)      O(n^2)
s = list(map(int, input().split()))
povt = 0
res = s.copy()


def swap(res, x):
    m = res[x]
    res[x] = res[x + 1]
    res[x + 1] = m


if s == sorted(s):
    print()
else:
    s = sorted(s)
    while res != s:
        for j in range(len(s) - 1):
            if res[j] > res[j + 1]:
                koord = j
                break
        if res.index(res[koord]) != s.index(res[koord]):
            swap(res, koord)
            for j in range(len(res)):
                print(res[j], end=' ')
            print()

#C Сортировка дурака (1/10)    O(n^3)
s = list(map(int, input().split()))
povt = 0
res = s.copy()


def swap(res, x):
    m = res[x]
    res[x] = res[x + 1]
    res[x + 1] = m


if s == sorted(s):
    print()
else:
    s = sorted(s)
    while res != s:
        for j in range(len(s) - 1):
            if res[j] > res[j + 1]:
                koord = j
                break
        swap(res, koord)
        for j in range(len(res)):
            print(res[j], end=' ')
        print()

#D Сортировка пузырьком (2/10) O(n^2)
s = list(map(int, input().split()))
povt = 0
res = s.copy()
if s == sorted(s):
    print()
else:
    s = sorted(s)
    while res != s:
        for i in range(len(s) - 1):
            while res[i] > res[i + 1]:
                m = res[i]
                res[i] = res[i + 1]
                res[i + 1] = m
                for j in range(len(res)):
                    print(res[j], end=' ')
                print()

#E Сортировка подсчетом (1/10) O(n + m)
s = list(map(int, input().split()))
count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
for i in range(len(s)):
    count[s[i]] += 1
    for i in count.values():
        print(i, end=' ')
    print()
for i in count.keys():
    for j in range(count[i]):
        print(i, end=' ')


#F Поразрядная сортировка (4/10) O(n)
def print_arr_1d(arr):
    for i in range(len(arr)):
        print(arr[i], end=' ')


def count_length(n):
    r = 0
    while n > 0:
        n = n // 10
        r += 1
    return (r)


s = list(map(int, input().split()))
length = 0
for i in range(len(s)):
    l_curr = count_length(s[i])
    if l_curr > length:
        length = l_curr
for i in range(length):
    c = [[] for i in range(2)]
    for j in range(len(s)):
        a_curr_r = (s[j] // (10**i)) % 10
        c[a_curr_r].append(s[j])
    s = []
    for j in range(2):
        s += c[j]
    print_arr_1d(s)
    print()

#G Сортировка по сумме цифр (2/10)
s = []
res = {}
n = int(input())


def count(x):
    m = 0
    for k in range(len(str(x))):
        m += int(str(x)[k])
    return m


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


for i in range(n):
    s.append(int(input()))
for i in range(n):
    res[s[i]] = count(s[i])
s = []
for j in sorted(res.values()):
    s.append(get_key(res, j))
for i in range(len(s)):
    print(s[i])

#H Сортировка только четных элементов (5/10)
n = int(input())
s = []
even = {}


def bubble_sort(arr):
    for i in range(0, len(arr), 1):
        for j in range(0, len(arr) - 1 - i, 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


for i in range(n):
    s.append(int(input()))
    if s[i] % 2 == 0:
        even[s[i]] = i
copy = list(even.keys())
copy2 = bubble_sort(copy.copy())
while copy != copy2:
    for i in range(len(copy) - 1):
        if int(copy[i]) > int(copy[i + 1]):
            buff = copy[i]
            buff2 = even[copy[i]]
            even[copy[i]] = even[copy[i + 1]]
            even[copy[i + 1]] = buff2
            copy[i] = copy[i + 1]
            copy[i + 1] = buff
for i in range(len(s)):
    if i not in even.values():
        print(s[i], end=' ')
    else:
        print(get_key(even, i), end=' ')

#I Сортировка дат (2/10)
n = int(input())
months = {
    'January': 0.0,
    'February': 31.0,
    ' March': 59.0,
    'April': 90.0,
    'May': 120.0,
    'June': 151.0,
    ' July': 181.0,
    'August': 212.0,
    'September': 243.0,
    'October': 273.0,
    'November': 304.0,
    'December': 334.0
}
date = []
for i in range(n):
    date.append(input().split())
copy = date.copy()
for j in range(n):
    copy[j] = float(
        date[j][0]) + months[date[j][1]] + float(date[j][2]) * 365.0 + (
            float(date[j][3][:2]) / 24.0) + (float(date[j][3][3:]) / 1440.0)
for i in range(len(copy)):
    for j in range(len(copy) - 1 - i):
        if copy[j] > copy[j + 1]:
            copy[j], copy[j + 1] = copy[j + 1], copy[j]
            date[j], date[j + 1] = date[j + 1], date[j]
for i in range(n):
    for j in range(4):
        print(date[i][j], end=' ')
    print()

#Контест 7


#A Рекурсивная матрешка (5/10)
def matryoshka(n):
    if n > 1:
        print('verh matryoshki {0}'.format(n))
        matryoshka(n - 1)
        print('niz matryoshki {0}'.format(n))
    else:
        print('matryoshechka')


#B Женские и мужские последовательности Хофштадтера (2/10)
def F(n):
    if n == 0:
        return 1
    else:
        return n - M(F(n - 1))


def M(n):
    if n == 0:
        return 0
    else:
        return n - F(M(n - 1))


#C Подтягивания лесенкой (4/10)
k = int(input())
m = int(input())


def stairs(k, m):
    if m != 1:
        return 2 * k + stairs(k + 1, m - 1)
    else:
        return k


print(stairs(4, 2))


#D Размен денег (4/10)
def make_exchange(money, coins):
    if money == 0:
        return 1
    elif money < 0:
        return 0
    if len(coins) == 0:
        return 0
    coins1 = coins[1:]
    return make_exchange(money, coins1) + make_exchange(
        money - coins[0], coins)


#E Можно ли получить из числа 1 отнимая 5 и 3? (3/10)
def is_add_35(n):
    if n == 1:
        return True
    elif n < 1:
        return False
    if is_add_35(n - 3) is True or is_add_35(n - 5) is True:
        return True
    return False


#F Все подмассивы массива (4/10)
def find(arr, lenn, coun, curr_arr):
    print(' '.join(curr_arr))
    if coun == len(arr) and lenn == 1:
        return
    if lenn == 1:
        find(arr, coun + 1, coun + 1, arr[:(coun + 1)])
    else:
        find(arr, lenn - 1, coun, curr_arr[1:])


arr = input().split()
find(arr, int(1), int(1), arr[0])


#G Два хода конем (7/10)
def step(x0, y0, x2, y2):
    if x0 + 2 <= 8 and x1 == x0 + 2 and ((y1 == y0 + 1 and y0 + 1 <= 8) or
                                         (y1 == y0 - 1 and y0 - 1 >= 1)):
        return True
    if x0 + 1 <= 8 and x1 == x0 + 1 and ((y1 == y0 + 2 and y0 + 2 <= 8) or
                                         (y1 == y0 - 2 and y0 - 2 >= 1)):
        return True
    if x0 - 2 >= 1 and x1 == x0 - 2 and ((y1 == y0 + 1 and y0 + 1 <= 8) or
                                         (y1 == y0 - 1 and y0 - 1 >= 1)):
        return True
    if x0 - 1 >= 1 and x1 == x0 - 1 and ((y1 == y0 + 2 and y0 + 2 <= 8) or
                                         (y1 == y0 - 2 and y0 - 2 >= 1)):
        return True
    return False


def ans(x0, y0, x2, y2):
    if x0 == x1 and y0 == y1:
        return 0
    if step(x0, y0, x2, y2):
        return 1
    if ((x0 + 2 <= 8 and y0 + 1 <= 8 and step(x0 + 2, y0 + 1, x2, y2))
            or (x0 + 2 <= 8 and y0 - 1 >= 1 and step(x0 + 2, y0 - 1, x2, y2))
            or (x0 + 1 <= 8 and y0 + 2 <= 8 and step(x0 + 1, y0 + 2, x2, y2))
            or (x0 + 1 <= 8 and y0 - 2 >= 1 and step(x0 + 1, y0 - 2, x2, y2))
            or (x0 - 2 >= 1 and y0 + 1 <= 8 and step(x0 - 2, y0 + 1, x2, y2))
            or (x0 - 2 >= 1 and y0 - 1 >= 1 and step(x0 - 2, y0 - 1, x2, y2))
            or (x0 - 1 >= 1 and y0 + 2 <= 8 and step(x0 - 1, y0 + 2, x2, y2))
            or (x0 - 1 >= 1 and y0 - 2 >= 1 and step(x0 - 1, y0 - 2, x2, y2))):
        return 2
    return -1


x0 = int(input())
y0 = int(input())
x1 = int(input())
y1 = int(input())
print(ans(x0, y0, x1, y1))


#H Детерминант матрицы (7/10)
def erase(matr, b, n1):
    mat1 = [[0 for i in range(n1 - 1)] for i in range(n1 - 1)]
    for i in range(0, n1 - 1, 1):
        for j1 in range(0, b, 1):
            mat1[i][j1] = matr[i + 1][j1]
        for j1 in range(b, n1 - 1, 1):
            mat1[i][j1] = matr[i + 1][j1 + 1]
    return mat1


def det(matr2, n2):
    if n2 == 2:
        return matr2[0][0] * matr2[1][1] - matr2[1][0] * matr2[0][1]
    ans = int(0)
    for i in range(0, n2, 1):
        ans += matr2[0][i] * pow(-1, i) * det(erase(matr2, i, n2), n2 - 1)
    return ans


n = int(input())
matr = [[0 for i in range(n)] for i in range(n)]
if n == 1:
    a = input()
    print(a)
    exit(0)
for i in range(0, n, 1):
    s = input().split()
    for j in range(0, n, 1):
        matr[i][j] = int(s[j])
print(str(det(matr, n)))

#Контест 8


#A Слияние (0/10)
def merge(L, R):
    merged_arr = [0] * (len(L) + len(R))
    a, b, c = 0, 0, 0

    while True:
        if a != len(L) and b != len(R):
            if int(L[a]) >= int(R[b]):
                merged_arr[c] = R[b]
                b += 1
                c += 1
            elif int(R[b]) >= int(L[a]):
                merged_arr[c] = L[a]
                a += 1
                c += 1
        else:
            break
    if a == len(L):
        merged_arr = merged_arr[:c] + R[b:]
    elif b == len(R):
        merged_arr = merged_arr[:c] + L[a:]
    return merged_arr


#B Сортировка слиянием (3/10)        O(n^2)
def merge(L, R):
    merged_arr = [0] * (len(L) + len(R))
    a, b, c = 0, 0, 0

    while True:
        if a != len(L) and b != len(R):
            if int(L[a]) >= int(R[b]):
                merged_arr[c] = R[b]
                b += 1
                c += 1
            elif int(R[b]) >= int(L[a]):
                merged_arr[c] = L[a]
                a += 1
                c += 1
        else:
            break
    if a == len(L):
        merged_arr = merged_arr[:c] + R[b:]
    elif b == len(R):
        merged_arr = merged_arr[:c] + L[a:]
    return merged_arr


def merge_sort(A):
    if len(A) > 1:
        left, right = A[:len(A) // 2], A[len(A) // 2:]
        return merge(merge_sort(left), merge_sort(right))
    else:
        return A


#C Разбиение по барьеру (0/10)
def split_barrier(A, barrier):
    L, E, M = [], [], []
    for i in range(len(A)):
        if int(A[i]) < barrier:
            L.append(int(A[i]))
        elif int(A[i]) == barrier:
            E.append(int(A[i]))
        else:
            M.append(int(A[i]))
    return L + E + M


#D Сортировка Хоара (2/10)   O(nlog(n))
def hoar_sort(A):
    if len(A) > 1:
        barrier = int(A[0])
        L, E, M = [], [], []
        for i in range(len(A)):
            if int(A[i]) < barrier:
                L.append(int(A[i]))
            elif int(A[i]) == barrier:
                E.append(int(A[i]))
            else:
                M.append(int(A[i]))
        return hoar_sort(L) + E + hoar_sort(M)
    else:
        return A


#E Выборы выборы (1/10)
def hoar_sort(A):
    if len(A) > 1:
        barrier = int(A[0])
        L, E, M = [], [], []
        for i in range(len(A)):
            if int(A[i]) < barrier:
                L.append(int(A[i]))
            elif int(A[i]) == barrier:
                E.append(int(A[i]))
            else:
                M.append(int(A[i]))
        return hoar_sort(L) + E + hoar_sort(M)
    else:
        return A


n = int(input())
groups_count = hoar_sort(list(map(int, input().split())))
if n % 2 == 0:
    groups_count = groups_count[:n // 2]
elif n % 2 == 1:
    groups_count = groups_count[:n // 2 + 1]
for i in range(len(groups_count)):
    groups_count[i] = groups_count[i] // 2 + 1
print(sum(groups_count))

#F

#G

#H