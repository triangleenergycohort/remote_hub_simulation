# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 12:57:25 2018

@author: dvsto
"""
import re
    
def re_extract(pattern,text):
    m = re.search(pattern,text)
    if m:
        return m.group()