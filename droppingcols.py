# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 19:38:14 2016

@author: keshavsivakumar
"""

import pandas as pd

# The entry point function can contain up to two input arguments:
#   Param<dataframe1>: a pandas.DataFrame
#   Param<dataframe2>: a pandas.DataFrame
def azureml_main(marksframe):
 drop_cols = ['Year']
 marksframe.drop(drop_cols, axis = 1, inplace = True)
 return marksframe
