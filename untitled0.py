#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 16:24:37 2022

@author: lisiyang
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression

data = pd.read_csv("shots_data.csv")
A = data.iloc[0:280]
B = data.iloc[280::]
APT2 = []
ANC3 = []
AC3 = []
for i in range(280):
    if A.iloc[i]["y"] <= 7.8:
        if A.iloc[i]["x"] < -22 or A.iloc[i]["x"] > 22:
            AC3.append(A.iloc[i]["fgmade"])
        else:
            APT2.append(A.iloc[i]["fgmade"])
    elif A.iloc[i]["y"] > 7.8:
        if (A.iloc[i]["x"])**2 + (A.iloc[i]["y"])**2 > 23.75**2:
            ANC3.append(A.iloc[i]["fgmade"])
        else:
            APT2.append(A.iloc[i]["fgmade"])
    else:
        APT2.append(A.iloc[i]["fgmade"])
AFG2 = sum(APT2)/len(APT2)
AFGNC3 = sum(ANC3)/len(ANC3)
AFGC3 = sum(AC3)/len(AC3)
print(AFG2)
print(AFGNC3)
print(AFGC3)
AeFG2 = sum(APT2)/len(APT2)
AeFGNC3 = 1.5*sum(ANC3)/len(ANC3)
AeFGC3 = 1.5*sum(AC3)/len(AC3)
print(AeFG2)
print(AeFGNC3)
print(AeFGC3)
BPT2 = []
BNC3 = []
BC3 = []
for i in range(224):
    if B.iloc[i]["y"] <= 7.8:
        if B.iloc[i]["x"] < -22 or B.iloc[i]["x"] > 22:
            BC3.append(B.iloc[i]["fgmade"])
        else:
            BPT2.append(B.iloc[i]["fgmade"])
    elif B.iloc[i]["y"] > 7.8:
        if (B.iloc[i]["x"])**2 + (B.iloc[i]["y"])**2 > 23.75**2:
            BNC3.append(B.iloc[i]["fgmade"])
        else:
            BPT2.append(B.iloc[i]["fgmade"])
    else:
        BPT2.append(B.iloc[i]["fgmade"])
BPT2P = len(BPT2)/(len(BNC3) + len(BC3) + len(BPT2))
BNC3P = len(BNC3)/(len(BNC3) + len(BC3) + len(BPT2))
BC3P = len(BC3)/(len(BNC3) + len(BC3) + len(BPT2))
print(BPT2P)
print(BNC3P)
print(BC3P)
BFG2 = sum(BPT2)/len(BPT2)
BFGNC3= sum(BNC3)/len(BNC3)
BFGC3 = sum(BC3)/len(BC3)
print(BFG2)
print(BFGNC3)
print(BFGC3)
BeFG2 = sum(BPT2)/len(BPT2)
BeFGNC3 = 1.5*sum(BNC3)/len(BNC3)
BeFGC3 = 1.5*sum(BC3)/len(BC3)
print(BeFG2)
print(BeFGNC3)
print(BeFGC3)