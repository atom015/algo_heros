#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main(){	
	int N,a,b;
	vector<pair<int,int> > v;
	scanf("%d", &N);
	for (int i = 0; i < N; i++){
		scanf("%d %d",&a,&b);
		v.push_back(make_pair(a,b));
	}
	sort(v.begin(),v.end());
	int point = v[N-1].second; 
	for (int i = 0; i < N-1; i++){
		int time = v[i].first,money = v[i].second;
		if (time != v[i+1].first){
			point += money;
		}
			
	}
	printf("%d",point);
}
