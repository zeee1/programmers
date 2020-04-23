package kakao_recruitment_2020_searching_lyrics;

import java.util.HashMap;

public class Solution {
    public static void main(String[] args){
        String[] words = {"frodo", "front", "frost", "frozen", "frame", "kakao"};
        String[] queries = {"fro??", "????o", "fr???", "fro???", "pro?"};

        int[] answer= solution(words, queries);

        for(int i = 0 ; i < answer.length; i++){
            System.out.print(answer[i]+" ");
        }
    }

    public static int[] solution(String[] words, String[] queries) {
        int[] answer = new int[queries.length];
        Trie root = new Trie('*');

        for(int i = 0 ; i < words.length; i++){
            Trie index = root;
            for(int j = 0 ; j < words[i].length(); j++){
                char tmp = words[i].charAt(j);

                index = index.addChild(tmp, words[i].length());
            }
        }

        for(int i = 0 ; i < queries.length; i++){
            Trie index = root;
            if(queries[i].startsWith("?"))
                continue;

            for(int j = 0 ; j < queries[i].length(); j++){
                if(index == null){
                    answer[i] = 0;
                    continue;
                }
                char tmp = queries[i].charAt(j);

                if(tmp == '?'){
                    answer[i] = index.getWordLen(queries[i].length());
                    break;
                }
                else{
                    index = index.getChild(tmp);
                }
            }
        }

        Trie reverseRoot = new Trie('*');

        for(int i = 0 ; i < words.length; i++){
            Trie index = reverseRoot;
            for(int j = words[i].length()-1 ; j >= 0 ; j--){
                char tmp = words[i].charAt(j);

                index = index.addChild(tmp, words[i].length());
            }
        }

        for(int i = 0 ; i < queries.length; i++){
            Trie index = reverseRoot;


            if(!queries[i].startsWith("?"))
                continue;

            for(int j = queries[i].length()-1 ; j >= 0 ; j--){
                char tmp = queries[i].charAt(j);

                if(index == null){
                    answer[i] = 0;
                    continue;
                }

                if(tmp == '?'){
                    answer[i] = index.getWordLen(queries[i].length());
                    break;
                }
                else{
                    index = index.getChild(tmp);
                }
            }
        }
        return answer;
    }
}

class Trie{
    public char c;
    public HashMap<Character, Trie> children;
    public HashMap<Integer, Integer> wordLength;

    public Trie(char c){
        this.c = c;
        this.children = new HashMap<>();
        this.wordLength = new HashMap<>();
    }

    public Trie addChild(char c, int wordLen){
        if(!children.containsKey(c)){
            children.put(c, new Trie(c));
        }

        if(wordLength.containsKey(wordLen)){
            wordLength.put(wordLen, wordLength.get(wordLen)+1);
        }else{
            wordLength.put(wordLen, 1);
        }

        return children.get(c);
    }

    public Trie getChild(char c){
        if(children.containsKey(c)){
            return children.get(c);
        }
        else{
            return null;
        }
    }

    public int getWordLen(int len){
        if(wordLength.containsKey(len)){
            return wordLength.get(len);
        }
        else
            return 0;
    }
}
