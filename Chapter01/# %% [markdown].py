# %% [markdown]
# # Python Algorithmic Trading Cookbook

# %% [markdown]
# ## Chapter 1: Handling and Manipulating Date, Time and Time Series Data

# %% [markdown]
# This Jupyter Notebook is created using Python version 3.8.2

# %% [markdown]
# ----

# %% [markdown]
# ### Requirements

# %% [markdown]
# You can install the requirements for this Jupyter Notebook by executing the below cell

# %%
!pip install pandas

# %% [markdown]
# ----

# %% [markdown]
# ### Recipe 1:  Creating datetime objects 

# %%
from datetime import datetime

# %%
dt1 = datetime.now()
print(f'Approach #1: {dt1}')

# %%
print(f'Year: {dt1.year}')
print(f'Month: {dt1.month}')
print(f'Day: {dt1.day}')
print(f'Hours: {dt1.hour}')
print(f'Minutes: {dt1.minute}')
print(f'Seconds: {dt1.second}')
print(f'Microseconds: {dt1.microsecond}')
print(f'Timezone: {dt1.tzinfo}')

# %%
dt2 = datetime(year=2021, month=1, day=1)
print(f'Approach #2: {dt2}')

# %%
print(f'Year: {dt2.year}')
print(f'Month: {dt2.month}')
print(f'Day: {dt2.day}')
print(f'Hours: {dt2.hour}')
print(f'Minutes: {dt2.minute}')
print(f'Seconds: {dt2.second}')
print(f'Microseconds: {dt2.microsecond}')
print(f'Timezone: {dt2.tzinfo}')

# %% [markdown]
# ### There's more...

# %%
print(f"Date: {dt1.date()}")
print(f"Type: {type(dt1.date())}")

# %%
print(f"Time: {dt1.time()}")
print(f"Type: {type(dt1.time())}")

# %%
print(f"Date: {dt2.date()}")
print(f"Type: {type(dt2.date())}")

# %%
print(f"Time: {dt2.time()}")
print(f"Type: {type(dt2.time())}")

# %% [markdown]
# ### Recipe 2: Creating timedetla objects

# %%
from datetime import timedelta

# %%
td1 = timedelta(days=5)
print(f'Time difference: {td1}')

# %%
td2 = timedelta(days=4)
print(f'Time difference: {td2}')

# %%
print(f'Addition: {td1} + {td2} = {td1 + td2}')

# %%
print(f'Subtraction: {td1} - {td2} = {td1 - td2}')

# %%
print(f'Multiplication: {td1} * 2.5 = {td1 * 2.5}')

# %% [markdown]
# ### There's more...

# %%
td3 = timedelta(hours=23, minutes=59, seconds=60)
print(f'Time difference: {td3}')

# %%
print(f'Total seconds in 1 day: {td3.total_seconds()}')

# %% [markdown]
# ### Recipe 3: Operations on datetime objects

# %%
from datetime import date, datetime, timedelta

# %%
date_today = date.today()
print(f"Today's Date: {date_today}")

# %%
date_5days_later = date_today + timedelta(days=5)
print(f"Date 5 days later: {date_5days_later}")

# %%
date_5days_ago = date_today - timedelta(days=5)
print(f"Date 5 days ago: {date_5days_ago}")

# %%
date_5days_later > date_5days_ago

# %%
date_5days_later < date_5days_ago

# %%
date_5days_later > date_today > date_5days_ago

# %%
current_timestamp = datetime.now()

# %%
time_now = current_timestamp.time()
print(f"Time now: {time_now}")

# %%
time_5minutes_later = (current_timestamp + timedelta(minutes=5)).time()              # Note: operations are not allowed on time objects, so have to perform on datetime objects and then extract the time
print(f"Time 5 minutes later: {time_5minutes_later}")

# %%
time_5minutes_ago = (current_timestamp - timedelta(minutes=5)).time()              # Note: operations are not allowed on time objects, so have to perform on datetime objects and then extract the time
print(f"Time 5 minutes ago: {time_5minutes_ago}")

# %%
time_5minutes_later < time_5minutes_ago

# %%
time_5minutes_later > time_5minutes_ago

# %%
time_5minutes_later > time_now > time_5minutes_ago

# %% [markdown]
# ### Recipe 4: Modifying datetime objects

# %%
from datetime import datetime

# %%
dt1 = datetime.now()
print(dt1)

# %%
dt2 = dt1.replace(year=2021, month=1, day=1)
print(f'A timestamp from 1st January 2021: {dt2}')

# %%
dt3 = datetime(year=2021, 
               month=1, 
               day=1, 
               hour=dt1.hour, 
               minute=dt1.minute, 
               second=dt1.second, 
               microsecond=dt1.microsecond, 
               tzinfo=dt1.tzinfo)
print(f'A timestamp from 1st January 2021: {dt3}')

# %%
dt2 == dt3

# %% [markdown]
# ### Recipe 5: Converting a datetime object to a string

# %%
from datetime import datetime

# %%
now = datetime.now().astimezone()

# %%
print(str(now))

# %%
print(now.strftime("%d-%m-%Y %H:%M:%S %z"))

# %% [markdown]
# ### Recipe 6: Creating a datetime object from a string

# %%
from datetime import datetime

# %%
now_str = '13-1-2021 15:53:39 +05:30'

# %%
now = datetime.strptime(now_str, "%d-%m-%Y %H:%M:%S %z")
print(now)

# %%
print(type(now))

# %% [markdown]
# ### There's more...

# %%
now = datetime.strptime(now_str, "%d-%m-%Y")
# Note: It's expected to get an error below

# %% [markdown]
# ### Recipe 7: The datetime object and time zones

# %%
from datetime import datetime

# %%
now_tz_naive = datetime.now()                   # Timezone naive datetime object
print(now_tz_naive)

# %%
print(now_tz_naive.tzinfo)

# %%
now_tz_aware = datetime.now().astimezone()      # Timezone aware datetime object
print(now_tz_aware)

# %%
print(now_tz_aware.tzinfo)

# %%
new_tz_aware = now_tz_naive.replace(tzinfo=now_tz_aware.tzinfo)
print(new_tz_aware)

# %%
print(new_tz_aware.tzinfo)

# %%
new_tz_naive = new_tz_aware.replace(tzinfo=None)
print(new_tz_naive)

# %%
print(new_tz_naive.tzinfo)

# %% [markdown]
# ### There's more...

# %%
new_tz_naive <= now_tz_naive

# %%
new_tz_aware <= now_tz_aware

# %%
new_tz_aware <= now_tz_naive
# Note: It's expected to get an error below

# %% [markdown]
# ### Recipe 8: Creating a Pandas.Dataframe object

# %%
from datetime import datetime
import pandas

# %%
time_series_data = [
    {'date': datetime(2019, 11, 13, 9, 0),
     'open': 71.8075,
     'high': 71.845,
     'low': 71.7775,
     'close': 71.7925,
     'volume': 219512},
    {'date': datetime(2019, 11, 13, 9, 15),
     'open': 71.7925,
     'high': 71.8,
     'low': 71.78,
     'close': 71.7925,
     'volume': 59252},
    {'date': datetime(2019, 11, 13, 9, 30),
     'open': 71.7925,
     'high': 71.8125,
     'low': 71.76,
     'close': 71.7625,
     'volume': 57187},
    {'date': datetime(2019, 11, 13, 9, 45),
     'open': 71.76,
     'high': 71.765,
     'low': 71.735,
     'close': 71.7425,
     'volume': 43048},
    {'date': datetime(2019, 11, 13, 10, 0),
     'open': 71.7425,
     'high': 71.78,
     'low': 71.7425,
     'close': 71.7775,
     'volume': 45863},
    {'date': datetime(2019, 11, 13, 10, 15),
     'open': 71.775,
     'high': 71.8225,
     'low': 71.77,
     'close': 71.815,
     'volume': 42460},
    {'date': datetime(2019, 11, 13, 10, 30),
     'open': 71.815,
     'high': 71.83,
     'low': 71.7775,
     'close': 71.78,
     'volume': 62403},
    {'date': datetime(2019, 11, 13, 10, 45),
     'open': 71.775,
     'high': 71.7875,
     'low': 71.7475,
     'close': 71.7525,
     'volume': 34090},
    {'date': datetime(2019, 11, 13, 11, 0),
     'open': 71.7525,
     'high': 71.7825,
     'low': 71.7475,
     'close': 71.7625,
     'volume': 39320},
    {'date': datetime(2019, 11, 13, 11, 15),
     'open': 71.7625,
     'high': 71.7925,
     'low': 71.76,
     'close': 71.7875,
     'volume': 20190}
]

# %%
df = pandas.DataFrame(time_series_data)
df

# %%
df.columns.tolist()

# %%
pandas.DataFrame(time_series_data, 
    columns=['close', 'date', 'open', 'high', 'low', 'volume'])

# %% [markdown]
# ### There's more...

# %%
pandas.DataFrame(time_series_data, index=range(10, 20))

# %% [markdown]
# ### Recipes 9: Dataframe manipulation: renaming, rearranging, reversing, and slicing

# %%
df.rename(columns={'date':'timestamp'}, inplace=True)
df

# %%
df.reindex(columns=[
    'volume', 
    'close', 
    'timestamp', 
    'high', 
    'open', 
    'low'
])

# %%
df[::-1]

# %%
df['close']

# %%
df.iloc[0]

# %%
df.iloc[:2, :2]

# %% [markdown]
# ### There's more...

# %%
df.iloc[:, 4]

# %% [markdown]
# ### Recipes 10: Dataframe Manipulation: applying, sorting, iterating and concatenating

# %%
import pandas

# %%
df['timestamp'] = df['timestamp'].apply(
    lambda x: x.strftime("%d-%m-%Y %H:%M:%S"))
df

# %%
df.sort_values(by='close', ascending=True)

# %%
df.sort_values(by='open', ascending=False)

# %%
for _, row in df.iterrows():
    avg = (row['open'] + row['close'] + row['high'] + row['low'])/4
    print(f"Index: {_} | Average: {avg}")

# %%
for value in df.iloc[0]:
    print(value)

# %%
df_new = pandas.DataFrame([
    {'timestamp': datetime(2019, 11, 13, 11, 30),
     'open': 71.7875,
     'high': 71.8075,
     'low': 71.77,
     'close': 71.7925,
     'volume': 18655},
    {'timestamp': datetime(2019, 11, 13, 11, 45),
     'open': 71.7925,
     'high': 71.805,
     'low': 71.7625,
     'close': 71.7625,
     'volume': 25648},
    {'timestamp': datetime(2019, 11, 13, 12, 0),
     'open': 71.7625,
     'high': 71.805,
     'low': 71.75,
     'close': 71.785,
     'volume': 37300},
    {'timestamp': datetime(2019, 11, 13, 12, 15),
     'open': 71.785,
     'high': 71.7925,
     'low': 71.7575,
     'close': 71.7775,
     'volume': 15431},
    {'timestamp': datetime(2019, 11, 13, 12, 30),
     'open': 71.7775,
     'high': 71.795,
     'low': 71.7725,
     'close': 71.79,
     'volume': 5178}
])
df_new

# %%
pandas.concat([df, df_new]).reset_index(drop=True)

# %% [markdown]
# ### There's more...

# %%
import random

# %%
df1 = pandas.DataFrame([random.randint(1,100) for i in range(10)], 
                       columns=['open'])
df1

# %%
df2 = pandas.DataFrame([random.randint(1,100) for i in range(10)], 
                       columns=['close'])
df2

# %%
pandas.concat([df1, df2], axis=1)

# %% [markdown]
# ### Recipe 11: Converting a DataFrame into other formats

# %%
df.to_csv('dataframe.csv', index=False)

# %%
df.to_json()

# %%
df.to_pickle('df.pickle')

# %% [markdown]
# ### Recipe 12: Creating a DataFrame from other formats

# %%
pandas.read_csv('dataframe.csv')

# %%
pandas.read_json('{"timestamp":{"0":"13-11-2019 09:00:00","1":"13-11-2019 09:15:00","2":"13-11-2019 09:30:00","3":"13-11-2019 09:45:00","4":"13-11-2019 10:00:00","5":"13-11-2019 10:15:00","6":"13-11-2019 10:30:00","7":"13-11-2019 10:45:00","8":"13-11-2019 11:00:00","9":"13-11-2019 11:15:00"},"open":{"0":71.8075,"1":71.7925,"2":71.7925,"3":71.76,"4":71.7425,"5":71.775,"6":71.815,"7":71.775,"8":71.7525,"9":71.7625},"high":{"0":71.845,"1":71.8,"2":71.8125,"3":71.765,"4":71.78,"5":71.8225,"6":71.83,"7":71.7875,"8":71.7825,"9":71.7925},"low":{"0":71.7775,"1":71.78,"2":71.76,"3":71.735,"4":71.7425,"5":71.77,"6":71.7775,"7":71.7475,"8":71.7475,"9":71.76},"close":{"0":71.7925,"1":71.7925,"2":71.7625,"3":71.7425,"4":71.7775,"5":71.815,"6":71.78,"7":71.7525,"8":71.7625,"9":71.7875},"volume":{"0":219512,"1":59252,"2":57187,"3":43048,"4":45863,"5":42460,"6":62403,"7":34090,"8":39320,"9":20190}}')

# %%
pandas.read_pickle('df.pickle')


