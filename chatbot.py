import pandas as pd
import csv
import re

#load data
df = pd.read_csv('100kINC.csv')
print(df.columns.values)