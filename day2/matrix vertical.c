#include<stdio.h>
void main()
{
    int n,i,j,flag1,flag2,flag3,flag4;
    printf("enter the value of n");
    scanf("%d",&n);
    int m[n][n];
    
    printf("enter the values of n");
    for(i=1;i<=4;i++)
    {
        for(j=1;j<=4;j++)
        {
            scanf("%d",&m[i][j]);
        }
    }
    printf("the matrix is");
    for(i=1;i<=4;i++)
    {
        for(j=1;j<=4;j++)
        {
            printf("%d",m[i][j]);
        }
        printf("\n");
    }
    
    int one_horizontal_cnt=0;
    int one_veritical_cnt=0;
    int one_right_diagonal_cnt=0;
    int one_left_diagonal_cnt=0;
    int zero_horizontal_cnt=0;
    int zero_veritical_cnt=0;
    int zero_right_diagonal_cnt=0;
    int zero_left_diagonal_cnt=0;
    
    for(j=1;j<=n;j++)
    {
        flag1=m[1][j];
        for(i=1;i<=4;i++)
        {
            if(m[i][j]!=flag1)
            {
                flag1=100;
                break;
            }
        }
        if(flag1!=100)
        {
            if(flag1==1)
            {
                one_veritical_cnt++;
            }
            else
            {
                zero_veritical_cnt++;
            }
        }
    }
    printf("1-vertical-count: %d\n",one_veritical_cnt);
    printf("0-vertical-count; %d\n",zero_veritical_cnt);
    
    for(i=1;i<=4;i++)
    {
        flag2=m[i][1];
        for(j=1;j<=4;j++)
        {
            if(m[i][j]!=flag2)
            {
                flag2=100;
                break;
            }
        }
        if(flag2!=100)
        {
            if(flag2==1)
            {
                one_horizontal_cnt++;
            }
            else
            {
                zero_horizontal_cnt++;
            }
        }
    }
    printf("1-hori-count: %d\n",one_horizontal_cnt);
    printf("0-hori-count; %d\n",zero_horizontal_cnt);
    
    flag3=m[1][1];
    for(i=1;i<=4;i++)
    {
        if(m[i][i]!=flag3)
        {
            flag3=100;
            break;
        }
    }
    if(flag3!=100)
    {
        if(flag3==1)
        {
            one_left_diagonal_cnt++;
        }
        else
        {
            zero_left_diagonal_cnt++;
        }
    }
    printf("1-left-diag-count: %d\n",one_left_diagonal_cnt);
    printf("0-left-diag-count; %d\n",zero_left_diagonal_cnt);
    
    flag4=m[1][4];
    for(i=0;i<4;i++)
    {
        for(j=5;i<1;j--)
        {
            if(m[i+1][j-1]!=flag4)
            {
                flag4=100;
                break;
            }
        }
        if(flag4!=100)
        {
            if(flag4==1)
            {
                one_right_diagonal_cnt++;
            }
            else
            {
                zero_right_diagonal_cnt++;
            }
        }
    }
    printf("one_right_diagonal_cnt: %d\n",one_right_diagonal_cnt);
    printf("zero_right_diagonal_cnt: %d\n",zero_right_diagonal_cnt);
    
    
    
    

}