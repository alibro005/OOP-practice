> > > > > > > > > > > OBJECT ORIENTED PROGRAMMING <<<<<<<<<

Class

> A class is a blue print for creating objects.

Objects

> An object is the current instance of the class.

---

Constructor

> A contructor is a function which is automatically invoked when the object is being created.

1.  Default Constructor
    >     No parameters.
    >     Used to assign default values.
2.  Parameterized Constructor
    >     Takes parameters to assign custom values during object creation.
3.  Copy Constructor (mainly in C++ and conceptually in Java/Python)
    > Creates a new object by copying another object's values.

---

Shallow Copy

> Copies the address.
> Both object use the same memory.
> If one changed it, the other also changed.

Deep Copy

> Creates a new memory.
> Each object has its own data.
> Safe too change one the other remains same.

---

Destructor

> A destructor is a special member function of a class that is automatically called when an object goes out of scope or is deleted.

---

Inheritance

> Inheritance allows a class (child) to inherit properties and behaviors from another class (parent).

1. Single Inheritance
2. Multi-level Inheritance
3. Multiple Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance

---

Encapsulation

> Wrapping up the data in single class Unit.

---

Polymorphism

> Polymorphism means "many forms" and it ocuurs when we have many classes that are related to each other by inheritance
> Same name but different usage and working.
> Enables a single function or method to have different meanings based on context
> Constructor Overloading

1. Compile time Polymorphism eg; Constructor Overloading , Method/Function Overloading (Statically)

2. Run time Polymorphism eg; Method/Function Overrinding (Dynamically) , Vitual function

---

Overiding (depends on inheritance)

> Parent and child both contain the same function with different implementation.
> Overriding means a child class redefines a method of its parent class with the same name, same parameters.

Where it is used:

> Occurs in inheritance (between base and derived classes).
> Purpose:
> To change or extend the behavior of a method in the derived class.

---

Overloading

> One class but multiple function inside it.
> Overloading means having multiple functions/methods with the same name but different parameters (number or type).

Where it is used:

> Occurs within the same class.
> Purpose:
> To perform similar operations in different ways.

Virtual Function

> A virtual function is a member function that you expect to redefined it in derived classes.

---

Abstraction

> Hides complex implementation details, showing only necessary functionalities

Abstract Class

> An abstract class is a class that cannot create objects.
> It is used to create a base class that sets rules for other classes.
> An abstract class is a base class that has at least one pure virtual function.
> A pure virtual function is a function with no body — only a declaration — written like this: virtual void show() = 0;

---

Static Keyword

> Static member variables are variables that are shared among all objects of a class. They are initialized only once and exist for the lifetime of the program, rather than the lifetime of the objects.
