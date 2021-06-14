alpha = re.compile(r"[a-z]+")
class Solution:
    def solve(self, s):
        return sum(map(int, alpha.sub(" ", s).split()))