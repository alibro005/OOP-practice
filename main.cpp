// #include <iostream>
// using namespace std;

// // Abstract base class
// class Animal {
//   public:
//     // Pure virtual function
//     virtual void makeSound() = 0;

//     void sleep() {
//         cout << "Animal is sleeping." << endl;
//     }
// };

// // Derived class 1
// class Dog : public Animal {
//   public:
//     void makeSound() {
//         cout << "Dog says Woof!" << endl;
//     }
// };

// // Derived class 2
// class Cat : public Animal {
//   public:
//     void makeSound() {
//         cout << "Cat says Meow!" << endl;
//     }
// };

// int main() {
//     // Animal a;         ❌ Error: cannot instantiate abstract class
//     Dog d;
//     d.makeSound();       // Output: Dog says Woof!
//     d.sleep();           // Output: Animal is sleeping.

//     Cat c;
//     c.makeSound();       // Output: Cat says Meow!
// }

// #include <iostream>
// using namespace std;

// class Person
// {
// public:
//   virtual void work()
//   { // virtual function allows polymorphism
//     cout << "Person is working" << endl;
//   }
// };

// class Student : public Person
// {
// public:
//   void work() override
//   { // overriding base method
//     cout << "Student is studying" << endl;
//   }
// };

// class Teacher : public Person
// {
// public:
//   void work() override
//   {
//     cout << "Teacher is teaching" << endl;
//   }
// };

// int main()
// {
//   Person *p; // Base class pointer

//   Student s;
//   Teacher t;

//   p = &s;
//   p->work(); // Output: Student is studying

//   p = &t;
//   p->work(); // Output: Teacher is teaching

//   return 0;

// }

// #include <iostream>
// using namespace std;

// template <class T>
// class Box
// {
//   T value;

// public:
//   void set(T val) { value = val; }
//   T get() { return value; }
// };

// int main()
// {
//   Box<int> intBox;
//   intBox.set(100);

//   Box<string> strBox;
//   strBox.set("Hello");

//   cout << intBox.get()<<" ";  // Output: 100
//   cout << strBox.get();       // Output: Hello

// }

#include <iostream>
using namespace std;

class Complex
{
    float real, imag;

public:
    Complex()
    {
        real = imag = 0;
    }

    Complex(float r, float i)
    {
        real = r;
        imag = i;
    }

    Complex operator+(const Complex &obj)
    {
        Complex result;
        result.real = real + obj.real;
        result.imag = imag + obj.imag;
        return result;
    }

    void display()
    {
        cout << real << " + " << imag << "i" << endl;
    }
};

int main()
{
    Complex c1(2.5, 3.5);
    Complex c2(1.5, 4.5);

    Complex sum = c1 + c2;

    cout << "Sum of complex numbers: ";
    sum.display();

    return 0;
}
