class Solution:
    def numSquares(self, n: int) -> int:
        # ps = set()
        ps = []
        # print(n)
        for i in range(1, int(n**0.5)+1):
            # print(i)
            # if int(i**0.5) * int(i**0.5) == i:
            #     # print("i",i)
            #     # ps.add(i)
            ps.append(i*i)
        visi = set()
        # print(ps)
        que = deque()
        que.append((0,0))
        while que:
            target , ste = que.popleft()
            if target == n:
                return ste
            # res = []
            for i in ps:
                # print(target)
                n_target  = i+ target
                # print(i,"i",n_target+target)
                if n_target == n:
                    return ste + 1
                if n_target < n and n_target not in visi:
                    visi.add(n_target)
                    que.append((n_target,ste+1))
                    # print(que)
        # print(visi)
        return -1
        