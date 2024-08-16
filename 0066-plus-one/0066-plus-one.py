class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            else:
                digits[i]=0
                # return digits
        return [1]+digits
        
        # if len(str(last_element)) >=2 and len(digits) == 1:
        #     new_list = [int(new_list) for new_list in str(last_element)]
        #     return new_list
        # elif len(str(last_element)) >=2 and len(digits) > 1:
        #     new_list = [int(new_list) for new_list in str(last_element)]
        #     last_element = new_list[-1]
        #     second_element = new_list[-2]
        #     # new_list.append(second_element)
        #     new_list.append(last_element)
        #     print(new_list)
        #     return new_list
        # else:
        #     digits[-1] = last_element
        #     return digits


        
        