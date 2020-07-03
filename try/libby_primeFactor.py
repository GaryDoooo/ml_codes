def is_prime(a):
    if int(a) != a:
        return False
    if a <= 1:
        return False
    for i in range(2, int(a) - 1):
        if a / i == int(a / i):
            return False
    return True


def pf(a):
    res = []
    if is_prime(a):
        res = [a]
    while is_prime(a) == False and a > 1:
        for i in range(2, int(a)):
            if is_prime(i) and a / i == int(a / i):
                a = a / i
                res.append(i)
    res.sort()

    return res


def primeFactors(n):
    a = pf(n)
    seta = set(a)
    listseta = list(seta)
    res = ""

    for i in range(len(seta)):
        # print(listseta[i],a.count(listseta[i]))
        res = res + "(" + str(listseta[i]) + \
            "**" + str(a.count(listseta[i])) + ")"
    return res


def test_small(m, a):
    if m == a:
        print(a)
    elif m > a:
        count = 0
        while int(m / a) == m / a:
            m = m / a
            count += 1
        if count == 1:
            print(a)
        elif count > 1:
            print(a, "**", count)
        test_small(m, a + 1)


#  print(test_small(7775460,2))
print(primeFactors(15460))
