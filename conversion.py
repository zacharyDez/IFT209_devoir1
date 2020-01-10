def number(val: int) -> str:
    """
    returns number associated with numerical value
    """
    return str(val) if val < 10 else chr(val + 55)


def convert_from_base_10(x: int, b: int) -> str:
    """
    returns number converted from base 10 to base b
    """
    y = ""

    while True:
        y = number(x % b) + y
        x = x // b

        if x == 0:
            break

    return y


def convert_from_base_10_latex(x: int, b: int) -> str:
    """
    returns string in latex format for math demonstration
    """

    msg = "y = x \% b\qquad x = x\n\n"
    msg += f"y = {x} \% {b} \qquad x = {x}\n\n"
    y = ""

    # prints empty string if y entered
    msg += f"y = {x} \% {b}\qquad x = {x}\n\n"

    while True:
        y = number(x % b) + y
        x = x // b
        msg += f"y = {x} \% {b} + {y}\qquad "
        msg += f"x = {x}//{b}\n\n"

        if x == 0:
            msg += f"y = {y}\qquad \qquad x = {x}\n\n"
            break

    return msg


def convert_to_base_10(x: str, b: int, i=0) -> int:
    """
    returns number converted from base b to base 10
    """
    # allow function to be used with numbers
    if not isinstance(x, str):
        x = str(x)

    # breaks when length of number is reached
    if i == len(x) - 1:
        return int(x[-(i + 1)])
    return int(x[-(i + 1)]) + b * (convert_to_base_10(x, b, i + 1))


def convert_to_base_10_latex(x: str, b: int) -> str:
    """
    returns string in latex format for math demonstration
    """

    msg = f"{x}_{{{b}}} = y_{{10}}\n\n"
    msg += f"x_0 + b \\times (x_1 + b \\times (... + x_{{n-1}}\\times b))\n\n"

    # allow function to be used with numbers
    if not isinstance(x, str):
        x = str(x)

    for i in range(0, len(x)):
        if i == len(x) - 1:
            msg += f"{x[-(i + 1)]} + {b}{')' * i}"
        else:
            msg += f"{x[-(i + 1)]} + {b} \\times ("

    y = convert_to_base_10(x, b)

    msg += f"\n\n{x}_{{{b}}} = {y}_{{10}}"
    return msg


# example
if __name__ == "__main__":

    x = 34152
    b1 = 6

    print(convert_to_base_10_latex(x, b1))

