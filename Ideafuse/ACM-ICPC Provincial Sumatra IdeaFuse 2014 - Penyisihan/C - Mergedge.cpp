#include <bits/stdc++.h>
using namespace std;

int main(){

    int n, m, flag=0, ans=0;
    string s, temp;

    cin >> n >> m;
    for(int i=0; i<m; i++) temp += "0";
    for(int i=0; i<n; i++){
        cin >> s;
        for(int j=0; j<m; j++){

            if(s[j]=='1' && temp[j]=='0' && flag ==0){
                ans += 4;
                flag = 1;
            }
            else if(s[j]=='1' && temp[j]=='1' && flag==0){
                ans += 3;
                flag = 1;
            }
            else if(s[j]=='1' && s[j]==temp[j] && flag==1) ans+=2;
            else if(s[j] == '0') flag = 0;
            else ans += 3;
        }
        flag = 0;
        temp = s;
    }
    cout << ans << endl;

    return 0;
}