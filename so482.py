class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        tmp = "".join(S.split("-"))[::-1]
        res = ""
        for i in range(len(tmp)) :
            if i != 0 and i % K == 0 :
                res += "-" + tmp[i]
            else :
                res += tmp[i]
        return res[::-1].upper()