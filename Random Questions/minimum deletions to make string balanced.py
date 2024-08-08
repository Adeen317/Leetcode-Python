class Solution:
    def minimumDeletions(self, s: str) -> int:
        a = 0
        for c in s:
            a += 1 if c == "a" else 0
        b = 0
        res = len(s)
        for i, c in enumerate(s):
            if c == "a":
                a -= 1
            deletions = b + a
            res = min(res, deletions)
            if c == "b":
                b += 1
        return res
