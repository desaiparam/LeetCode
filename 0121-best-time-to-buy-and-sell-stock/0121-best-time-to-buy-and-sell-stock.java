class Solution {
    public int maxProfit(int[] prices) {
        int buyingStock = Integer.MAX_VALUE;
        int sellingStock = Integer.MIN_VALUE;
        int profit = 0;
        for (int i = 0; i < prices.length; i++) {
            if (buyingStock > prices[i]) {
                buyingStock = prices[i];
                System.out.println("buyingStock otto" + buyingStock);
            } else {
                int currentProfit = prices[i] - buyingStock;
                if (currentProfit > profit) {
                    profit = currentProfit;
                }
            }
            System.out.println("buyingStock i" + profit);
        }
        return profit;
    }
}