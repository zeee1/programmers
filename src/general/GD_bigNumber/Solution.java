package GD_bigNumber;

public class Solution {
    public static void main(String[] args){
        System.out.println(solution("1924", 2));
        System.out.println(solution("1231234", 3));
        System.out.println(solution("4177252841", 4));
    }

    public static String solution(String number, int k){
        StringBuilder  answer = new StringBuilder();
        int cnt = number.length() - k;
        int left = 0;
        int right = k;
        while(cnt > 0){
            int max = -1;
            int idx = 0;

            for(int i = left; i <= right; i++){
                if(max < number.charAt(i)-'0'){
                    max = number.charAt(i)-'0';
                    idx = i;
                }
            }

            answer.append(number.charAt(idx));
            left = idx+1;
            right = number.length()-(cnt-1);
            cnt-=1;
        }
        return answer.toString();
    }
}
