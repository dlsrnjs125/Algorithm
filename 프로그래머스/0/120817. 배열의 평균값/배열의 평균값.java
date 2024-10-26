import java.util.*;

class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        int tmp = 0;
        
        for(int i=0; i< numbers.length; i++) {
            tmp += numbers[i];
        }
        
        answer = (double)tmp / numbers.length;
        
        
        return answer;
    }
}