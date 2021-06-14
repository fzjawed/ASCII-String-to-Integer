class Solution:
    def solve(self, s):
        temp = '0'
        total = 0
        for ch in s:
            if ch.isdigit():
                temp += ch
            else:
                total += int(temp)
                temp = '0'
        return total + int(temp)