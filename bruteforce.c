#include<stdio.h>
#include<string.h>
char t[100],p[50];
void main()
{
     int position;
     printf("Enter the text ");
     scanf("%s",t);
     printf("Enter the pattern ");
     scanf("%s",p);
     position=brute_force();
     if(position==-1)
           printf("%s pattern not found in text",p);
      else
           printf("%s pattern found at index %d",p,position);
      getch();
}
int brute_force()
{
       int n,j,m,i;
       n=strlen(t);
       m=strlen(p);
       for(i=0;i<n;i++)
      {
             j=0;
             while(j<m && t[i+j]==p[j])
            {
                     j++;
                    if(j==m)
                            return i+1;  //pattern found
            }
      }
      return -1;  //pattern not found
}