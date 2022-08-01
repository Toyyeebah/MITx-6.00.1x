#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:18:08 2022

@author: toyyeebahmustapha
"""
import numpy

#LECTURE EXAMPLES

#1.

# x = 6
# if x != 5:
#   print('I am here')
# else:
#    print("no I am not")


#2.

#ans = 0
#neg_flag = False
#x = int(input("Enter an integer: "))
#if x < 0:
   # neg_flag = True
#while ans**2 < x:
 #   ans = ans + 1
#if ans**2 == x:
 #   print("Square root of", x, "is", ans)
#else:
 #   print(x, "is not a perfect square”)
  #  if neg_flag:
       # print("Just checking... did you mean", -x, "?”)
       
       
       
  #3.
     
#s = 'abcdefgh'
#for index in range(len(s)):
 #   if s[index] == 'i' or s[index] == 'u': 
  #      print ('There is an i or u”\')
#for char in s:
#if char == 'i' or char == 'u':
  #      print ('There is an i or u1)
  
  
  
  #4.
  
#an_letters = 'aefhilmnorsxAEFHILMNORSX'
#word = input("I will cheer for you! Enter a word: ") 
#times = int(input("Enthusiasm level (1-10): ")) 
#i=0

#while i < len(word):
#    char = word[i]
    #if char in an_letters:
   #     print("Give me an " + char + "! " + char)
   # else:
  #      print("Give me a " + char + "! " + char)
  #  i += 1
#print('What does that spell?') 
#for i in range(times):
 #   print(word, '!!!')
 
 
 #5.
 
#cube = 27
#epsilon = 0.01
#guess = 0.0
#increment = 0.0001
#num_guesses = 0
#while abs(guess**3 - cube) >= epsilon: 
  #  and guess <= cube:
 #   guess += increment
#    num_guesses += 1 
#print('num_guesses =', num_guesses) 
#if abs(guess**3 - cube) >= epsilon:
 #   print('Failed on cube root of', cube) 
#else:
#    print(guess, 'is close to the cube root of', cube)



#6. 

#x = 25
#epsilon = 0.01
#numGuesses = 0
#low = 1.0
#high = x
#ans = (high + low)/2.0

#while abs(ans**2 - x) >= epsilon:
   # print('low =' + str(low) + 'high =' + str(high) + 'ans =' + str(ans)) 
   # numGuesses += 1
  #  if ans**2 < x:
   #     low = ans
  #  else:
    #    high = ans
   # ans = (high + low)/2.0
#print('numGuesses = ' + str(numGuesses))
#print(str(ans) + ' is close to square root of ' + str(x))
  

#7.

#cube = 27
#epsilon = 0.01
#num_guesses = 0
#low = 1
#high = cube
#guess = (high + low)/2.0
#while abs(guess**3 - cube) >= epsilon:
 #   if guess**3 < cube :
 #       low = guess
#    else:
#        high = guess
#    guess = (high + low)/2.0
#    num_guesses += 1
#print('num_guesses =', num_guesses)
#print(guess, 'is close to the cube root of', cube)


#8.

#if num < 0:
#    isNeg = True
 #   num = abs(num)
#else:
 #   isNeg = False 
#result = ''
#if num == 0:
#    result = ‘0’
#while num > 0:
#    result = str(num%2) + result 
#    num = num//2
#if isNeg:
#    result = ‘-’ + result

#9. (problwm set 0, assignments)

#x = int(input ('Enter number x:'))
#y = int(input ('Enter number y:'))
#print (x**y)
#print(numpy.log2(x))

#10. (Binary representation)

#x = float(input('Enter a decimal number between 0 and 1: '))

#p=0
#while ((2**p)*x)%1 != 0:
  #  print('Remainder = ' + str((2**p)*x - int((2**p)*x)))
    #   p += 1
  
#num = int(x*(2**p))

#result = '' 
#if num == 0:
#    result = '0'
#while num > 0:
#    result = str(num%2) + result 
#    num = num//2
#for i in range(p - len(result)): 
 #   result = '0' + result

#result = result[0:-p] + '.' + result[-p:]
#print('The binary representation of the decimal ' + str(x) + ' is ' + str(result))

#11. [Newton Raphson]

#epsilon = 0.01 
#y = 24.0 
#numGuesses = 0

#while abs(guess*guess - y) >= epsilon: 
 #   numGuesses += 1
#    guess = guess - (((guess**2) - y)/(2*guess)) 
#print('numGuesses = ' + str(numGuesses))
#print('Square root of ' + str(y) + ' is about ' + str(guess))

#12. [writing a function]

#def is_even(i):
 #   """
 #   Input: i, a positive int
 #   Returns True if i is even, otherwise False
 #   """ 
 #   print('hi')
  #  return i%2 == 0 
#is_even(3)

#13. Variable scope

#def f( x ): 
 #   x = x + 1
#    print('in f(x): x =', x)
#    return x 
#x = 3
#z = f( x )

#14. If no "return" statement

#def is_even( i ):
#    """
#    Input: i, a positive int 
#    Does not return anything 
#    """
#    i % 2 == 0

#15. functions as arguments

#def func_a():
 #   print('inside func_a')
#def func_b(y):
#    print('inside func_b')
#    return y
#def func_c(z): 
#    print('inside func_c') 
#    return z()
#print(func_a())
#print(5 + func_b(2))
#print(func_c(func_a))

#16. scope details

#def g(x):
#    def h():
#        x = 'abc' 
#    x = x + 1
#    print('in g(x): x =', x) 
#    h()
#    return x
#x = 3
#z = g(x)
  
#17.  KEYWORD ARGUMENTS AND DEFAULT VALUES
#def printName(firstName, lastName, reverse):
#    if reverse:
#        print(lastName + ', ' + firstName) 
#    else:
#        print(firstName, lastName)
#
#printName('Eric', 'Grimson', False)
#printName('Eric', 'Grimson', reverse = False)
#printName('Eric', lastName = 'Grimson', reverse = False)
#printName(lastName = 'Grimson', firstName = 'Eric', reverse = False)
#
#def printName(firstName, lastName, reverse = False): 
#    if reverse:
#        print(lastName + ',' + firstName)
#    else:
#        print(firstName, lastName)
#     
#printName('Eric', 'Grimson')
#printName('Eric', 'Grimson', True)

#18. Specification

#def is_even( i ):
 #   """
 #   Input: i, a positive int
 #   Returns True if i is even, otherwise False 
 #   """
 #   print ("hi")
 #   return i%2 == 0
#is_even(3)

#19. MULTIPLICATION – ITERATIVE SOLUTION
#def mult_iter(a, b):
  #  result = 0
  #  while b > 0:
  #      result += a
  #      b -= 1
  #  return result
  
 #20.MULTIPLICATION – RECURSIVE SOLUTION
#def mult(a, b):
#    if b == 1:
#        return a 
#    else:
#        return a + mult(a, b-1)

#21. FACTORIAL
#def fact(n):
#    if n == 1:
#        return 1 
#    else:
#        return n*fact(n-1)
#print(fact(12))

#22. INDUCTIVE REASONING

#def mult_iter(a, b): 
#    result = 0
#    while b > 0: 
#        result += a
#        b -= 1
#    return result

#def mult(a, b):
#    if b == 1:
#        return a
#    else:
#        return a + mult(a, b-1)

#23. MATHEMATICAL INDUCTION

# INDUCTIVE REASONING
#def printMove(fr, to):
#    print('move from ' + str(fr) + ' to ' + str(to))
#def Towers(n, fr, to, spare): 
#    if n == 1:
#        printMove(fr, to) 
#    else:
#        Towers(n-1, fr, spare, to) 
#        Towers(1, fr, to, spare) 
#        Towers(n-1, spare, to, fr)
#print(Towers(4,'P1','P2','P3'))

#24. FIBONACCI
#def fib(x):
#        """assumes x an int >= 0
#        returns Fibonacci of x"""
#        if x == 0 or x == 1: 
#            return 1
#        else:
#            return fib(x-1) + fib(x-2)

#25. RECURSION ON NON-NUMERICS
#palindrome check
#def isPalindrome(s):
#    def toChars(s):
#        s = s.lower()
#        ans = '' 
#        for c in s:
#            if c in 'abcdefghijklmnopqrstuvwxyz':
#                ans = ans + c
#        return ans
#    def isPal(s):
#        if len(s) <= 1:
#            return True
#        else:
#            return s[0] == s[-1] and isPal(s[1:-1])
#    return isPal(toChars(s))
#print('')
#print('Able was I')
#print(isPalindrome('eve'))

#print('')
#print('Is able was I ere I saw Elba a palindrome?')
#print(isPalindrome('Able was I, ere I saw Elba'))

#26. Grader 

import math
def polysum(n,s):
    '''
    Input: n - number of sides(should be an integer)
    s- length of each sides(can be an intger or a float)
    
    Output: Returns Sum of area and the square of the perimeter of the regular polygon(gives a float)
    '''
    #Code
    def areaOfPolygon(n,s):
        #Pi = 3.1428
        area = (0.25 * n * s ** 2)/math.tan(math.pi/n)
        return area
    def perimeterOfPolygon(n,s):
        perimeter = n * s
        return perimeter
    sum = areaOfPolygon(n,s) + (perimeterOfPolygon(n,s) ** 2)
    return round(sum,4)
polysum(3,4)
#25.  Files: Example 
#nameHandle = open ('kids', 'w') 
#for i in range(2):
#    name = input('Enter name: ')
#    nameHandle.write(name + '/' )
#nameHandle.close()

#26.  Files: Example 2
#nameHandle = open('kids', 'r') 
#for line in nameHandle:
#    print(line)
#nameHandle.close()

#27.  















