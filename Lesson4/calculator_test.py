from calculator import Calculator

Calculator=Calculator() 

res=Calculator.sum(4,5)
assert res == 9

res = Calculator.sum(-6, -10)
assert res == -16

res = Calculator.sum(-6, 6)
assert res == 0

res = Calculator.sum(5.6, 4.3)
assert res == 9.9


print:

res = Calculator.sum(5.6, 4.3)
print(res)
assert res == 9.9

res = Calculator.sum(10, 0)
assert res == 10


res = Calculator.div(10, 2)
assert res == 5