#!/usr/bin/env python
# -*- coding: utf-8 -*-


def square_root(number: int) -> float:
    new_value = number**0.5
    return new_value
  

def square(number: int) -> int:
    new__value = number**2
    return new__value


def main() -> None:
    for i in range(25):
        print(f"Square root: {square_root(i)}, square: {square(i)}")


if __name__ == '__main__':
    main()
