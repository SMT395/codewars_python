from math import log, sqrt
def isPP(n):
    # m^k = n hence exponent k is contained somewhere between 2 and the square root of n: 
    for k in range(2, round(sqrt(n)+1)):
        # loop over that range and find whichever base is an even integer such that k^log_k(n)|=m|=n.
        if k ** round(log(n, k)) == n:
            return [k, round(log(n, k))]
    return None