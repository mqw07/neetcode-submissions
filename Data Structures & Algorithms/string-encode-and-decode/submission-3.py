class Solution:

    def encode(self, strs: List[str]) -> str:
        lengs = [len(s) for s in strs]
        res = ''
        for index, string in enumerate(strs):
            res += f"{lengs[index]}#{string}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            leng = int(s[i: j])
            res.append(s[j + 1: 1 + j + leng])
            i = j + leng + 1
        return res
