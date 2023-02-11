# Number Theory of Fibonacci Numbers

This is a program for studying some number-theoretic properties of Fibonacci numbers.

## Number Theory (`nt.py`)

This module contains some standard number-theoretic functions.

## Fibonacci (`fibonacci.py`)

This module contains the `FibonacciPrime` class, which represents a Fibonacci number with a prime index. It makes use of the `quadratic_integer` [[4]](#4) module. The module also contains a function `pisano_period` to compute the Pisano period.

### Prime Factors
Fibonacci numbers with composite index greater than 4 are composite [[1]](#1). The converse however is false. `lpf` and `ppf` respectively return the least prime factor and the prime power factorisation (slow for large index) of Fibonacci numbers with prime index [[2]](#2).

### Pisano Period
The Fibonacci sequence modulo `n` is periodic [[1]](#1). The period is known as the *Pisano period*. `pisano_period(n)` returns the length of the Pisano period modulo `n`. [[3]](#3).

## References

<a id="1">[1]</a> [Z[phi] and the Fibonacci Sequence Modulo n](https://sriasat.files.wordpress.com/2012/12/fibonacci13.pdf)

<a id="2">[2]</a> [On Fibonacci Numbers with Prime Index](https://sriasat.files.wordpress.com/2012/12/fibonacci31.pdf)

<a id="3">[3]</a> [Some Divisibility Properties of Fibonacci-Like Sequences](https://sriasat.wordpress.com/2013/08/30/some-divisibility-properties-of-fibonacci-like-sequences/)

<a id="4">[4]</a> [Symbolic Integer Arithmetic in Quadratic Integer Rings](https://github.com/nayel71/quadratic-integer)
