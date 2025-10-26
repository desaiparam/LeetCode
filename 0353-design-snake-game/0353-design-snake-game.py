class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake = deque([(0,0)]) 
        self.set = {(0,0)}
        self.h = height
        self.w = width
        self.idx = 0
        self.food = food
    def move(self, direction: str) -> int:
        head = self.snake[0]
        r ,c= head
        if direction == "U":
            r -= 1
        if direction == "D":
            r += 1
        if direction == "L":
            c -= 1
        if direction == "R":
            c += 1
        if r < 0 or c < 0 or r == self.h or c == self.w:
            return -1
        for i in range(len(self.snake)-1):
            temp = self.snake[i]
            if (r,c) == (temp[0],temp[1]):
                return -1
        if self.idx < len(self.food):
            if [r,c] ==  self.food[self.idx]:
                self.snake.appendleft([r,c])
                self.idx += 1
                return len(self.snake) -1
        self.snake.appendleft([r,c])
        self.snake.pop()
        return len(self.snake) - 1


        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)