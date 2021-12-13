#include <iostream>
using namespace std;
int main()
{
    string a, b;
    cin >> a >> b;
    int numar = 0;
    for (int i = a.size() - 1; i >= 0; --i)
        if (a[i] == '1')
            numar += 1 << (a.size() - 1 - i);
    for (int i = b.size() - 1; i >= 0; --i)
        if (b[i] == '1')
            numar += 1 << (b.size() - 1 - i);
    cout << numar << '\n';
    return 0;
}