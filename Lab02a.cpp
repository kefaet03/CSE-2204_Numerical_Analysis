#include <bits/stdc++.h>
using namespace std;

float poly(const vector<float> &coeff, int n, float x)
{
    float result = 0.0;
    for (int i = 0; i <= n; i++)
    {
        result += coeff[i] * pow(x, n - i);
    }
    return result;
}

float bisection(vector<float> coeff, int n)
{
    float a, b;
    cout << "Approximation" << endl;
    while (1)
    {
        cout << "a : ";
        cin >> a;
        cout << "b : ";
        cin >> b;

        if (poly(coeff, n, a) * poly(coeff, n, b) < 0)
        {
            break;
        }
        else
        {
            cout << "Invalid input of a or b" << endl << "Try again" << endl;
        }
    }

    float xr = 0;
    int count = 0;
    float error = 0.0;
    int max_iterations = 100;

    while (count < max_iterations)
    {
        float temp = xr;
        xr = (a + b) / 2;

        if (count > 0)
        {
            error = abs(xr - temp);
        }

        cout << count << " " << a << " " << b << " " << xr << " " << error << endl;
        count++;

        float f_xr = poly(coeff, n, xr);
        // cout <<  f_xr << " " << error << endl;

        if (f_xr == 0 || (error <= 0.001 && count > 1))
        {
            break;
        }

        if (poly(coeff, n, a) * f_xr < 0)
        {
            b = xr;
        }
        else
        {
            a = xr;
        }
    }
    return xr;
}

float false_position(vector<float> coeff, int n)
{
    float a, b;
    cout << "Approximation" << endl;
    while (1)
    {
        cout << "a : ";
        cin >> a;
        cout << "b : ";
        cin >> b;

        if (poly(coeff, n, a) * poly(coeff, n, b) < 0)
        {
            break;
        }
        else
        {
            cout << "Invalid input of a or b" << endl << "Try again" << endl;
        }
    }

    float xr = a;
    int count = 0;
    float error = 0.0;
    int max_iterations = 100;

    while (count < max_iterations)
    {
        float f_a = poly(coeff, n, a);
        float f_b = poly(coeff, n, b);

        float temp = xr;
        xr = (a * f_b - b * f_a) / (f_b - f_a);

        if (count > 0)
        {
            error = abs(xr - temp);
        }

        cout << count << " " << a << " " << b << " " << xr << " " << error << endl;
        count++;

        float f_xr = poly(coeff, n, xr);

        if (f_xr == 0 || (error <= 0.001 && count > 1))
        {
            break;
        }

        if (f_a * f_xr < 0)
        {
            b = xr;
        }
        else
        {
            a = xr;
        }
    }

    return xr;
}

int index(vector<float>coeff, int n){
    int common_index = 0;
    for (int i = coeff.size()-2; i >= 0 ; i--)
    {
        if (coeff[i]!=0)
        {
            common_index = i;
            break;
        }
    }
    return common_index;
}

float func(vector <float> coeff, int n, float x,int common_index){
    float common_power = coeff.size() - 1 - common_index*1.0;

    float result = 0.0;
    for (int i = 0; i <= common_index ; i++)
    {
        result += coeff[i] * pow(x, coeff.size()-1-i-common_power);
    }
    // cout <<  pow((((-1)*coeff[coeff.size()-1])/result),1/common_power) << endl;
    return pow((((-1)*coeff[coeff.size()-1])/result),1/common_power);
}

float iteration(vector<float> coeff, int n)
{
    float initial;
    cout << "Initial guess : ";
    cin >> initial;

    float xr = initial;
    int count = 0;
    int max_iterations = 50;

    int common_index = index(coeff,n);
    // cout <<  common_index << endl;

    while (count < max_iterations)
    {
        float error = 0.0;
        float temp = xr;
        xr = func(coeff,n,temp,common_index);

        error = abs(xr-temp);

        cout << count << " " << temp << " " << xr << " " << error << endl;
        count++;

        if (error <= 0.001) {
            break;
        }
    }

    return xr;
}

int main()
{
    cout << "Order : ";
    int n;
    cin >> n;
    vector<float> coeff(n + 1);
    cout << "The form of the equation" << endl
         << "ax^(n) + bx^(n-1) + ..... + ex + z = 0" << endl
         << "Enter the co-efficients" << endl;
    for (int i = 0; i <= n; i++)
    {
        cin >> coeff[i];
    }

    while (1)
    {
        cout << "Choose your method" << endl
             << "1. Bisection\n2. False Position\n3. Iteration Method\n0. Exit" << endl;
        int choose;
        cin >> choose;

        if (choose == 1)
        {
            cout << "Root : " << bisection(coeff, n) << endl;
        }
        else if (choose == 2)
        {
            cout << "Root : " << false_position(coeff, n) << endl;
        }
        else if (choose == 3)
        {
            cout << "Root : " << iteration(coeff,n) << endl;
        }
        else
        {
            break;
        }
    }

    return 0;
}