class Solution {
    public int lengthOfLastWord(String s) {

        String [] st = s.split(" ");
        //for(String i : st){System.out.println(i);}
        String s1 = st[st.length-1];
        //System.out.println(s1);
        return s1.length();
        
    }
}
