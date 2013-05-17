#include <iostream>
#include <vector>
#include <cmath>
#include <limits>

#include <boost/timer/timer.hpp>

using namespace std;

class Test
{
public:
    Test() : x(1), y(2), z(3)
    {}
    double x;
    double y;
    double z;
    double doSomething(double val)
    { 
        double retVal = x+y+z+val;
        x += retVal;
        y += retVal;
        z += retVal;
        return retVal; 
    }
};

double testIterTrailing(vector<Test> vec)
{
    double sum = 0;
    for (auto it = vec.begin(); it != vec.end(); it++)
    {
        sum = it->doSomething(sum);
    }
    return sum;
}

double testIterLeading(vector<Test> vec)
{
    double sum = 0;
    for (auto it = vec.begin(); it != vec.end(); ++it)
    {
        sum = it->doSomething(sum);
    }
    return sum;
}

double testIndexTrailing(vector<Test> vec)
{
    double sum = 0;
    for (int it = 0; it < vec.size(); it++)
    {
        sum = vec[it].doSomething(sum);
    }
    return sum;
}

double testIndexLeading(vector<Test> vec)
{
    double sum = 0;
    for (int it = 0; it < vec.size(); ++it)
    {
        sum = vec[it].doSomething(sum);
    }
    return sum;
}

int main()
{
    boost::timer::cpu_timer timer;
    int x = 5000000;
    cout.precision(numeric_limits<double>::digits10 + 1);
    cout << ">label,1,Iterator Trailing" << endl;
    cout << ">label,2,Iterator Leading" << endl;
    cout << ">label,3,Index Trailing" << endl;
    cout << ">label,4,Index Leading" << endl;
    for (int i = 1; i < 50; ++i)
    {
        double test;
        x += 500000;
        vector<Test> vec;
        for (int j = 0; j < x; ++j)
        {
            vec.push_back(Test());
        }
        timer.start();
        test = testIterTrailing(vec);
        timer.stop();
        cout << "1," << x << "," << double(timer.elapsed().system + timer.elapsed().user) << endl;
        timer.start();
        test = testIterLeading(vec);
        timer.stop();
        cout << "2," << x << "," << double(timer.elapsed().system + timer.elapsed().user) << endl;
        timer.start();
        test = testIndexTrailing(vec);
        timer.stop();
        cout << "3," << x << "," << double(timer.elapsed().system + timer.elapsed().user) << endl;
        timer.start();
        test = testIndexLeading(vec);
        timer.stop();
        cout << "4," << x << "," << double(timer.elapsed().system + timer.elapsed().user) << endl;
    }

    return 0;
}