# CS515-project2
Kavitha Siratla [ksiratla@stevens.edu](mailto:ksiratla@stevens.edu)
Rushiraj Herma [rherma@stevens.edu](mailto:rherma@stevens.edu)

# the URL of your public GitHub repo
https://github.com/kavitha-siratla/CS515-project2

# an estimate of how many hours you spent on the project
45 hours

# a description of how you tested your code

When implementing a basic calculator project, it's important to test the code thoroughly to ensure that it's functioning correctly. In this particular project, the first step was to implement a lexical analyzer (lex) to generate a token stream. The token stream was then fed to the parser to generate an abstract syntax tree (AST), which was used to create an interpreter that generated the output.

To test the code, we began by adding doctests to the individual functions to ensure that they were behaving as expected. This allowed us to test the individual components of the code before testing the entire project as a whole.

Once we were confident that each individual component was functioning correctly, we tested the project step by step. We started by testing the lexer. Instead of directly supplying input from a text file, we initially tested it with a variable and passed it to the lexer function, checking the output by printing it out to the console. This approach allowed us to identify any issues with the lexer's implementation and ensure that it was generating the desired output.

After verifying that the lexer was functioning correctly, we moved on to testing the parser and interpreter. We used a similar approach, passing input as a variable and checking the output by printing it out to the console. This helped us to ensure that the parser was generating the expected AST, and that the interpreter was correctly interpreting the AST to generate the desired output.

Finally, we tested the entire project by using a text file as input. This allowed us to ensure that the entire system was working as intended, and that there were no issues or bugs that had been missed during testing.


# bugs and issues
None 

# resolved issue
Faced an issue with print statement.

# Implemented extensions
# 1) Op-equals
The Op-equals extension is a feature that allows compound assignment operators to be used in a programming language. These operators combine a binary operator with an assignment operation, such as adding or subtracting a value to a variable. The Op-equals extension adds support for six compound assignment operators, which include +=, -=, *=, /=, %=, and ^=.

The meaning of these operators is straightforward: x op= e is equivalent to x = x op (e), where op is a binary operator, x is a variable, and e is an expression. For example, x += 1 is equivalent to x = x + 1. This means that the value of x is incremented by 1 and then assigned back to x. Similarly, x -= 1 would subtract 1 from the value of x and assign the result back to x.

The Op-equals extension simplifies code by allowing more concise expressions to be written. For example, instead of writing x = x + 1, one can write x += 1. This makes the code shorter and easier to read, especially in cases where the expression is long or complex. Additionally, using compound assignment operators can make the code more efficient since it eliminates the need to recompute the value of x on the right-hand side of the assignment.

In conclusion, the Op-equals extension is a useful feature that simplifies code and improves readability. It allows for the use of compound assignment operators, such as +=, -=, *=, /=, %=, and ^=, which can make expressions shorter and easier to read. By eliminating the need to recompute the value of a variable, this extension can also improve code efficiency.

# 2) Relational operations
The second extension, Relational operations, provides support for operators that allow comparisons between values. Relational operators include "==", "<=", ">=", "!=", "<", and ">". These operators are binary operators that return a boolean value of either 1 (true) or 0 (false) based on whether the comparison is true or false.

For example, if we have two variables a and b, and we want to compare if a is greater than b, we would write "a > b". If a is indeed greater than b, the expression would evaluate to 1, otherwise, it would evaluate to 0. Similarly, we could check if two variables are equal by using the "==" operator.

It's worth noting that these operators have lower precedence than arithmetic operators, meaning that arithmetic operations are performed before relational operations. For example, in the expression "3 + 4 < 7", the addition operation is performed first, and then the comparison operator "<" is applied to the result.

By providing support for relational operators, this extension allows programmers to create more complex conditional statements and logic in their code. For instance, they can use relational operators to compare user input with predefined values or to test the validity of a given condition.


# 3) Boolean operations
The Boolean operations extension allows the calculator to perform logical operations on expressions. The && (conjunction) operator returns 1 if both operands are non-zero and 0 otherwise. The || (disjunction) operator returns 1 if either operand is non-zero and 0 otherwise. The ! (negation) operator reverses the truth value of its operand.

In the example given, the code snippet "print 1 && 2, 2 && 1, -5 && 1, 0 && -100" uses the && operator to test various combinations of operands. The first two expressions both evaluate to 1 because both operands are non-zero. The third expression also evaluates to 1 because -5 is non-zero. The last expression evaluates to 0 because both operands are zero.

It's important to note that Boolean operators have lower precedence than arithmetic and relational operators. For example, the expression "5 + 4 > 6 && 2 * 3 == 6" will be evaluated as "(5 + 4) > 6 && (2 * 3) == 6" due to operator precedence rules. Additionally, the && and || operators are left associative, meaning that expressions are evaluated from left to right. Finally, the ! operator is non-associative, meaning that it can only operate on a single operand.

The Boolean operations extension allows for the creation of complex conditions and expressions in the calculator, enabling more advanced calculations and decision making.

# 4) Comments

The fourth extension, Multi-line comments and single-line comments, allows developers to add comments to their code. Multi-line comments begin with /* and end with */, and can span multiple lines of code. Arbitrary line breaks are allowed between the start and end of multi-line comments. For example,

/* This is a
multi-line comment
*/
Single-line comments begin with # and continue until the end of the line. They can be used anywhere in the code. For example,

x = 1  # this sets x to 1
Comments are not executed as part of the code and are purely for the benefit of the developer. They can be used to provide additional information about the code, such as why a particular approach was taken or to describe the purpose of a variable. This can improve code readability and help other developers understand the code. Additionally, comments can be used to temporarily remove or disable parts of the code for testing purposes, without actually deleting the code.