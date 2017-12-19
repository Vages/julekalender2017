from math import sqrt
from typing import Set


def is_prime(n: int) -> bool:  # https://stackoverflow.com/questions/18833759/python-prime-number-checker
    if n % 2 == 0 and n > 2:
        return False

    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


def reverse_in_base_10(n: int) -> int:
    return int(str(n)[::-1])


def is_palindrome_in_base_10(n: int) -> bool:
    return reverse_in_base_10(n) == n


if __name__ == '__main__':
    primes: Set[int] = {n for n in range(2, 1000) if is_prime(n)}
    non_palindromic_primes: Set[int] = {p for p in primes if not is_palindrome_in_base_10(p)}
    emirps: Set[int] = {npp for npp in non_palindromic_primes if reverse_in_base_10(npp) in non_palindromic_primes}
    print(len(emirps))
