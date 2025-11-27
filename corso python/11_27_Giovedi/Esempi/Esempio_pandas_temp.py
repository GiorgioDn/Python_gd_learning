import pandas as pd

df = pd.DataFrame()

#esempio: colonna “date” in stringhe → datetime
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

#generazione di una serie di date
date_range = pd.date_range(start='2021-01-01', periods=10, freq='M')

#oppure per creare un indice
df.index = pd.to_datetime(df['date'])

#gesampling dei dati di una serie temporale
df_resampled = df.resample('M').mean()
print(df_resampled)

#partendo da un DataFrame con indice DatetimeIndex:
#media giornaliera
df_daily = df.resample('D').mean()      
#somma mensile
df_monthly = df.resample('M').sum()

#aggiunge una colonna con il valore del giorno precedente
df['prev_day'] = df['value'].shift(1)

#tasso di variazione giornaliero
#equivalente a shift + calcolo %
df['daily_return'] = df['value'].pct_change()  

#finestra mobile di 7 giorni: media e deviazione standard
df['rolling_mean7'] = df['value'].rolling(window=7).mean()
df['rolling_std7']  = df['value'].rolling(window=7).std()

