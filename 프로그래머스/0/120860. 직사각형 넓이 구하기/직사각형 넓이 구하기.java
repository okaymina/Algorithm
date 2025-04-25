class Solution {
    public int solution(int[][] dots) {
        int answer = 0;

        int maxX = Integer.MIN_VALUE;
        int minX = Integer.MAX_VALUE;
        int maxY = Integer.MIN_VALUE;
        int minY = Integer.MAX_VALUE;

        for (int[] dot : dots) {
            maxX = Math.max(maxX, dot[0]);
            minX = Math.min(minX, dot[0]);
            maxY = Math.max(maxY, dot[1]);
            minY = Math.min(minY, dot[1]);
        }

        answer = (maxX - minX) * (maxY - minY);
        
        return answer;
    }
}