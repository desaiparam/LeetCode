class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        e = []
        g = []
        p = []
        r = []
        pattern = '^[a-zA-Z0-9_]+$'
        for i in range(len(businessLine)):
            if isActive[i]:
                if businessLine[i] == "electronics":
                    if re.fullmatch(pattern, code[i]):
                        e.append(code[i])
                elif businessLine[i] == "grocery":
                    if re.fullmatch(pattern, code[i]):
                        g.append(code[i])
                elif businessLine[i] == "pharmacy":
                    if re.fullmatch(pattern, code[i]):
                        p.append(code[i])
                elif businessLine[i] =="restaurant":
                    if re.fullmatch(pattern, code[i]):
                        r.append(code[i])
        return sorted(e)+sorted(g)+sorted(p)+sorted(r)