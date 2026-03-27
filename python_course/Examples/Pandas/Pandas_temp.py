import pandas as pd

df = pd.DataFrame()

#example: "date" column in strings → datetime
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

#generating a series of dates
date_range = pd.date_range(start='2021-01-01', periods=10, freq='M')

#or to create an index
df.index = pd.to_datetime(df['date'])

#resampling time series data
df_resampled = df.resample('M').mean()
print(df_resampled)

#starting from a DataFrame with DatetimeIndex:
#daily average
df_daily = df.resample('D').mean()      
#monthly sum
df_monthly = df.resample('M').sum()

#adds a column with the previous day's value
df['prev_day'] = df['value'].shift(1)

#daily rate of change
#equivalent to shift + % calculation
df['daily_return'] = df['value'].pct_change()  

#7-day rolling window: mean and standard deviation
df['rolling_mean7'] = df['value'].rolling(window=7).mean()
df['rolling_std7']  = df['value'].rolling(window=7).std()
