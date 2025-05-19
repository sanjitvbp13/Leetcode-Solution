class Solution {
    public String maximumOddBinaryNumber(String s) {
        int count1=0;
        int count0 =0;
        for (char c: s.toCharArray()){
            if (c=='1'){
                count1++;
            }
            else{
                count0++;
            }
        }
        StringBuilder ans = new StringBuilder();
        ans.append("1".repeat(count1-1));
        ans.append("0".repeat(count0));
        ans.append("1");
        return ans.toString();
        
    }
}