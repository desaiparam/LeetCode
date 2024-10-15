class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        sets = {}
        for i in range(len(magazine)):
            if magazine[i] in sets:
                sets[magazine[i]] += 1
            else:
                 sets[magazine[i]] = 1
        print(sets)
        # if ransomNote not in sets and len(ransomNote) <= len(sets):
        #     return False
        for i in range(len(ransomNote)):
            if ransomNote[i] in sets and sets[ransomNote[i]] > 0:
                sets[ransomNote[i]] -=1
            else:
                return False

        return True


        