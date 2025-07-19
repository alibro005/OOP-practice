#include <iostream>
using namespace std;
class Student
{
    int marks;

public:
    Student(int m)
    {
        m = marks;
    }

    bool operator<(const Student &other)
    {
        return marks < other.marks;
    }

    int getmarks()
    {
        return marks;
    }
};

int main()
{
    Student s1(20);
    Student s2(60);

    if (s1 < s2)
    {
        cout << "Student 1 has fewer marks." << endl;
    }
    else
    {
        cout << "Student 1 has more or equal marks." << endl;
    }

    return 0;
}