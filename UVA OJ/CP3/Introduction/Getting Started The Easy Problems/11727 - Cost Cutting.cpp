#include <bits/stdc++.h>
using namespace std;

int main(){

    int t, a,b,c, data[10005], cnt=1;

    cin >> t;
    while(t--){
        cin >> a >> b >> c;
        data[0] = a; data[1] = b; data[2] = c;
        sort(data, data+3);
        cout << "Case " << cnt << ": " <<  data[1] << "\n";
        cnt++;
    }

    return 0;
}
