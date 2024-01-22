def kthFactor(n: int, k: int) -> int:
    factors = [1]
    i = 2
    while len(factors) < k and i <= n:
        if n % i == 0:
            factors.append(i)
            i += 1
        else:
            i += 1
    if(len(factors) is k):
        return factors[len(factors) - 1]
    else:
        return -1

print(kthFactor(7, 2))