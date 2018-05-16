# -*- coding: utf-8 -*-
"""
Created on Wed May 16 10:37:50 2018

@author: co-op1
"""

from tkinter import filedialog
from tkinter import Tk
from import_excel import sheet_data_frame
#import pandas as pd
#from pandas import Timestamp
#from pandas import DataFrame



root = Tk()
root.deiconify()

path = filedialog.askopenfilename(
        filetypes=[('XLSX', '*.xlsx')],
        title='Select the .xlsx file containing the desired constraint data')

if path == '':
    root.destroy()

excel_file_df = sheet_data_frame(path)

# store size of data frame for later
rowcol = excel_file_df.shape

string_df = str(excel_file_df.to_dict()).replace(" nan", " float('nan')")

string_df = string_df.replace('{', '[')
string_df = string_df.replace('}', ']')
string_df = string_df.replace('[','{', 1)
string_df = string_df[::-1]
string_df = string_df.replace(']','}', 1)
string_df = string_df[::-1]

# need to change the 200 hard code in the future
for i in range(0,rowcol[0] + 1):
    string_df = string_df.replace( '[' + str(i) + ': ', '[')
    string_df = string_df.replace( ', ' + str(i) + ': ', ', ')
#    string_df = string_df.replace( ", " + str(i) + ":''", ", ''")
#    string_df = string_df.replace("[" + str(i) + ":''", "[''")
#    string_df = string_df.replace('Timestamp', 'parser.parse')
#    string_df = string_df.replace("''", ')


# this will output to a file once I'm done
#print(string_df)
    
n = string_df.count('],')
    
line_string = string_df.split('],', n)

file = open('constraints_dict.txt', 'w+')
for i in range(0, len(line_string)):
#    string1.append('\n')
    
    file.write(line_string[i] + '],\n')

file.close()
    
line_string = ''.join(line_string)
    

root.destroy()
