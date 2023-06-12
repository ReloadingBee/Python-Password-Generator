# Python-Password-Generator

Python Password Generator is a project that generates different passwords.

## Description

Python Password Generator is a simple tool that uses Python's built it libraries to generate different, secure passwords.

## Installation

Make sure you have [Python](https://www.python.org/) installed.

## Usage

To use Python Password Generator, you can call the `generatePassword` function. Optionally, you can specify the length of the password, the use of upperCased letters, the use of lowerCased letters, the use of numbers, the use of symbols and you can also add a suffix(any other characters you want to generate).

```python
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


print(generatePassword(10, True, False, True, False, "_-<>/"))

```
