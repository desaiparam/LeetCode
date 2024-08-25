class Solution {
    public int maxProfit(int[] prices) {
        int buyingStock = Integer.MAX_VALUE;
        int sellingStock = Integer.MIN_VALUE;
        int profit = 0;
        for (int i = 0; i < prices.length; i++) {
            // System.out.println("buyingStock o"+prices[i]);
            // if (buyingStock>prices[i]){
            // buyingStock=prices[i];
            // System.out.println("buyingStock i"+buyingStock);
            // }
            // else if (sellingStock<prices[i]){
            // sellingStock=prices[i];
            // System.out.println("sellingStock"+sellingStock);
            // }
            if (buyingStock > prices[i]) {
                buyingStock = prices[i];
                System.out.println("buyingStock otto" + buyingStock);
            } else {
                int currentProfit = prices[i] - buyingStock;
                if (currentProfit > profit) {
                    profit = currentProfit;
                }
                // profit = prices[i]-buyingStock;
            }
            System.out.println("buyingStock i" + profit);
        }
        // if (sellingStock==Integer.MAX_VALUE || sellingStock==Integer.MIN_VALUE){
        // return 0;
        // }

        return profit;
    }
}