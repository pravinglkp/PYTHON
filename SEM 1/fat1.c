#include<stdio.h>
#include<math.h>
int main()
{
	int n,a[100],i,j,b[100][100],x,y,num[100],k,s=0,u;
	float avg[100],d;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	i=1;
	x=0;
	while(i<(n/2))
	{
		y=0;
		s=0;
		for(j=i;j<n-i;j++)
		{
			b[x][y]=a[j];
			y++;
			s=s+a[j];
		}
		printf("\n");
		avg[x]=s/(float)(y);
		num[x]=y;
		x=x+1;
		i=i+1;
	}
	for(i=0;i<x-1;i++)
	{
		for(j=i+1;j<x;j++)
		{
			d=avg[i]-avg[j];
			d=fabs(d);
			if(d<1.2)
			{
				for(u=0;u<num[i];u++)
				{
					printf("%d ",b[i][u]);
				}
				printf("\n");
				for(u=0;u<num[j];u++)
				{
					printf("%d ",b[j][u]);
				}
				printf("\n\n");
			}
		}
	}
	return 0;
}