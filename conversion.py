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


def convert_to_base_10(x: str, b: int, i=0, y=0) -> int:
    while i != len(x):
        y += int(x[-(i + 1)]) * b ** i
        i += 1

    return y


# example
if __name__ == "__main__":
    b = 7
    x = 314256
    y = convert_from_base_10(x, b)

    print(f"{x}_10 = {y}_{b}")
