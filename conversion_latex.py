from conversion import convert_to_base_10, number


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
