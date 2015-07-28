
def get_pair(n,k):
    if n == 1 or n == 2:
        return 1
    if n == 3:
        return 4
    else:
        return k * ( 1 + (n -4) * k) + get_pair(n-1,k)


# when n =1, k=3    a1 = 1
# when n=2, a2 = 1  The rabits need 1 months to grow to produce
# when n=3, a3 = 3 + 1
# when n=4, a4 = 1 * 3 + a3
# when n=5, a5 = 4 * 3 + a4
# when n=6, a6 = 7 * 3 + a5
# when n=7, a7 = 10 * 3 + a6
