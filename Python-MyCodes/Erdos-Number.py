from fractions import gcd

k = 16
a = 0

while True:
    ew = True
    for i in xrange(a + 1, a + k):
        if gcd(i, a) == 1 and gcd(i, a+k) == 1:
            ew = False
    if ew == True:
        print "Erdos Number:", k
        print "Proof:", a
        break
a += 1
