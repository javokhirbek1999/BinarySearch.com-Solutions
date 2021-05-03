class Solution:
    def solve(self, words):
        words.sort(key=len)
        prex = []
        for i in words:
            c = 0
            for j in words:
                if i.startswith(j):
                    c+=1
            prex.append([i,c])
        prex.sort(key=lambda x:x[1])

        t = 0
        for i in words:
            if prex[-1][0].startswith(i):
                t +=1
        return t
