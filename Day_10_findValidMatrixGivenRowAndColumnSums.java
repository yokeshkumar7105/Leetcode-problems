class Solution {
    public int[][] restoreMatrix(int[] rowSum, int[] colSum) {
        int row = rowSum.length;
        int col = colSum.length;
        int mat[][] = new int[row][col];
        int i=0,j=0;

        while(i<row&&j<col){
            int mini = Math.min(rowSum[i],colSum[j]);
            mat[i][j]=mini;
            rowSum[i]-=mini;
            colSum[j]-=mini;
            if(rowSum[i]==0){
                i++;
            }
            if(colSum[j]==0){
                j++;
            }
        }
        return mat;
    }
}
