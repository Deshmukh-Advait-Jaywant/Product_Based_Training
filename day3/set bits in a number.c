#include<stdio.h>
void main()
{
    int count=0;
    int a = 15;
    while(a)
    {
        count++;
        a=a&(a-1);
    }
    printf("%d",count);
}
