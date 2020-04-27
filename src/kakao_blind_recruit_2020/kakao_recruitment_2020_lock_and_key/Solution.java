package kakao_recruitment_2020_lock_and_key;

public class Solution {
    public static int emptyCount = 0;
    public static int count =0;
    public static int M;
    public static int N;

    public static void main(String[] args){
        int[][] key = {{0,0,0},{1,0,0},{0,1,1}};
        int[][] lock = {{1,1,1},{1,1,0},{1,0,1}};

        System.out.println(solution(key, lock));
    }

    public static boolean solution(int[][] key, int[][] lock) {

        N = lock.length;

        for(int i = 0 ; i < N ; i++){
            for(int j = 0 ; j < N ; j++){
                if(lock[i][j] == 0){
                    emptyCount += 1;
                }
            }
        }

        int[][] bigArray = new int[3*N][3*N];

        for(int i = 0 ;i < N ; i++){
            System.arraycopy(lock[i], 0, bigArray[N+i], N, N);
        }

        M = key.length;

        for(int i = 0 ; i < 4; i++){

            for(int j = 0 ; j <= (3*N - M); j++){
                for(int k = 0 ; k <= (3*N - M); k++){
                    count = 0;
                    if(filled(j, k, key, bigArray)&&count == emptyCount)
                        return true;

                }
            }

            int[][] rotatedKey = rotateLeft(key);
            key = rotatedKey;
        }

        for(int i = 0 ; i < 4; i++){

            for(int j = 0 ; j <= (3*N - M); j++){
                for(int k = 0 ; k <= (3*N - M); k++){
                    count = 0;

                    if(filled(j, k, key, bigArray)&&count == emptyCount)
                        return true;



                }
            }

            int[][] rotatedKey = rotateRight(key);
            key = rotatedKey;
        }

        return false;
    }



    public static int[][] rotateLeft(int[][] key){
        int[][] rotatedKey = new int[M][M];

        for(int i = 0 ; i < M ; i++){
            for(int j = 0 ; j < M ; j++){
                if(key[i][j] == 1){
                    rotatedKey[j][(M-1)-i] = 1;
                }
            }
        }
        return rotatedKey;
    }

    public static int[][] rotateRight(int[][] key){
        int[][] rotatedKey = new int[key.length][key.length];
        for(int i = 0 ; i < M ; i++){
            for(int j = 0 ; j < M ; j++){
                if(key[i][j] == 1){
                    rotatedKey[(M-1)-j][i] = 1;
                }
            }
        }
        return rotatedKey;
    }

    public static boolean filled(int x, int y, int[][] key, int[][] bigArray){

        for(int i = 0 ; i < M ; i++){
            int indexX = x + i;

            if (indexX < N || indexX >=2*N)
                continue;

            for(int j = 0; j < M ; j++){
                int indexY = y + j;

                if(indexY < N || indexY >= 2*N)
                    continue;

                if(bigArray[indexX][indexY] == 0 && key[i][j] == 1){
                    count += 1;
                }

                if(bigArray[indexX][indexY] == key[i][j])
                    return false;
            }
        }

        return true;
    }




}
