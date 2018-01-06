#include <bits/stdc++.h>
using namespace std;

int main(){

    int t, k, ans=0;
    string s;

    cin >> t;
    while(t--){
        cin >> s;
        if(s == "donate"){
            cin >> k;
            ans += k;
        }else if(s == "report") cout << ans << "\n";
    }

    return 0;
}
