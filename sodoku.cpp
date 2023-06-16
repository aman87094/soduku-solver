#include<bits/stdc++.h>
using namespace std;
# define blank 0
# define N 9
# define debug(a,b) cout<<#a<<" "<<a<<" "<<#b<<" "<<b<<endl;

bool find_blank(int grid[N][N],int &row,int &col);
void print_grid(int grid[N][N]);
bool is_safe(int grid[N][N],int row,int col,int num);
bool solve_sodoku(int grid[N][N]){
    int row,col;
    if(!find_blank(grid,row,col)){
        return true;//if there is no blank space 
    }
    // print_grid(grid);
    // debug(row,col);
    for(int num=1;num<=9;num++){
        if(is_safe(grid,row,col,num)){
            grid[row][col]=num;//assign the value assuming the value is correct and then call recursive function
            if(solve_sodoku(grid)){
                return true;
            }
            grid[row][col]=blank;//unassign the assigned value because it is not correct 
        }
    }
    return false;
}

bool find_blank(int grid[N][N],int& row,int& col){
    for( row=0;row<N;row++){
        for( col=0;col<N;col++){
            if(grid[row][col]==blank){
                // debug(row,col);
                return true;
            }
        }
    }
    return false;
}

bool row_used(int grid[N][N],int row,int num){
    for(int col=0;col<N;col++){
        if(grid[row][col]==num){
            return true;
        }
    }
    return false;
}
bool col_used(int grid[N][N],int col,int num){
    for(int row=0;row<N;row++){
        if(grid[row][col]==num){
            return true;
        }
    }
    return false;
}
bool box_3x3_used(int grid[N][N],int st_row,int st_col,int num){
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            if(grid[st_row+i][st_col+j]==num){
                return true;
            }
        }
    }
    return false;
}
bool is_safe(int grid[N][N],int row,int col,int num){
    return (!row_used(grid,row,num))&&(!col_used(grid,col,num))&&(!box_3x3_used(grid,row-row%3,col-col%3,num))&&grid[row][col]==blank;
}

void print_grid(int grid[N][N]){
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cout<<grid[i][j]<<" ";
        }
        cout<<endl;
    }
    
}



int main(){
    int grid[N][N] = { { 0, 4, 8, 0, 0, 0, 0, 7, 0 },
                       { 2, 7, 0, 6, 9, 0, 0, 3, 0 },
                       { 0, 3, 0, 0, 7, 2, 0, 4, 0 },
                       { 3, 0, 0, 0, 0, 0, 4, 1, 0 },
                       { 0, 9, 0, 1, 0, 8, 7, 0, 3 },
                       { 5, 1, 6, 0, 4, 0, 0, 0, 8 },
                       { 0, 2, 0, 0, 0, 9, 1, 0, 0 },
                       { 7, 5, 4, 2, 0, 1, 3, 0, 6 },
                       { 1, 0, 0, 7, 0, 5, 0, 0, 0 } };
    if(solve_sodoku(grid)==true){
        print_grid(grid);
    }
    else{
        cout<<"NO solution exits\n";
    }
    return 0;
}