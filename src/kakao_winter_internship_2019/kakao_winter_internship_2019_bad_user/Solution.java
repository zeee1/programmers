package kakao_winter_internship_2019_bad_user;



import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;

public class Solution {
    public static ArrayList<HashSet> totalAnswerSet;
    public static int count;

    public static int solution(String[] user_id, String[] banned_id) {
        int answer = 0;
        totalAnswerSet = new ArrayList<>();
        count = 0;

        ArrayList<String>[] candidateList = new ArrayList[banned_id.length];
        for(int i = 0 ; i < banned_id.length; i++){
            ArrayList<String> tmpSet = new ArrayList<>();

            for(int j = 0 ; j < user_id.length; j++){
                if(compareTwoString(user_id[j], banned_id[i])){
                    tmpSet.add(user_id[j]);
                }
            }

            candidateList[i] = tmpSet;
        }

        combination(candidateList, 0, new HashSet<>());
        answer = count;
        return answer;
    }

    public static boolean compareTwoString(String uid, String bid){
        if(uid.length() != bid.length())
            return false;

        for(int i = 0 ; i < uid.length(); i++){
            if(bid.charAt(i) == '*'){
                continue;
            }
            if (bid.charAt(i) != uid.charAt(i)){
                return false;
            }
        }

        return true;
    }

    public static void combination(ArrayList<String>[] candidateList, int depth, HashSet<String> answerSet){
        if(depth == candidateList.length){
            if(!totalAnswerSet.contains(answerSet)){
                HashSet<String> newAnswerSet= new HashSet<>();

                Iterator<String> iterator = answerSet.iterator();

                while(iterator.hasNext()){
                    newAnswerSet.add(iterator.next());
                }

                totalAnswerSet.add(newAnswerSet);
                count += 1;
            }
            return;
        }
        ArrayList<String> indexList = candidateList[depth];

        for(int i = 0 ; i < indexList.size(); i++){
            if(answerSet.contains(indexList.get(i))){
                continue;
            }

            answerSet.add(indexList.get(i));
            combination(candidateList, depth+1, answerSet);
            answerSet.remove(indexList.get(i));
        }
    }


    public static void main(String[] args){
        String[] user_id1 = {"frodo", "fradi", "crodo", "abc123", "frodoc"};
        String[] banned_id1 = {"fr*d*", "abc1**"};

        String[] user_id2 = {"frodo", "fradi", "crodo", "abc123", "frodoc"};
        String[] banned_id2 = {"*rodo", "*rodo", "******"};

        String[] user_id3 = {"frodo", "fradi", "crodo", "abc123", "frodoc"};
        String[] banned_id3 = {"fr*d*", "*rodo", "******", "******"};
        System.out.println(solution(user_id1, banned_id1));
        System.out.println(solution(user_id2, banned_id2));
        System.out.println(solution(user_id3, banned_id3));

    }
}
