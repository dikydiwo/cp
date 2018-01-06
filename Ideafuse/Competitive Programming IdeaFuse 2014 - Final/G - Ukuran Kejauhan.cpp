#include <bits/stdc++.h>
using namespace std;

int main(){

    int n, x;

    scanf("%d", &n);
    for(int i=0; i<n; i++){
        scanf("%d", &x);
        int y = sqrt(x);
        printf("%d^2 = %d\n", y, y*y);
    }

    return 0;
}