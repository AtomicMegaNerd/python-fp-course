# Composition
def f(x):
    return x + 2


def g(h, x):
    return h(x) * 2


# Closure
def addx(x):
    def _(y):
        return x + y

    return _


# Currying
def f2(x, y):
    return x * y


def f3(x):
    def _(y):
        return f2(x, y)

    return _


def main() -> None:
    print(g(f, 42))

    add2 = addx(2)
    add3 = addx(3)

    print(add2(2), add3(3))

    print(f3(2))
    print(f3(2)(3))


if __name__ == "__main__":
    main()
