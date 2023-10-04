#include<stdio.h>
void main()
{
    int n;
    scanf("%d",&n);
    if(n<0)
    {
        printf("not power of 2");
    }
    else if(n&n-1)
    {
        printf("not power of 2");
    }
    else
    {
        printf("power of 2");
    }
}
