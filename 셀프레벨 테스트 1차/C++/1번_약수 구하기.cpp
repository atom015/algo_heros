#include<stdio.h>
#include<iostream>
using namespace std;

int main(){	
	int N;
	scanf("%d",&N);
	for (int i = 1; i <= N; i++){
		if (N % i == 0){
			printf("%d ",i);
		}
	}
}
