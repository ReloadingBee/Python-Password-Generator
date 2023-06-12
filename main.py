import random
import string


def generatePassword(
    length: int = 10,
    upper: bool = True,
    lower: bool = True,
    numbers: bool = True,
    symbols: bool = True,
    suffix: string = None
):
    if length == 0 or length is None:
        return None

    charSet = ""
    if upper:
        charSet += string.ascii_uppercase
    if lower:
        charSet += string.ascii_lowercase
    if numbers:
        charSet += string.digits
    if symbols:
        charSet += string.punctuation
    if suffix is not None:
        charSet += suffix

    password = "".join(random.choice(charSet) for _ in range(length))
    return password

