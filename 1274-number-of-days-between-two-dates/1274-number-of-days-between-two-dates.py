class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        # gap = 0
        def lp(yr:int) -> bool:
            return yr % 4 == 0 and (yr % 100 !=0 or yr % 400 ==0)
        def dd(date:str) -> int:
            y , m , d = map(int,date.split('-'))
            gap = d + int(lp(y) and m>2) 
            gap += sum(365 + int(lp(y)) for y in range(1971,y))
            gap += sum([0,31,28,31,30,31,30,31,31,30,31,30,31][:m])
            print(gap)
            return gap
        return abs(dd(date1) - dd(date2))

        