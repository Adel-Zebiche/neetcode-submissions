class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = [0] * 26
        win = [0] * 26
        idx = lambda c: ord(c) - ord('a')

        for c in s1:
            need[idx(c)] += 1
        for c in s2[:len(s1)]:
            win[idx(c)] += 1

        matches = sum(need[j] == win[j] for j in range(26))
        if matches == 26:
            return True

        for i in range(len(s1), len(s2)):
            out, inn = idx(s2[i - len(s1)]), idx(s2[i])

            if win[inn] == need[inn]: matches -= 1
            win[inn] += 1
            if win[inn] == need[inn]: matches += 1

            if win[out] == need[out]: matches -= 1
            win[out] -= 1
            if win[out] == need[out]: matches += 1

            if matches == 26:
                return True

        return False