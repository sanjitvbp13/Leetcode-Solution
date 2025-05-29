class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> ans=new ArrayList<>();
        List<String> temp=new ArrayList<>();
        for(int i=0; i<n; i++){
            StringBuilder st=new StringBuilder();
            for(int j=0; j<n; j++){
                st.append(".");
            }
            temp.add(st.toString());

        }
        find(ans,temp,n,0);
        System.out.println(temp);
        return ans;
    }
    void find(List<List<String>> ans,List<String> temp,int n,int i){
        if(i==n){
            ans.add(new ArrayList<>(temp));
            return;
        }
        for(int j=0; j<n; j++){
            if(isSafe(temp,n,i,j)){
                StringBuilder t=new StringBuilder(temp.get(i));
                t.setCharAt(j,'Q');
                temp.set(i,t.toString());

                find(ans,temp,n,i+1);

                StringBuilder t2=new StringBuilder(temp.get(i));
                t2.setCharAt(j,'.');
                temp.set(i,t2.toString());
            }
        }     
    }
    boolean isSafe(List<String> temp,int n,int i,int j){
        for(int x=0; x<i; x++){
            if(temp.get(x).charAt(j)=='Q') return false;
        }
        int d1 = i;
        int d2 = j;
        while (d1 >= 0 && d2 >= 0) {
            if (temp.get(d1).charAt(d2) == 'Q') return false;
            d1--;
            d2--;
        }
        d1 = i;
        d2 = j;
        while (d1 >= 0 && d2 < n) {
            if (temp.get(d1).charAt(d2) == 'Q') return false;
            d1--;
            d2++;
        }

        return true;

    }
}