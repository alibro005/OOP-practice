#include <iostream>
using namespace std;
int main()
{
   
   int A[3][3], B[3], D, D1, D2, D3, x, y, z;
   cout << "cramer's rule to solve linear equation x-2y+3z = 4" << endl;
   cout << "enter equation 1:" << endl;
   cin >> A[0][0] >> A[0][1] >> A[0][2];
   cout << "enter equation 2:" << endl;
   cin >> A[1][0] >> A[1][1] >> A[1][2];
   cout << "enter equation 3:" << endl;
   cin >> A[2][0] >> A[2][1] >> A[2][2];
   cout << "enter fourth column:" << endl;
   cin >> B[0] >> B[1] >> B[2];

   D = A[0][0] * ((A[1][1] * A[2][2]) - (A[1][2] * A[2][1])) - A[0][1] * ((A[1][0] - A[2][2]) - (A[1][2] - A[2][0])) + A[0][2] * ((A[1][0] * A[2][1]) - (A[1][1] * A[2][0]));

   D1 = B[0] * ((A[1][1] * A[2][2]) - (A[1][2] * A[2][1])) - A[0][1] * ((B[1] - A[2][2]) - (A[1][2] - B[3])) + A[0][2] * ((B[1] * A[2][1]) - (A[1][1] * B[2]));

   D2 = A[0][0] * ((B[1] * A[2][2]) - (A[1][2] * B[2])) - B[0] * ((A[1][0] - A[2][2]) - (A[1][2] - A[2][0])) + A[0][2] * ((A[1][0] * B[2]) - (B[1] * A[2][0]));

   D3 = A[0][0] * ((A[1][1] * B[2]) - (B[1] * A[2][1])) - B[0] * ((A[1][0] - B[2]) - (B[1] - A[2][0])) + B[0] * ((A[1][0] * A[2][1]) - (A[1][1] * A[2][0]));

   /* Code that determines if the system has a unique solution */

   if ((D) != 0)
   {
      cout << "\nSystem has a unique solution" << endl;
      x = D1 / D;
      y = D2 / D;
      z = D3 / D;
      cout << "x = " << x << endl;
      cout << "y = " << y << endl;
      cout << "z = " << z << endl;
   }
   else
   {
      cout << "\nSystem does not have a unique solution because determinant is 0";
   }
   return 0;
}
