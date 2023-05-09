#include <iostream>
#include <ctime>

using namespace std;

int createBall(int n)
{
    //Create new ball, <=b : black, > b white
    return 1 + n * rand() / (RAND_MAX + 1);
}

bool simulate (int b, int w, int k)
{
   //Simulator, repeated selected of black or white balls from the box
   bool white_selected = false;
   bool black_selected = false;

   //Repeated selection
   for(int i = 0; i < k - 1; i++)
   {
       //Create random number ball
       int r = createBall(w + b);

       //std::cout << r << ' ';

       //Which ball did we select
       if (r <= b)
           black_selected = true;
       else
           white_selected = true;
   }

   //We chose black and white balls
   return black_selected && white_selected;
}

int main()
{
    //Initialize random number generator
    srand(time(0));

    //Perform simulations
    int repeat = 1e8, ns = 0;
    for (int i = 0; i < repeat ;i++)
    {
        //Create a test
        bool res = simulate(5, 4, 5);

        //Successful?
        if (res)
            ns++;
    }

    std::cout << "Results: " << double(ns)/repeat << '\n';

    return 0;
}
