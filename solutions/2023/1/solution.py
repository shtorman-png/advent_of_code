from typing import Iterable, Generator, Callable, Generic, Self, ClassVar
from io import TextIOWrapper
import string
from rich import print
class Solution:
    @classmethod
    def part_1(cls: Self, file: TextIOWrapper) -> int:
        buf = 0
        for line in file:
            digits = [char for char in line if char in string.digits]
            buf += int(digits[0] + digits[-1]) 
            
        return buf
        
    @classmethod
    def part_2(cls: Self, file: TextIOWrapper) -> int:
        buf = 0
        full_nums = ["one","two","three", "four", "five", "six", "seven", "eight","nine"] + [*"123456789"]
        for index,line in enumerate(file):
            find_buf = [line.find(num) for num in full_nums]
            rfind_buf = [line.rfind(num) for num in full_nums]
            left = (find_buf.index(min([n for n in find_buf if n >= 0])))
            right = (rfind_buf.index(max([n for n in rfind_buf if n >= 0])))

            buf += (((find_buf.index(min([n for n in find_buf if n >= 0])) + 1) % 9 or 9) * 10 + ((rfind_buf.index(max([n for n in rfind_buf if n >= 0])) + 1) % 9 or 9))
        return buf