class Solution:
    def solve(self,s):
        c,p = 0,0
        l = []
    
        for i in set(sorted(s)):
            t = []
            for j in sorted(s):
                if j == i:
                    t.append(j)
            l.append(t)
        l.sort(key=len)
    
        for i in range(len(l)):
            if len(l[i])==2:
                l.pop(i)
                p+=1
                break
            else:
                if len(l[i])%3!=0 and len(l[i])>2:
                    l[i].pop()
                    l[i].pop()
                    p+=1
                    break
        print(l)
        for i in l:
            if len(i)%3==0:
                c+=1
        return (c==len(l) and p == 1)
