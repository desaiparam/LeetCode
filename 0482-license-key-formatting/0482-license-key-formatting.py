class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        co = 0
        newS = ['']
        # print(s[::-1])
        # for i range(len(s[::-1])):
        #     if co != k:
        #         if s[i] == 
        #         newS(s[i])
        for i in s[::-1]:
            if i != '-':
                newS += i.upper()
                co += 1

            # if co != k+1:
            #     print("co", co)
            #     co += 1
            #     if i == '-':
            #         continue
            #     else:
            #         newS += i.upper()
            if co == k:
                # newS += i.upper()
                newS += '-'
                co = 0

        if (len(newS) > 0 and newS[len(newS)-1] == '-'):
            newS = newS[:-1]
        newS = newS[::-1]
        # res = .joi
            
        # for j in newS:
        #     if co != k:
        #         co += 1
        #         print(co)
        #     elif co == k:
        #         print("gh")
        #         newS+= '-'
        #         co = 0 
            
        # print(newS)
        print(newS)
        return "".join(newS)