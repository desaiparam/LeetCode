class Solution:
    def intToRoman(self, num: int) -> str:
        hashmap = {
            "M": 1000,
            "CM":900,
            "D": 500,
            "CD":400,
            "C": 100,
            "XC":90,
            "L": 50,
            "XL":40,
            "X": 10,
            "IX":9,
            "V": 5,
            "IV": 4,
            "I": 1   
        }
        res = []
        for s,v in hashmap.items():
            if num == 0:
                break
            count = num//v
            res.append(s*count)
            num-= count*v
        return ''.join(res)