class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        parsing = []
        for i in range(len(transactions)):
            parts = transactions[i].split(",")
            parsing.append((parts[0],int(parts[1]),int(parts[2]),parts[3],transactions[i]))
        print(parsing)
        invalid = [False] * len(transactions)
        # for i in parsing:
        #     if i[2] > 1000:
        #         ans.add(i[4])
        for i in range(len(parsing)):
            if parsing[i][2] > 1000:
                invalid[i] = True
                continue
            for j in range(len(parsing)):
                # print("Awesrdfgh",parsing[i][0])
                if i == j:
                    continue
                if parsing[i][0] == parsing[j][0] and abs(parsing[i][1]- parsing[j][1]) <= 60 and parsing[i][3] != parsing[j][3]:
                    invalid[i] = True
                    # ans.append(parsing[j][4])
        return [parsing[i][4] for i in range(len(transactions)) if invalid[i]]

       