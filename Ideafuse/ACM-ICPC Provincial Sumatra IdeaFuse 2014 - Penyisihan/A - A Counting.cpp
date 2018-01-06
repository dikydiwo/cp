#include <bits/stdc++.h>
using namespace std;

int main(){

    int t, x, y;

    scanf("%d", &t);
    for(int i=0; i<t; i++){
        scanf("%d %d", &x, &y);
        while(x<=y && y>=x){
            if(x == y) break;
            x += 7;
            y -= 5;
        }
        if(x == y) printf("Case #%d: %d\n", i+1, x);
        else printf("Case #%d: impossible\n", i+1);
    }

    return 0;
}