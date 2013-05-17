#include <iostream>
#include <vector>
#include <cmath>
#include <limits>

#include <boost/timer/timer.hpp>

using namespace std;

vector<double> testIterTrailing(vector<double> vec)
{
    for (auto it = vec.begin(); it != vec.end(); it++)
    {
        *it += *it;
    }
    return vec;
}

vector<double> testIterLeading(vector<double> vec)
{
    for (auto it = vec.begin(); it != vec.end(); ++it)
    {
        *it += *it;
    }
    return vec;
}

vector<double> testIndexTrailing(vector<double> vec)
{
    for (int it = 0; it < vec.size(); it++)
    {
        vec[it] += vec[it];
    }
    return vec;
}

vector<double> testIndexLeading(vector<double> vec)
{
    for (int it = 0; it < vec.size(); ++it)
    {
        vec[it] += vec[it];
    }
    return vec;
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
    // cout << ">label,1,wall" << endl;
    // cout << ">label,2,user" << endl;
    // cout << ">label,3,system" << endl;
    // cout << ">label,4,user+system" << endl;
    for (int i = 1; i < 50; ++i)
    {
        vector<double> test;
        x += 500000;
        vector<double> vec;
        for (int j = 0; j < x; ++j)
        {
            vec.push_back((double)j);
        }
        timer.start();
        test = testIterTrailing(vec);
        timer.stop();
        cout << "1," << x << "," << timer.elapsed().wall/1000000 << endl;
        // cout << "2," << x << "," << timer.elapsed().user/1000000 << endl;
        // cout << "3," << x << "," << timer.elapsed().system /1000000<< endl;
        // cout << "4," << x << "," << (timer.elapsed().system + timer.elapsed().user)/1000000 << endl;
        timer.start();
        test = testIterLeading(vec);
        timer.stop();
        cout << "2," << x << "," << timer.elapsed().wall << endl;
        timer.start();
        test = testIndexTrailing(vec);
        timer.stop();
        cout << "3," << x << "," << timer.elapsed().wall << endl;
        timer.start();
        test = testIndexLeading(vec);
        timer.stop();
        cout << "4," << x << "," << timer.elapsed().wall << endl;
    }

    return 0;
}