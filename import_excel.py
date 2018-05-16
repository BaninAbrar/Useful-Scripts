# -*- coding: utf-8 -*-
"""
Created on Thu May  3 14:38:33 2018

@author: co-op4
"""

import pandas as pd
def sheet_data_frame(Location):
    df = pd.ExcelFile(Location)
    df_Assets = df.parse(1)
    return df_Assets
