# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 15:08:40 2022

@author: Hasan
"""
from datetime import datetime
import time
start_time = time.process_time()
current_time = datetime.now().strftime("%H:%M:%S")
print("Start =", current_time)

def TimeCounter(e): return 'TIME TAKEN: ' + str(time.process_time() - e - start_time) + 's'
    
def Comb(Ref0):
    Comb0 = []
    for i in range(len(Ref0)):
        for j in range(len(Ref0)):
            if i < j:
                g = str(Ref0[i])+'-'+str(Ref0[j])
                Comb0.append(g)
    return Comb0
    

def OnlyNumb(string):
    string = list(string)
    word = [char for char in string] #split the string to each character
    w = [s for s in word if s.isdigit()] #keep the number
    new = ""
    for x in w:
        new += x
    
    return int(new)

def strip_n(f1):
    f2=[]
    for i in range(len(f1)):
        f1[i]=f1[i].rstrip('\r\n')
        f2.append(f1[i])
    return f2

def insert_n(f1):
    f2=[]
    for i in range(len(f1)):
        f2.append(f1[i])
        f2.append("\n")
    return f2

def split(word):
    return [char for char in word] #split a string into each word

def concat_list(list):
    result= ''
    for element in list:
        result += str(element)
    return result

def count_dups(nums): 
    element = []
    freque = []
    nums = sorted(nums)
    if not nums:
        return element,freque
    
    if len(nums) == 1:
        element.append(nums[0])
        freque.append(1)
    else:
        running_count = 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                running_count += 1
            else:
                freque.append(running_count)
                element.append(nums[i])
                running_count = 1
        freque.append(running_count)
        element.append(nums[i+1])
    return element,freque

def concat_dups(criteria,ele):
    element = []
    freque = []
    if not criteria:
        return element,freque
    
    if len(criteria) == 1:
        element.append(criteria[0])
        freque.append(ele[0])
    
    else:    
        running_count = ele[0]
        for i in range(len(criteria)-1):
            if criteria[i] == criteria[i+1]:
                running_count += ","+ele[i+1] #the original form is without str
            else:
                freque.append(running_count)
                element.append(criteria[i])
                running_count = ele[i+1]
    
        freque.append(running_count)
        element.append(criteria[i+1])
    return element,freque

def concat_dups_slash(criteria,ele):
    element = []
    freque = []
    if not criteria:
        return element,freque
    
    if len(criteria) == 1:
        element.append(criteria[0])
        freque.append(ele[0])
    
    else:    
        running_count = ele[0]
        for i in range(len(criteria)-1):
            if criteria[i] == criteria[i+1]:
                running_count += ","+ele[i+1] #the original form is without str
            else:
                freque.append(running_count)
                element.append(criteria[i])
                running_count = ele[i+1]
    
        freque.append(running_count)
        element.append(criteria[i+1])
    return element,freque

def sumsimilar(criteria,ele):
    element = []
    freque = []
    if not criteria:
        return element,freque
    if len(criteria) == 1:
        element.append(criteria[0])
        freque.append(ele[0])
    else:
        running_count = ele[0]
        for i in range(len(criteria)-1):
            if criteria[i] == criteria[i+1]:
                running_count += ele[i+1]
            else:
                freque.append(running_count)
                element.append(criteria[i])
                running_count = ele[i+1]
        
        freque.append(running_count)
        element.append(criteria[i+1])
    return element,freque