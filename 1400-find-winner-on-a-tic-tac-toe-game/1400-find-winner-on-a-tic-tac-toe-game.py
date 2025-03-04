class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # print(len(moves))
        # if len(moves) == 9:
        #     return "Draw"
        # elif len(moves) <= 4:
        #     return "Pending"
        # elif len(moves) % 3:
        #     # print("A")
        #     return "A"
        # else:
        #     return "B"
        A = [0] * 8
        B = [0] * 8
        for i in range(len(moves)):
            row,col = moves[i]
            play = A if i % 2 == 0 else B
            play[row] += 1
            play[col + 3]  += 1
            if row == col:
                play[6] += 1
            if row == 2 - col:
                play[7] += 1
        print("A",A)
        print("B",B)
        for i in range(8):
            if A[i] == 3:
                return "A"
            if B[i] == 3:
                return "B"
        return "Draw" if len(moves) == 9 else  "Pending"
