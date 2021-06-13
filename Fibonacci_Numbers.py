def fib(num):
    a = 0
    b = 1
    for i in range(num):
        print(f'F{i} : ', end='')
        yield a
        temp = a
        a = b
        b = temp + b


while True:
    try:
        num = int(input('Enter The Number Of Fibonacci Numbers You Want To See : '))
        break
    except:
        print('Enter A Valid Input ( Integer )')
for x in fib(num):
    print(x)
