
def get_pair(n,k):
    if n == 1 or n == 2:
        return 1
    else:
        return k * get_pair(n-2,k) + get_pair(n-1,k)


