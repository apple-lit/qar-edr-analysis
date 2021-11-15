# %%

import datetime as dt
import matplotlib.ticker as ticker
from matplotlib.dates import DateFormatter
from matplotlib.dates import date2num
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# %%


def plt_edr(ymd):
    df = pd.read_csv('../python_data/csv2/' + str(ymd) +
                     '.csv', delimiter=',', encoding="shift_jis")
    # 先頭行を削除
    df = df.drop(df.index[0])
    # 不要な列を削除
    # df = df.drop(columns=['AC_TAIL1', 'AC_TAIL2',
    #              'AC_TAIL3', 'AC_TAIL4', 'DATECLKYR', 'DATECLKMON', 'DATECLKDAY', 'GMT_HR', 'GMT_SEC', 'RALTC', 'SAT', 'TAT', 'TAS', 'CAS', 'MACH', 'HEAD_MAG', 'HEAD_TRUE', 'TOTFW', 'LATG_C', 'LONG_C'])

    # %%
    df = df.fillna(0)
    df['ALT_diff'] = df['ALT_ADIRU'].astype(float).diff(-1)
    df['ALT_diff_Ave'] = df['ALT_diff'].rolling(
        10, center=True).mean().shift(-1)
    df['STDEV'] = df['ALT_diff_Ave'].rolling(10, center=True).std().shift(-1)
    df['V_a'] = df['WINDSPEED']**(2/3)
    w_1 = 0.1
    w_2 = 2
    constant = w_1**(-2/3) - w_2**(-2/3)

    df['denominator'] = np.sqrt(1.05 * df['V_a'] * constant)

    df['EDR'] = df['STDEV'] / df['denominator']
    df['Time'] = pd.to_datetime(df['Time'], format="%H:%M:%S")
    print(df)

    fig = plt.figure(dpi=300)
    ax = fig.add_subplot()
    ax.plot(df['Time'], df['EDR'], 'o-', lw=1, ms=0.1, color='r')
    new_xticks = date2num(
        [df['Time'].iloc[0] + dt.timedelta(minutes=60*x) for x in range(len(df)//1800)])
    ax.xaxis.set_major_locator(ticker.FixedLocator(new_xticks))
    ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))
    ax.tick_params(axis='x', rotation=30)
    plt.savefig('./' + str(ymd) + '.png')


plt_edr(20170910)
# %%
