#include <iostream>
#include <string>

int cases;
std::string correct;
std::string incorrect;
int i;
int u;
int deleted;

int main()
{
    std::cin >> cases;
    for (int a = 0; a < cases;  a++)
    {
        i = 0;
        u = 0;
        deleted = 0;
        std::cin >> correct >> incorrect;
        while (i < correct.length() && u < incorrect.length())
        {
            if (correct[i] == incorrect[u])
            {
                i += 1;
                u += 1;
            }
            else
            {
                u += 1;
                deleted += 1;
            }
        }
        if (i == correct.length())
        {
            std::cout << "Case #" << a + 1 << ": " << deleted + incorrect.length() - u << "\n";
        }
        else
        {
            std::cout << "Case #" << a + 1 << ": IMPOSSIBLE\n";
        }
    }
}
