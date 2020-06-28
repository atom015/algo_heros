#include<stdio.h>
#include<iostream>
using namespace std;

int main(){	
	int N,dp[100];
	scanf("%d",&N);
	dp[0] = 1;
	dp[1] = 1;
	for (int i = 2; i <= N; i++){
		dp[i] = dp[i-1]+dp[i-2];
	}
	printf("%d",dp[N]);
}
