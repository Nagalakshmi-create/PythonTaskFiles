t = int(input())

for _ in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()] 
    maxi = max(a) 

    mxind = [i for i,x in enumerate(a) if x == maxi and i >= (k-1)]
    
    ans = 0

    for i in range(len(mxind)):
        if mxind[i] >= (k-1):
            ans += 1
            ans += n - (mxind[i]+1)

    print(ans)