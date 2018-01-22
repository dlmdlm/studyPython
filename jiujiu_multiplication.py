#!/usr/bin/env python
# -*- coding -*-

from utils.util import multiplication


def multiplication1():
    count = 0
    for i in range(1, 10):
        for j in range(1, i + 1):
            count += 1
            print("%d * %d = %d" % (i, j, multiplication(i, j)), end=' ')
        print()
    print("multiplication1={}\n".format(count))


def multiplication2():
    count = 0
    for i in range(1, 10):
        for j in range(1, 10):
            count += 1
            if i >= j:
                pass
                print("%d * %d = %d" % (i, j, i * j), end=' ')
        print()
    print("multiplication1={}\n".format(count))


def multiplication3():
    count = 0
    for i in range(1, 10):
        for j in range(1, 10):
            count += 1
            if i >= j:
                pass
                print("%d * %d = %d" % (i, j, multiplication(i, j)), end=' ')
            else:
                break
        print()
    print("multiplication1=%d\n" % count)


def test():
    multiplication1()
    multiplication2()
    multiplication3()


if __name__ == '__main__':
    test()
