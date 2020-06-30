#include<stdio.h>
#include<iostream>
#include<queue>
using namespace std;

int main(){	
	int N,ans=0;
	scanf("%d",&N);
	queue<int> q;
	q.push(0);
	while (!q.empty()){
		int p = q.front();
		q.pop();
		if (p == N){
			ans += 1;
			continue;
		}
		if (p > N){
			continue;
		}
		q.push(p+1);
		q.push(p+2);
	}
	printf("%d",ans);
}
