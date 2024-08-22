class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_alpha = {"2": 'abc',"3":'def',"4":'ghi',"5":'jkl',"6":'nmo',"7":'pqrs',"8":'tuv',"9":'wxyz'}
        if digits =="":
            return []
        all_alph=[]
        self.back(0,[],digits,number_alpha,all_alph)
        return all_alph
    def back(self,index:int ,path:List[str] ,digits:str ,letters:dict ,all_alph:List[str]):
        if len(path) == len(digits):
            all_alph.append(''.join(path))
            return
        posible_l = letters[digits[index]]
        for letter in posible_l:
            path.append(letter)
            self.back(index+1,path,digits,letters,all_alph)
            path.pop()




        