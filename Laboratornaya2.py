import functools

def Spisok(x = list()):
    s1 = list()
    s2 = list()
    s3 = list()
    for i in range(len(x)):#проходим по исходному списку, проверяем делимость и распределяем между списками
        if ((x[i] % 2) == 0):
            s1.append(x[i])
        if ((x[i] % 3) == 0):
            s2.append(x[i])
        if ((x[i] % 5) == 0):
            s3.append(x[i])
    return s1, s2, s3 #возвращаем списки

def Reverse(n):# воспроизводим число наоборот
    x = str(abs(n))
    s = ""
    for a in range(len(x)):#разбиваем на символы
        s += str(x[((len(x)-1)-a)])#воспроиводим наоборот
    if (n < 0):# если исходное число отрицательное, добавляем минус
        return -int(s)
    return int(s)#возвращаем число

def Palindrom(n):
    return n==Reverse(n)#используем предыдущую функцию чтобы проверить палиндром

def newton(a, x, n, accuracy=0.0000000000000001):
    xn = 1/n * ((n-1)*x + a/(pow(x, (n-1))))# формула Ньютона для вычисления нового приближения
    if ((x-xn) <= accuracy):#проверка на точность
        return xn
    else:
        return newton(a, xn, n)# вызываем рекурсию

def Prosto(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

print('Func1:', Palindrom(5225))
print('Func2:', Spisok(list([2,25,9,256,135,8, 74, 225])))
print('Func3:', Reverse(-9468214))
print('Func4:', newton(2,8,4))
print('Func5:',  Prosto(513))





