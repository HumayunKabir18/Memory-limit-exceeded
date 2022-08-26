try:
    t=int(input())
    for i in range(t):
        f,l=map(int,input().split())
        c=list(range(1,l+1,1))
        n=f
        z=[]
        while n<=l:
            k=map(str,c[:n])
            j="".join(k)
            z.append(j)
            n=n+1
        z=list(map(int,z))
        w=0
        for x in z:
            if x%3==0:
                w=w+1
        print(f'Case {i+1}: {w}')
except:
    pass
