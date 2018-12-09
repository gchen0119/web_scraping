def getCommodityPrice(start_date,end_date,commodity):
    df = pd.DataFrame.from_csv('./data/data.csv')
    mask = (df['date']>=start_date) & (df['date']<=end_date) # alternatively, df[df.some_date.between(start_date, end_date)]
    df = df.loc[mask]
    return commodity, df[commodity].mean(), df[commodity].std()
