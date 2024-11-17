class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        emp_ro = set()
        que = collections.deque([])

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 2147483647:
                    emp_ro.add((i,j))
                    # rooms[i][j] = "Space"
                # if rooms[i][j] == -1:
                #     rooms[i][j] = "Wall"
                if rooms[i][j] == 0:
                    que.append((i,j,0))
                    emp_ro.add((i,j))
                    # rooms[i][j] = "Gate"
        print("que",que)
        print("emp_ro",emp_ro)
        while que:
            i,j,d = que.popleft()
            print(i,j,d)
            if (i,j) in emp_ro:
                rooms[i][j] = d
                emp_ro.remove((i,j))
                que.append((i+1,j,d+1))
                que.append((i,j+1,d+1))
                que.append((i,j-1,d+1))
                que.append((i-1,j,d+1))


        