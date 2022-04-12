"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

"""

#solution
import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if re.fullmatch(p, s) == None: return False
        else: return True
        
