import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

dfexcl = pd.read_csv('EXCL.csv', index_col='Date', parse_dates=['Date'])
dffren = pd.read_csv('FREN.csv', index_col='Date', parse_dates=['Date'])
dfisat = pd.read_csv('ISAT.csv', index_col='Date', parse_dates=['Date'])
dftlkm = pd.read_csv('TLKM.csv', index_col='Date', parse_dates=['Date'])


df1 = dfexcl['2019-04']['Close']
df2 = dffren['2019-04']['Close']
df3 = dfisat['2019-04']['Close']
df4 = dftlkm['2019-04']['Close']

plt.style.use('seaborn')
plt.figure('Indonesian Telco Provider Stock April 2019')
plt.title('Indonesian Telco Provider Stock April 2019')
plt.plot(
    df1.index, df1,
    df2.index, df2,
    df3.index, df3,
    df4.index, df4
)

plt.xticks(rotation= 60)
plt.xlabel('Date')
plt.ylabel('IDR')
plt.legend(['PT XL Axiata Tbk', 'PT Smartfren Telecom Tbk', 'PT Indosat Tbk', 'PT Telekomunikasi Indonesia Tbk'],
    loc='center left', bbox_to_anchor=(1.0, 0.5))

plt.subplots_adjust(right=0.8, left=0.08)
plt.show()