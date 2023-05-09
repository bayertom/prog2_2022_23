#include <iostream>
#include <vector>
#include <tuple>
#include <cmath>

using namespace std;

//Create structure representing a planet
struct Planet
{
    //Coordinates
    double x;
    double y;
    double z;

    //Radius
    double r;
};

double get2PlanetsDistance(Planet &p, Planet &q)
{
    //Get distance between 2 planets
    double dx = p.x - q.x;
    double dy = p.y - q.y;
    double dz = p.z - q.z;

    return sqrt(dx * dx + dy * dy + dz * dz) - p.r - q.r;
}

std::tuple<int, int, double> getNearestPlanets(std::vector<Planet> &P)
{
    //Get distance between two nearest planets
    double dmin = get2PlanetsDistance(P[0], P[1]);
    int i1min = -1;
    int i2min = -1;

    //Process all pairs of planets
    for(int i = 0; i < P.size(); i++)
    {
        for(int j = i + 1; j < P.size(); j++)
        {
            //Get distance
            double d = get2PlanetsDistance(P[i], P[j]);

            //Actualize minimum
            if (d < dmin)
            {
                i1min = i;
                i2min = j;
                dmin = d;

            }
        }
    }

    return {i1min, i2min, dmin};
}


double getNearestPlanets(std::vector<Planet> &P, int &i1min, int &i2min)
{
    //Get distance between two nearest planets
    double dmin = get2PlanetsDistance(P[0], P[1]);

    //Process all pairs of planets
    for(int i = 0; i < P.size(); i++)
    {
        for(int j = i + 1; j < P.size(); j++)
        {
            //Get distance
            double d = get2PlanetsDistance(P[i], P[j]);

            //Actualize minimum
            if (d < dmin)
            {
                i1min = i;
                i2min = j;
                dmin = d;

            }
        }
    }

    return dmin;
}


int main()
{
    //Create empty list of planets
    std::vector<Planet> P;

    //Initialize planrets
    Planet p1{0, 0, 0, 5};
    Planet p2{10, 20, 30, 0};
    Planet p3{30, 40, 15,10};
    Planet p4{4, 17, 9, 6};
    Planet p5{9, 5, 23, 1};

    //Add planets to the vector
    P.push_back(p1);
    P.push_back(p2);
    P.push_back(p3);
    P.push_back(p4);
    P.push_back(p5);

    //Get distance between two nearest planets
    //Pass both indices by reference
    int i1min = -1, i2min = -1;
    double dmin = getNearestPlanets(P, i1min, i2min);
    std::cout << "Nearest distance: " << dmin << ", i1: " << i1min << ", i2: " << i2min << '\n';

    //Get distance between two nearest planets
    //Return both indices as a tuple
    auto [i3min, i4min, d2min] = getNearestPlanets(P);

    std::cout << "Nearest distance: " << d2min << ", i1: " << i3min << ", i2: " << i4min << '\n';

    return 0;
}
