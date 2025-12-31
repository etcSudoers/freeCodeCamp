'''
Sum the String

Given a string containing digits and other characters, return the sum of all numbers in the string.

    Treat consecutive digits as a single number. For example, "13" counts as 13, not 1 + 3.
    Ignore any non-digit characters.


'''
import re

def string_sum(s: str) -> int:
    allSums = 0
    allInts = re.findall(r'[0-9]+',s)
    for i in allInts:
        allSums = allSums + int(i)
    return allSums


string_sum("3apples2bananas") == 5
string_sum("10cats5dogs2birds") == 17
string_sum("125344") == 125344
string_sum("a1b20c300") == 321
string_sum("a12b34c56d78e90f123g456h789i0j1k2l3m4n5") == 1653