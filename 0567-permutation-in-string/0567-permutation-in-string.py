class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)  > len(s2):
            return False
        set_s1 = {}
        set_s2 = {}
        for i in range(len(s1)):
            set_s1[s1[i]] = 1 + set_s1.get(s1[i],0)
            set_s2[s2[i]] = 1 + set_s2.get(s2[i],0)
            print("set_s1",set_s1)
            # print("set_s2",set_s2) 
        if set_s1 == set_s2:
            return True
        left = 0 
        for right in range(len(s1),len(s2)):
            set_s2[s2[right]] = 1 + set_s2.get(s2[right],0)
            set_s2[s2[left]] -= 1
            print("set_s2",set_s2) 

            if set_s2[s2[left]] == 0:
                # print("set_s2 del",set_s2[s2[left]]) 
                del set_s2[s2[left]]
            left += 1
            if set_s1 == set_s2:
                return True
        return False
