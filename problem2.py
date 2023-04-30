# Even Fibonacci numbers

initial_range_to_work_with = list(range(1,4000000))
fib_list = list()

value1 = 0
value2 = 1
sum_fib_even = 0


max_value = initial_range_to_work_with[len(initial_range_to_work_with)-1]

while value1+value2 < max_value:
    sum_fx = value1 + value2
    if sum_fx%2 == 0:
        sum_fib_even = sum_fib_even + sum_fx
    value1 = value2
    value2 = sum_fx

print(sum_fib_even)