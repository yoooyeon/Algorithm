import java.util.Arrays;
import java.util.Comparator;

class Solution {
 public int solution(int[][] targets) {
        int answer = 0;
        int p=0;
        Arrays.sort(targets, Comparator.comparingInt((int[] o) -> o[1]));
        for (int[] target : targets) {
            if (p<=target[0]){
                answer+=1;
                p=target[1];
            }
        }

        return answer;
    }
}
