#include<bits/stdc++.h>
using namespace std;

int main()
{
    float x = (1*1.0)/3;
    vector <float> approx = {0.30,0.31,0.32,0.33,0.34};
    vector <float> error;
    for (float i : approx){
        error.push_back(abs(x-i));
    }
    cout << "Minimum approx error: " << *min_element(error.begin(),error.end()) << endl;
    int index = 0 ;
    for (float i : error)
    {
        if (i == *min_element(error.begin(),error.end()))
        {
            break;
        }
        index++;
    }
    
    cout << "Best approximation: " << approx[index] << endl;
    return 0;
}