class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        sub_table = {}
        # alphabet = "abcdefghijklmnopqrstuvwxyz"
        # key_without_spaces = key.replace(" ", "")
        # cha = set()
        i = 0
        for ch in key:
           if ch != ' ' and ch not in sub_table:
            sub_table[ch] = chr(ord('a') + i)
            i+=1
        print(sub_table)
        res = ""
        for ch in message:
            if ch != ' ':
                res += sub_table[ch]
            else:
                res += ' '
        return res


        