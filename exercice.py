#!/usr/bin/env python
# -*- coding: utf-8 -*-


def square_root(number: int) -> float:
    
    return number**0.5
  

def square(number: int) -> int:
    # test
    return number**2


def main() -> None:
    for i in range(25):
        print(f"Square root: {square_root(i)}, square: {square(i)}")


if __name__ == '__main__':
    main()
