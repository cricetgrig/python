import pandas as pd
import numpy as np

#Part 1
df = pd.read_csv("mtesrl_20150626_MD0000600012_stats.txt", header = 1, skipfooter = 2, sep = "\t", usecols = ['EVENT', 'AVGTSMR'], engine='python')

stat = df.groupby('EVENT').AVGTSMR.agg([ lambda x: 'min = ' + str(x.min()), 
                                         lambda x: '50% = ' + str(round(x.median(),2)), 
                                         lambda x: '90% = ' + str(round(x.quantile(0.9),2)), 
                                         lambda x: '99% = ' + str(round(x.quantile(0.99),2)), 
                                         lambda x: '99.9% = ' + str(round(x.quantile(0.99),2))]).reset_index()
print(stat.to_csv(sep='\t', header = None, index = 0))

#Part 2
from tabulate import tabulate
def table(x):
    x = np.ceil(x/5)*5
    ExecTime, TransNo = np.unique(x, return_counts=True)
    Weight = TransNo*100/x.size
    Percent = np.cumsum(Weight)
    result = pd.DataFrame({'ExecTime': ExecTime, 'TransNo': TransNo, 'Weight%': Weight, 'Percent': Percent})
    return(result)

keys = df.EVENT.unique()
for key in keys:
    temp_group = df.groupby('EVENT').get_group(key)
    res = table(temp_group['AVGTSMR'].values)
    print(key)
    print(tabulate(res, headers='keys', tablefmt='fancy_grid', showindex=False))
