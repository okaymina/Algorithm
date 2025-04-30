class Solution {
    public String solution(int age) {
        String[] alienDigits = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j"};
        String numStr = String.valueOf(age);
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < numStr.length(); i++) {
            int digit = numStr.charAt(i) - '0';
            sb.append(alienDigits[digit]);
        }
        return sb.toString();
    }
}