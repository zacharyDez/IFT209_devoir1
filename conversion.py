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


def convert_to_base_10(x: int, b: int) -> int:
    y = 0
    str_x = str(x)

    print(f"y_10 = {x}_{b}")

    msg = "y_10 = "
    for i in range(0, len(str_x)):
        msg += f" {str_x[-1 - i]}*{b}**{i} + "
        y += int(str_x[-1 - i]) * b ** i

    print(msg)
    return y


# example
if __name__ == "__main__":
    b = 7
    x = 314256
    y = convert_from_base_10(x, b)

    print(f"{x}_10 = {y}_{b}")
