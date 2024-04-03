def task_1(*args):
    print(args)


param = ['Hi', True, 1.5, 16]
task_1(*param)

num_ = int(input('print number: '))


def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n - 1) * n


print(fact(num_))
