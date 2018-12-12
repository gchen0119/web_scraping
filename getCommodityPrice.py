# run this program in command line as
# Example:
# python getCommodityPrice 2018-11-07 2018-12-01 gold 


import sys
import pandas as pd
def getCommodityPrice():
    if len(sys.argv)!=4:
        raise ValueError("requires 3 input arguments, e.g., 2018-11-07 2018-12-01 gold")
    df = pd.read_csv('./data/data.csv')
    mask = (df['date']>=sys.argv[1]) & (df['date']<=sys.argv[2]) # alternatively, df[df.some_date.between(start_date, end_date)]
    if not any(mask): 
        raise ValueError("date out of range %s and %s" % (df['date'].iloc[-1],df['date'].iloc[0]))
    df = df.loc[mask]
    print(sys.argv[3], df[sys.argv[3]].mean(), df[sys.argv[3]].std())

if __name__ == '__main__': # if module executed directly, then run main()
    getCommodityPrice()
