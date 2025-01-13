Swift doesn't have identation, u hv to do it urself.
Code written at global scope is used as the entry point for the program, so you don’t need a main() function.
Let for consts and var for variables
If the initial value doesn’t provide enough information (or if there isn’t an initial value), specify the type by writing it after the variable, separated by a colon.
```swift
let implicitInteger = 70
let implicitDouble = 70.0
let explicitDouble: Double = 70
```
Values are never implicitly converted to another type. If you need to convert a value to a different type, explicitly make an instance of the desired type.
```swift
let label = "The width is "
let width = 94
let widthLabel = label + String(width)
```
Strings are somehow str types while classes are reference types.

UIKit is a framework that provides the necessary infrastructure for constructing and managing the user interface of iOS applications.


To run: 
``` bash
swiftc hello.swift; .\hello.exe
```