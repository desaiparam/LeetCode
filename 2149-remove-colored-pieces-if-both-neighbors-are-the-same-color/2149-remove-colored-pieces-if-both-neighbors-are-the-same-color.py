class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        def helperA(colors):
            count = 0 
            for i in range(1,len(colors) - 1):
                if colors[i - 1] == "A"and colors[i] == "A" and colors[i + 1] =="A":
                    count += 1 
            print("A",count)
            return count
        def helperB(colors):
            count = 0
            for i in range(1,len(colors) - 1):
                if colors[i - 1] == "B"and colors[i] == "B" and colors[i + 1] =="B":
                   count += 1
            print("B",count)
            return count
        if len(colors) < 3:
            return False
        a = helperA(colors)
        b = helperB(colors)
        return a > b
        
        