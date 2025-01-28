#include <bits/stdc++.h>
using namespace std;

int main()
{
    float s = sqrt(2) + sqrt(5) + sqrt(7);
    float x1 = 1.414213;
    float x2 = 2.236068;
    float x3 = 2.645751;
    float s1 = x1 + x2 + x3;
    float Ea = abs(s - s1);
    float Er = Ea / s;
    float Ep = Er * 100;
    cout << fixed << setprecision(6) << "Absoluter Error : " << Ea << endl
         << "Relative Error : " << Er << endl
         << "Percentage Error : " << Ep << "%" << endl;
    return 0;
}