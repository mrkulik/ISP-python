import readfromfile


def fibonacci(n):
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1


def start(file_name='fib.txt'):
    print list(fibonacci(n=int(readfromfile.read_from_file(file_name))))


start()