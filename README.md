# Number Theory of Fibonacci Numbers

This is a program for studying some number-theoretic properties of Fibonacci numbers.

## Number Theory (`nt.py`)

This module contains some standard number-theoretic functions.

## Fibonacci (`fibonacci.py`)

### Prime Factors
Fibonacci numbers with composite index greater than 4 are composite [[1]](#1). The converse however is false. `lpf` and `ppf` respectively return the least prime factor and the prime factorisation (slow for large index) of Fibonacci numbers with prime index [[2]](#2).

### Pisano Period
The Fibonacci sequence modulo `n` is periodic [[1]](#1). The period is known as the *Pisano period*. `period` returns the length of the Pisano period modulo `n` [[3]](#3).

## References

<a id="1">[1]</a> [Z[phi] and the Fibonacci Sequence Modulo n](https://sriasat.files.wordpress.com/2012/12/fibonacci13.pdf)

<a id="2">[2]</a> [On Fibonacci Numbers with Prime Index](https://sriasat.files.wordpress.com/2012/12/fibonacci31.pdf)

<a id="3">[3]</a> [Some Divisibility Properties of Fibonacci-Like Sequences](https://sriasat.wordpress.com/2013/08/30/some-divisibility-properties-of-fibonacci-like-sequences/)
