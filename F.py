def digit(e, i):
    return int(e[i])


def digit_task(e, i, m):
    i = i - (m-len(e))
    if i < 0:
        return 0
    return int(e[i])


def lsd(a):
    base = 10
    n = len(a)
    m = len(a[0])
    for i in range(m-1, -1, -1):
        c = [[] for _ in range(base)]
        for e in a:
            d = digit(e, i)
            c[d].append(e)

        j = 0
        for i in range(base):
            for e in c[i]:
                a[j] = e
                j += 1

        for k in range(base):
            for e in c[k]:
                print(e, end=' ')
        print()


def lsd_task(a):
    base = 2
    m = max(len(i) for i in a)
    for i in range(m-1, -1, -1):
        c = [[] for _ in range(base)]
        for e in a:
            d = digit_task(e, i, m)
            c[d].append(e)

        j = 0
        for i in range(base):
            for e in c[i]:
                a[j] = e
                j += 1

        for k in range(base):
            for e in c[k]:
                print(e, end=' ')
        print()

    # j = 0
    # for i in range(base):
    #     for e in c[i][::-1]:
    #         a[j] = e
    #         j += 1


x = ['112', '023', '011', '213']
#x = ['10', '1', '0']
# x = input().split()
lsd(x)
