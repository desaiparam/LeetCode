class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        ans = []
        restaurants.sort(key = lambda x:(x[1],x[0]),reverse = True)
        print(restaurants)
        for i in range(len(restaurants)):
            restaurantsId = restaurants[i][0]
            ratings = restaurants[i][1]
            vegan = restaurants[i][2]
            price = restaurants[i][3]
            distance = restaurants[i][4]
            if veganFriendly == 1 and vegan == 1 and price <= maxPrice and distance <= maxDistance:
                ans.append(restaurantsId)
            if veganFriendly == 0 and price <= maxPrice and distance <= maxDistance:
                ans.append(restaurantsId)
                # print("yes",restaurantsId)
            #     pass
            # if :
            #     print("sad Price",restaurantsId)
            # if :
            #     print("sad Distance",restaurantsId)
        return ans


        