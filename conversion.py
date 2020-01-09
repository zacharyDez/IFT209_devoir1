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


def convert_to_base_10(x: str, b: int, i=0) -> int:
    """
    returns number converted from base b to base 10
    """

    # allow function to be used with numbers
    if not isinstance(x, str):
        x = str(x)

    # breaks when length of number is achieved
    if i == len(x) - 1:
        return int(x[-(i + 1)])
    return int(x[-(i + 1)]) + b * (convert_to_base_10(x, b, i + 1))


# example
if __name__ == "__main__":
    b = 7
    x = 314256
    y = convert_from_base_10(x, b)

    print(f"{x}_10 = {y}_{b}")
