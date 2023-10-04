#include<stdio.h>
void main()
{
    int n=15,i=4;
    printf("%d",n&(1<<i-1));
}

if output is zero the the i'th pos is not 1
else i'th pos is 1