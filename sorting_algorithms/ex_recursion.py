# coding=utf-8


def countdown(i):
    print("i =", i)
    if i <= 1:  # base case
        return
    else:  # recursive case
        countdown(i - 1)


def use_countdown(n):
    countdown(n)  # This is the initial call to the function


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


def main():
    # use_countdown(5)
    print(fact(3))


if __name__ == '__main__':
    main()