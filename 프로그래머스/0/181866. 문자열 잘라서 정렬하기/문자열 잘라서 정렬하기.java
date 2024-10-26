import java.util.*;

class Solution {
    public String[] solution(String myString) {
        String[] splitArr = myString.split("x");
        List<String> result = new ArrayList<>();
        
        for (String str : splitArr) {
            if (!str.isEmpty()) {
                result.add(str);
            }
        }
        
        String[] answer = result.toArray(new String[result.size()]);
        Arrays.sort(answer);
        
        return answer;
    }
}