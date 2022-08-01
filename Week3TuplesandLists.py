#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 16:46:56 2022

@author: toyyeebahmustapha
"""

import math

te = ()
t = (2,'one', 3)
t[0]

 = (1, 2, 3)

t[0]
Out[78]: 1

(2,"one",3)+(5,6)
Out[79]: (2, 'one', 3, 5, 6)

t[1:2]
Out[80]: (2,)

t[1:3]
Out[81]: (2, 3)

t[1] = 4
Traceback (most recent call last):

  File "<ipython-input-82-87b0f225887f>", line 1, in <module>
    t[1] = 4

TypeError: 'tuple' object does not support item assignment

#%%%%%%%%%%
""
#1. TUPLES

def quotient_and_remainder(x, y):
    q = x//y
    r = x%y 
    return (q, r)
(quot, rem) = quotient_and_remainder(4,5)

#2. Example of tuple (Did not run properly)

def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],) 
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return (min_nums, max_nums, unique_words)

(small, large, words) = get_data((1, 'mine'),
                                 (2, 'yours'), 
                                 (3, 'ours'), 
                                 (4, 'theirs'))

#3.OPERATIONS ON LISTS - ADD 

L1 = [2,1,3]
L2 = [4,5,6] #Here, L3 = [2, 1, 3, 4, 5, 6]
L1.extend([0,6])
L3 = L1 + L2 # here, L3 = [2, 1, 3, 0, 6, 4, 5, 6]

#4. PRINT IS NOT ==
cool = ['blue', 'green', 'grey'] 
chill = ['blue', 'green', 'grey'] 
print(cool)
print(chill)

chill[2] = 'blue'
print(chill)
print(cool)


#5. ALIASES

a=1 
b=a 
print(a) 
print(b)
warm = ['red', 'yellow', 'orange'] 
hot = warm
hot.append('pink')
print(hot)
print(warm)

#6. CLONING A LIST

cool = [‘blue’, ‘green’, ‘grey’] c
hill = cool[:]
chill.append(‘black’)
print(chill)
print(cool)

#7. SORTING LISTS

warm = [‘red’, ‘yellow’, ‘orange’] 
sortedwarm = warm.sort() 
print(warm)
print(sortedwarm)
cool = [‘grey’, ‘green’, ‘blue’] 
sortedcool = sorted(cool) 
print(cool)
print(sortedcool)

#8. LISTS OF LISTS OF LISTS OF....

warm = [‘yellow’, ‘orange’] 
hot = [‘red’]
brightcolors = [warm]
brightcolors.append(hot)
print(brightcolors)
hot.append(‘pink’)
print(hot)
print(brightcolors)
print(hot + warm)
print(hot)

#9. MUTATION AND ITERATION

def remove_dups_new(L1, L2): 
    L1_copy = [:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)

FUNCTIONS AS OBJECTS, DICTIONARIES
#10. FUNCTIONS AS OBJECTS
#Example 1:

def applyToEach(L, f):
#assumes L is a list, f a function mutates L by replacing each element, 
e, of L by f(e)
    for i in range(len(L)): 
        L[i] = f(L[i])
        
#Example 2:
def applyToEach(L, f):
for i in range(len(L)):
        L[i] = f(L[i])
 
applyToEach(L, abs) #absolute value
applyToEach(L, int) #integer
applyToEach(L, fact) #factorial
applyToEach(L, fib)  #fibonacci
L = [1, -2, 3.4]

#11. GENERALIZATION OF HOPS

#12. DICTIONARIES: HOW TO STORE STUDENT INFO

names = ['Ana', 'John', 'Denise', 'Katy'] 
grade = ['B', 'A+', 'A', 'A']
course = [2.00, 6.0001, 20.002, 9.01]

def get_grade(student, name_list, grade_list, course_list): 
    i = name_list.index(student)
    grade = grade_list[i]
    course = course_list[i]
    return (course, grade) 

#13. First Dictionary

my_dict = {}
grades = {'Ana':'B', 'John':'A+', 'Denise':'A', 'Katy':'A'}

#14. CREATING & USING A DICTIONARY
def most_common_words(freqs): 
    values = freqs.values() 
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k) 
            return (words, best)

def lyrics_to_frequencies(lyrics): 
    myDict = {}
    for word in lyrics:
        if word in myDict:
           myDict[word] += 1 
        else:
           myDict[word] = 1
           return myDict

def words_often(freqs, minTimes): 
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs) 
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
            return result
#print(words_often(beatles, 5))

#15. FIBONACCI RECURSIVE CODE & 
#INEFFICIENT FIBONACCI [fib(n) = fib(n-1) + fib(n-2)]


def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)
    
def fib_efficient(n, d): 
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d) 
        d[n] = ans
        return ans
    
d = {1:1, 2:2} 
print(fib_efficient(6, d))
argToUse = 50
print("")
print('using fib')
print(fib(argToUse))
print("")
print('using_fib_coefficient')
print(fib_efficient(argToUse, d))

#16. TRACKING EFFICIENCY: GLOBAL VARIABLES

def fib(n):
    global numFibCalls 
    numFibCalls += 1 
    if n == 1:
        return 1 
    elif n == 2: 
        return 2
    else:
        return fib(n-1)+fib(n-2)

def fibef(n, d): 
    global numFibCalls 
    numFibCalls += 1 
    if n in d:
        return d[n]
    else:
        ans = fibef(n-1,d)+fibef(n-2,d)
        d[n] = ans
        return ans

numFibCalls = 0

print(fib(12))
print('function calls', numFibCalls)

numFibCalls = 0

d = {1:1, 2:2} 
print(fibef(12, d)) 
print('function calls', numFibCalls)





































