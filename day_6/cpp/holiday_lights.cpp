#include <iostream>
#include <vector>
#include <fstream>
#include <boost/algorithm/string.hpp>

using namespace std;

const string ON = "on";
const string OFF = "off";
const string TOGGLE = "toggle";

typedef vector< vector<string> > param_vector;
typedef vector< vector<int> > boolean_grid;

boolean_grid init_grid(const int n)
{
    boolean_grid grid(n, vector<int>(n, 0));
    return grid;
}

void turn_on(boolean_grid& g, const int &i, const int &j, const bool numeric)
{
    if (numeric)
    {
        g[i][j] = g[i][j] + 1;
    }
    else
    {
        g[i][j] = 1;
    }
}

void turn_off(boolean_grid& g, const int &i, const int &j, const bool numeric)
{
    if (numeric && g[i][j] > 0)
    {
        g[i][j] = g[i][j] - 1;
    }
    else
    {
        g[i][j] = 0;
    }
}

void toggle(boolean_grid& g, const int &i, const int &j, const bool numeric)
{
    if (numeric)
    {
        g[i][j] = g[i][j] + 2;
    }
    else{
        bool v = !(g[i][j]);
        g[i][j] = v;
    }

}

void perform_operation(boolean_grid& g, const int &i1, const int &j1, const int &i2, const int &j2,
                       const string &op_type, const bool numeric)
{
    if (i1 >= g.size() || i2 >= g.size() || j1 >= g.size() || j2 >= g.size() || i2 < i1 || j2 < j1)
    {
        cout << "Invalid" << endl;
        cout << i1 << " " << j1 << " " << i2 << " " << j2 << endl;
    }
    if (ON.compare(op_type) == 0)
    {
        for (int i = i1; i<=i2; i++)
        {
            for (int j = j1; j <= j2; j++)
            {
                turn_on(g, i, j, numeric);
            }
        }
    }
    else if (OFF.compare(op_type) == 0) {
        for (int i = i1; i<=i2; i++)
        {
            for (int j = j1; j <= j2; j++)
            {
                turn_off(g, i, j, numeric);
            }
        }
    }
    else if (TOGGLE.compare(op_type) == 0)
    {
        for (int i = i1; i<=i2; i++)
        {
            for (int j = j1; j <= j2; j++)
            {
                toggle(g, i, j, numeric);
            }
        }
    }
}

void print_pretty_grid(const boolean_grid &g)
{
    for (int r = 0; r<g.size(); r++)
    {
        for (int row = 0; row < g[r].size(); row++)
        {
            bool value = g[r][row];
            if (value)
            {
                printf("@");
            } else{
                printf(".");
            }
            printf(" ");
        }
        printf("\n");
    }
    printf("\n\n");
}

param_vector get_input()
{
    std::ifstream fin("../input.txt");
    param_vector result;
    for (string line; getline(fin, line); ) {
        vector<string> strs;
        boost::split(strs, line, boost::is_any_of(" "));
        vector<string> line_split;
        for (size_t i = 0; i < strs.size(); i++) {
            if (strs.size() == 4) {
                line_split.push_back(strs[0]);
                vector<string> ij;
                boost::split(ij, strs[1], boost::is_any_of(","));
                line_split.push_back(ij[0]);
                line_split.push_back(ij[1]);
                boost::split(ij, strs[3], boost::is_any_of(","));
                line_split.push_back(ij[0]);
                line_split.push_back(ij[1]);
            } else if (strs.size() == 5) {
                line_split.push_back(strs[1]);
                vector<string> ij;
                boost::split(ij, strs[2], boost::is_any_of(","));
                line_split.push_back(ij[0]);
                line_split.push_back(ij[1]);
                boost::split(ij, strs[4], boost::is_any_of(","));
                line_split.push_back(ij[0]);
                line_split.push_back(ij[1]);
            }
        }
        result.push_back(line_split);
    }
    return result;
}

void test_grid()
{
    boolean_grid g = init_grid(100);
    param_vector params = get_input();
    for (int i = 0; i<params.size(); i++)
    {
        perform_operation(g,
                          stoi(params[i].at(1)),
                          stoi(params[i].at(2)),
                          stoi(params[i].at(3)),
                          stoi(params[i].at(4)),
                          params[i].at(0),
                          true);
    }
    perform_operation(g, 0, 0, 9, 9, "on", false);
    perform_operation(g, 9, 9, 9, 9, "off", false);
    perform_operation(g, 0, 0, 9, 9, "toggle", false);
    perform_operation(g, 0, 0, 9, 9, "toggle", false);
    perform_operation(g, 0, 0, 9, 0, "on", false);
    print_pretty_grid(g);
}

void run(const int &size, const bool numeric, const bool print_grid)
{
    boolean_grid g = init_grid(size);
    param_vector params = get_input();
    for (int i = 0; i<params.size(); i++)
    {
        perform_operation(g,
                          stoi(params[i].at(1)),
                          stoi(params[i].at(2)),
                          stoi(params[i].at(3)),
                          stoi(params[i].at(4)),
                          params[i].at(0),
                          numeric);
    }
    if (print_grid) print_pretty_grid(g);

    int counter;
    counter = 0;
    for (int i = 0; i<g.size();i++)
    {
        for (int j=0; j<g.size();j++)
        {
                counter += g[i][j];
        }
    }
    cout << counter << endl;
}

int main()
{
    run(1000, false, false); // non-numeric
    run(1000, true, false); // numeric
    return 0;
}

