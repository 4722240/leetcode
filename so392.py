class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        tmp = -1
        for i in s:
            tmp = t.find(i,tmp+1)
            print(tmp)
            if tmp == -1 :
                return False
        return True

    def isSubsequence2(self,s:str,t:str)->bool:
        m,n = len(s),len(t)
        f = [ [0] * 26 for _ in range(n)]
        f.append([n]* 26)
        for i in range(n-1 ,-1 ,-1) :
            for j in range(26):
                f[i][j] = i if ord(t[i]) == j + ord('a') else f[i+1][j]
        for i in f :
            print(i)
        tmp =0
        for i in s:
            if f[tmp][ord(i)-ord('a')] == n :
                return False
            tmp = f[tmp][ord(i)-ord('a')] + 1
            print(tmp)
        return True