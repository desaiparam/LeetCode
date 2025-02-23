class Solution {
    public int maxEvents(int[][] events) {
       Arrays.sort(events,(a,b) -> a[0] - b[0]);
       PriorityQueue<Integer> pq = new PriorityQueue<>(); 
       int co = 0;
       int index = 0;
       for(int d = 0;d <= 100000; d++){
        while(!pq.isEmpty() && pq.peek() < d){
            pq.poll();
        }
        while(index < events.length && events[index][0] == d){
            pq.add(events[index++][1]);
        }
        if(!pq.isEmpty()){
            pq.poll();
            co++;
        }
       }
       return co;
    }
}