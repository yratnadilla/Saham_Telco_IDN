import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
import matplotlib.ticker as plticker

register_matplotlib_converters()

dfexcl = pd.read_csv('EXCL.csv', index_col='Date', parse_dates=['Date'])
dffren = pd.read_csv('FREN.csv', index_col='Date', parse_dates=['Date'])
dfisat = pd.read_csv('ISAT.csv', index_col='Date', parse_dates=['Date'])
dftlkm = pd.read_csv('TLKM.csv', index_col='Date', parse_dates=['Date'])

plt.style.use('seaborn')
plt.figure('Indonesian Telco Provider Stock March-June 2019')
plt.title('Indonesian Telco Provider Stock March-June 2019')

plt.plot(
    dfexcl.index, dfexcl['Close'],
    dffren.index, dffren['Close'],
    dfisat.index, dfisat['Close'],
    dftlkm.index, dftlkm['Close']
)

plt.xticks(rotation= 60)
plt.xlabel('Date')
plt.ylabel('IDR')
plt.legend(['PT XL Axiata Tbk', 'PT Smartfren Telecom Tbk', 'PT Indosat Tbk', 'PT Telekomunikasi Indonesia Tbk'],
    loc='center left', bbox_to_anchor=(1.0, 0.5))

plt.subplots_adjust(right=0.8, left=0.08)
plt.show()