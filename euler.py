import math

# Python 3 program to calculate
# Euler's Totient Function
# using Euler's product formula


def euler(n):

    result = n  # Initialize result as n

    # Consider all prime factors
    # of n and for every prime
    # factor p, multiply result with (1 – 1/p)
    p = 2
    while(p*p <= n):

        # Check if p is a prime factor.
        if (n % p == 0):

            # If yes, then update n and result
            while (n % p == 0):
                n = n / p
            result -= result / p

        p += 1

    # If n has a prime factor
    # greater than sqrt(n)
    # (There can be at-most one
    # such prime factor)
    if (n > 1):
        result -= result / n

    return int(result)

if __name__ == "__main__":
    arr = [0, 1]

    with open('euler.txt', 'w') as f:
        for n in range(2, 1000000):
            result = n-1
            p = 2
            while(p*p <= n):
                if(n % p == 0):
                    m = int(n/p)
                    d = math.gcd(p, m)
                    result = int(arr[p]*arr[m]*d/arr[d])
                    break
                p += 1

            arr.append(result)
            source = str(n)
            target = str(arr[n])
            f.write(str.join(" ", list(source)) + "\t" + str.join(" ", list(target)) + "\n")
