#include <iostream>
#include <vector>

using namespace std;


bool isDivided(int a, int c)
{
    //Is a divided by c?
    return a%c == 0;
}

bool areDivided(int a, int b, int c)
{
    //Are a, b divided by c?
    bool resa = (a%c == 0);
    bool resb = (b%c == 0);

    return resa && resb;
}

std::vector<int> getDividers(int a)
{
    //Get all dividers of a
    std::vector<int> dividers;

    //Test all reasonable dividers
    for (int c = 1; c <= a/2; c++)
    {
        //Is a divided by c?
        bool result = isDivided(a, c);

        //Number a is divided by c
        if (result)
        {
            dividers.push_back(c);
        }
    }

    return dividers;
}

std::vector<int> getDividers2(int a, int b)
{
    //Get all common dividers of a, b
    std::vector<int> dividers;

    //Test all reasonable dividers
    for (int c = 1; c <= a/2; c++)
    {
        //Are a, b divided by c
        bool result = areDivided(a, b, c);

        //Both numbers are divided by c
        if (result)
        {
            dividers.push_back(c);
        }
    }

    return dividers;
}


void printVector(std::vector<int> &v)
{
    //Print vector
    for (int value : v)
    {
        std::cout << value << " ";
    }
}


int main()
{
    //Numbers and their dividers
    int a = 24;
    int b = 48;
    int c = 5;

    //Test dividers
    bool result = isDivided(a, c);
    bool result2 = areDivided(a, b, c);

    //Print results
    std::cout << "a divided by c: " << result << '\n';
    std::cout << "a divided by c and b divided by c: " << result2 << '\n';

    //Find all dividers
    std::vector<int> dividers = getDividers(a);
    std::vector<int> dividers2 = getDividers2(a, b);

    //Print results
    printVector(dividers);
    printVector(dividers2);
}
