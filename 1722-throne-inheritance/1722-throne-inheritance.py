class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.children = {}
        self.dead = set()
        self.children[kingName] = []

    def birth(self, parentName: str, childName: str) -> None:
        if parentName not in self.children:
            self.children[parentName] = []
        self.children[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)        

    def getInheritanceOrder(self) -> List[str]:
        order = []
        def dfs(name):
            if name not in self.dead:
                order.append(name)
            if name in self.children:
                for child in self.children[name]:
                    dfs(child)
        dfs(self.king)
        return order


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()