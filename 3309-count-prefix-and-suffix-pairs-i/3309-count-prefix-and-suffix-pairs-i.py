class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count=0
        for i in range(0,len(words)):
            for j in range(i+1,len(words)):
                count =self.isPrefixAndSuffix(words[i],words[j],count)
        return count
    def isPrefixAndSuffix(self,wordI:string,wordJ:string,count:int) -> int:
        if wordJ[:len(wordI)] == wordI and wordJ[-len(wordI):] == wordI:
            print("wordI(0)",wordI[0],wordI[-1] )
            print("wordJ[0]",wordJ[0],wordJ[-1])
            count+=1
        return count

        