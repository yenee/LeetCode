class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def skip_check(string, index):
            skip = 0
            while index >= 0:
                if string[index] == "#":
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    break
                index -= 1
            return index

        s_index = len(s) - 1
        t_index = len(t) - 1
        while s_index >= 0 or t_index >= 0:
            s1 = skip_check(s, s_index)
            t1 = skip_check(t, t_index)
            if s1 < 0 and t1 < 0:
                return True
            if s1 < 0 or t1 < 0:
                return False
            if s[s1] != t[t1]:
                return False
            s_index = s1 - 1
            t_index = t1 - 1
        return True
