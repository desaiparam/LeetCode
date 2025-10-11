class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hashmap = Counter(s)
        print(hashmap)
        result = []
        for i in order:
            if i in hashmap:
                while hashmap[i]:
                    result.append(i)
                    hashmap[i] -= 1
                del hashmap[i]
        for i in hashmap:
            while hashmap[i]:
                result.append(i)
                hashmap[i] -= 1
        return "".join(result)

        