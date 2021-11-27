def temporal_cycles(date):
    from math import sin, cos, pi
    import pandas as pd
    d = pd.to_datetime(date)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Correct to start at 0
    day = d.day - 1
    month = d.month - 1
    dayofyear = d.dayofyear - 1
    return {
        'yearmonth_sin': sin(2*pi*(month/12)),
        'yearmonth_cos': cos(2*pi*(month/12)),
        'monthday_sin': sin(2*pi*(day/days_in_month[month])),
        'monthday_cos': cos(2*pi*(day/days_in_month[month])),
        'weekday_sin': sin(2*pi*(d.weekday()/7)),
        'weekday_cos': cos(2*pi*(d.weekday()/7)),
        'yearday_sin': sin(2*pi*(dayofyear/365)),
        'yearday_cos': cos(2*pi*(dayofyear/365)),
        'hour_sin': sin(2*pi*(d.hour/24)),
        'hour_cos': cos(2*pi*(d.hour/24)),
        'minute_sin': sin(2*pi*(d.minute/60)),
        'minute_cos': cos(2*pi*(d.minute/60)),
        'second_sin': sin(2*pi*(d.second/60)),
        'second_cos': cos(2*pi*(d.second/60)),
        }

# May be inefficient for large datasets
df['cycles'] = df.apply(lambda x: temporal_cycles(x[datetime_col]), axis = 1)
df = pd.concat([df.drop(['cycles'], axis = 1), df['cycles'].apply(pd.Series)], axis = 1)

# Alternative method
cycles = list(orders.apply(lambda x: temporal_cycles(x[datetime_col]), axis = 1))
cycles = {k: [dic[k] for dic in cycles] for k in cycles[0]}
for key in cycles.keys():
    df[key] = cycles.get(key)
