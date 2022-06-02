#!/usr/bin/python3
import fibo

print(fibo.fib(1000))
print(fibo.fib2(1000))
print(fibo.__name__)
bonucci = fibo.fib
nuchi = bonucci(500)
print(nuchi)
