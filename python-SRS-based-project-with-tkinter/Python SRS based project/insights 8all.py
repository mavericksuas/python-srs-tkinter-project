# -*- coding: utf-8 -*-
"""
Created on Sun Oct 4 02:13:46 2020

@author: UPMANYU JChilliwack
"""

from tkinter import*
from tkinter import ttk
import tkinter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np



df8 = pd.DataFrame()

#\\
for f in ["C:\\Users\\Upmanyu\\Desktop\\Python SRS based project(Internship)\\data by client\\ccaedfproperty.xlsx"]:
    excel_data_df8 = pd.read_excel(f,"Page1_1",header=8)
    df8 = pd.DataFrame(excel_data_df8, columns= ['Latitude','Longitude'])
    products_list = df8.values.tolist()
    #print (products_list[0])
    #print(df8.head(0))
    #print(df8)
    #print(df8.index)
df8.plot()
plt.show()