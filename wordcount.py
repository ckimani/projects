#!/usr/bin/python
 # -*- coding: iso-8859-15 -*-
import os, sys


def words(str):  
    counts = dict()  
    word = str.split()  

     
    for char in word:  
        if char in counts:  
            counts[char] += 1 

        else:  
            counts[char] = 1  
  
    return counts  
  
print( words('olly olly : ¿Qué   in come free.')) 


