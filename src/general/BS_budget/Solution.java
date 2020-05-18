package BS_budget;

public class Solution {
    public static int solution(int[] budgets, int M) {
        int answer = 0;
        int min = 0;
        int max = 0;

        for(int i = 0 ; i < budgets.length; i++){
            max = Math.max(max, budgets[i]);
        }

        int prevDiff = Integer.MAX_VALUE;
        while(min <= max){
            int mid = (min+max)/2;

            int sum = 0;
            for(int i = 0 ; i < budgets.length; i++){
                if(budgets[i]> mid){
                    sum += mid;
                }
                else{
                    sum += budgets[i];
                }
            }

            if(sum > M){
                max = mid-1;
            }else{
                min = mid+1;
            }

            int diff = M-sum;

            if(diff < 0){
                continue;
            }
            else{
                if(diff < prevDiff){
                    answer = mid;
                    prevDiff = diff;
                }
            }
        }
        return answer;
    }

    public static void main(String[] args){
        int[] budgets = {120,110, 140, 150};
        System.out.println(solution(budgets, 485));
    }
}
