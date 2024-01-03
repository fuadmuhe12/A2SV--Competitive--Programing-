class Robot:

    def __init__(self, w: int, h: int):
        self.dic_point = {}# get x, y from number
        self.dic_number = {}# get number from x, y
        self.num = 0
        self.moved = False
        self.pos = (0,0)
        self.w = w
        self.h = h
        while self.num < w: #Easting
            self.dic_point[self.num] = (self.num, 0)
            self.dic_number[(self.num, 0)] = self.num
            self.num += 1

        for i in range(1, h): #northing
            self.dic_point[self.num] = (w-1, i)
            self.dic_number[(w-1, i)] = self.num
            self.num += 1
        for i in range(w-2, -1, -1):#Westign
            self.dic_point[self.num] = (i, h-1)
            self.dic_number[(i, h-1)] = self.num
            self.num += 1
        for i in range(h-2, 0, -1):#southing
            self.dic_point[self.num] = (0, i)
            self.dic_number[(0, i)] = self.num
            self.num += 1


    def step(self, num: int) -> None:
        if num > 0:
            self.moved = True
        num = num % ((self.w-1)*2 + (self.h-1)*2)
        
        self.pos = self.dic_point[(self.dic_number[self.pos] + num)%((self.w-1)*2 + (self.h-1)*2)]

    def getPos(self) -> List[int]:
        return list(self.pos)
        

    def getDir(self) -> str:
        x, y = self.pos
        if not self.moved and x == 0 and y == 0:
            return "East"
        else:
            if 1 <= x <= self.w-1 and y == 0:
                return "East"
            elif x == self.w-1 and 1 <= y <= self.h-1:
                return "North"
            elif 0 <= x <= self.w -2  and y == self.h-1:
                return "West"
            else:
                return "South"

        


# Your Robot object will be instantiated and called as such:
# obj = Robot(w, h)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()