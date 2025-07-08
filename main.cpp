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

#include <iostream>
using namespace std;

template <class T>
class Box
{
  T value;

public:
  void set(T val) { value = val; }
  T get() { return value; }
};

int main()
{
  Box<int> intBox;
  intBox.set(100);

  Box<string> strBox;
  strBox.set("Hello");

  cout << intBox.get()<<" ";  // Output: 100
  cout << strBox.get();       // Output: Hello
  
}
