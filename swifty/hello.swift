// 1. Print hello in Swift
// // print("Hello, Swift in VS Code!")
// let label = "The width is "
// let width = 94
// let length: Int = 120
// let widthLabel = label + String(width)
// // print(widthLabel)
// let areaLabel: String = "The area is \(width + length)."
// // print(areaLabel)

//Playgrounds help see changes live

import Foundation
// Foundation is a separate framework that includes all swift core functionality
// 2. var vs let
// var myName = "Edwige"
// var herName = "Audrey"
// var names = [myName, herName]
// names.append("David")
// // print(names)

// 3. mutabality & immutability
// let oldArray = NSMutableArray(
//     array: [
//         "Foo",
//         "Bar"
//     ]
// )
// oldArray.add("Baz")
// var newArray = oldArray
// oldArray.add("Quix")
// // print(oldArray)

// 4. Operators

/// 4.1 Unary prefixes
// let test1 = !true

/// 4.2 Unary postfixes
// let name = Optional("Joella")
// // print(type(of: name))
// let unaryPostfix = name!
// // print(type(of: unaryPostfix))

/// 4.3 Binary infix
// let myNames = "Akuzwe" + "Sheja" + "Edwige"
// // print(myNames)

/// 4.2 Ternary operator
// let age = 17
// let approval = age > 18 
//     ? "Welcome!!" 
//     : "You're not allowed here"
// // print(approval)

// 5. If-Else
// let myName = "Ediwge"
// let myAge = 17
// let yourName = "Joella"
// let yourAge = 18

// if (myName == "Sheja" && yourName == "Iriza" && yourAge == 20 || myAge == 17) {
//         print("myName, yourName, yourAge might not be what was given but the `||` is at the end so terminates everything.")
//     } else {
//         print("myAge yields false too.")
//     }

// import UIKit
// 6. Funcs
// func noArgsNoReturnVal () {
//     print("I do not know wat am doing!")
// }
// noArgsNoReturnVal()

// @discardableResult
// func plusTwo (value: Int) -> Int {
//     value + 2 //return is Optional
// }
// plusTwo(value: 2)

// func customFunc (value1: Int, value2: Int) -> Int {
//     value1 + value2
// }
// let customAdded = customFunc(value1: 20, value2: 12)
// print(customAdded)

// // Types of args: Internal & external
// func customMinus (_ lhs: Int, _ rhs: Int) -> Int { 
//     // the _ means externally it doesn't need a notation as lhs is internal name
//     lhs - rhs
// }
// let customSubtracted = customMinus(20, 15)
// print(customSubtracted)



