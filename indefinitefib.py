import time

a, b = 0, 1  # initialize the first two numbers in the Fibonacci sequence

while True:
    print(a)  # print the current Fibonacci number
    time.sleep(1)  # wait for 1 seconds before the next iteration
    a, b = b, a + b + 1  # generate the next Fibonacci number and add 1 to it

