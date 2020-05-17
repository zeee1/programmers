package BS_Immigration;


public class Solution {
    public static long solution(int n, int[] times) {
        long min = 1;
        long max = 0;
        for(int i = 0 ; i < times.length; i++){
            if(times[i] > max){
                max = times[i];
            }
        }

        max *= n;
        long answer = max;

        while(min <= max){
            long mid = (min+max)/2;

            long sum = 0;
            for(int i = 0 ; i < times.length; i++){
                sum +=(mid/times[i]);
            }

            if(sum < n){
                min = mid+1;
            }else{
                if(mid < answer){
                    answer = mid;
                }
                max = mid-1;
            }
        }
        return answer;
    }
    public static void main(String[] args){
        int[] times = {7, 10};
        System.out.println(solution(6, times));
    }
}
