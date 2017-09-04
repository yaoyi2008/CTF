#!/usr/bin/env python
# coding=utf-8

# first way
for a in xrange(10):
    for b in xrange(10):
        for c in xrange(10):
            for d in xrange(10):
                if a + b + c + d != 23:
                    continue
                if d == 0 or c == 0:
                    continue
                if c / d != 2:
                    continue
                if b != c - 1:
                    continue
                if a % c != 3:
                    continue
                print(a, b, c, d)

# second way
for a in xrange(10):
    for b in xrange(10):
        for c in xrange(10):
            for d in xrange(10):
                if c == 0 or d == 0:
                    continue
                if a + b + c + d != 23 or c / d != 2 or b - c != -1 or a % c != 3:
                    pass
                else:
                    print(a,b,c,d)

# third way
for a in xrange(10):
    for b in xrange(10):
        for c in xrange(10):
            for d in xrange(10):
                try:
                    if a + b + c + d != 23 or c / d != 2 or b - c != -1 or a % c != 3:
                        pass
                    else:
                        print(a,b,c,d)
                except:
                    pass
