class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        below20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        tens = ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        scales = ["","Thousand","Million","Billion"]
        
        def three_digit_words(n):
            parts = []
            if n >= 100:
                parts.append(below20[n//100])
                parts.append("Hundred")
                n %= 100
            if n >=20:
                parts.append(tens[n//10])
                if n % 10 != 0:
                    parts.append(below20[n % 10])
            elif n > 0:
                parts.append(below20[n])
            return " ".join([p for p in parts if p])

        words = []
        scale_idx = 0
        while num >0:
            block = num % 1000
            if block != 0:
                chunk_words = three_digit_words(block)
                if scales[scale_idx]:
                    words.append(scales[scale_idx])
                words.append(chunk_words)
            num //= 1000
            scale_idx += 1
        return " ".join(reversed(words))