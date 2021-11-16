# %%

# -*- coding: utf-8 -*-
import datetime as dt
import matplotlib.ticker as ticker
from matplotlib.dates import DateFormatter
from matplotlib.dates import date2num
import matplotlib.pyplot as plt
import pandas as pd

# %%


def plt_edr(ymd):
    df = pd.read_csv('../python_data/csv/' + str(ymd) +
                     '.csv', delimiter=',', encoding="UTF-8", dtype={float: 'float64'})
    # 先頭行を削除
    df = df.drop(df.index[0])
    # 不要な列を削除
    # df = df.drop(columns=['Unnamed: ' + str(num)
    #              for num in range(6, 28) if num != 14])

    # df = df.drop(columns=['AC_TAIL1', 'AC_TAIL2',
    #              'AC_TAIL3', 'AC_TAIL4', 'DATECLKYR', 'DATECLKMON', 'DATECLKDAY', 'GMT_HR', 'GMT_SEC', 'RALTC', 'SAT', 'TAT', 'TAS', 'CAS', 'MACH', 'HEAD_MAG', 'HEAD_TRUE', 'TOTFW', 'LATG_C', 'LONG_C'])

    # NaNを0に置換
    df = df.fillna(0)
    # df['ALT_diff'] = df['ALT_ADIRU'].diff()

    # w_1 = 0.1
    # w_2 = 2
    # constant = (w_1 ** (-2/3)) - (w_2 ** (-2/3))

    # df['omega_diff'] = constant

    df['Time'] = pd.to_datetime(df['Time'], format="%H:%M:%S")
    print(df)

    fig = plt.figure(dpi=300)
    ax = fig.add_subplot()
    # ax.plot(df['Time'], df['EDR'], 'o-', lw=1, ms=0.1, color='r')
    ax.plot(df['Time'], df['WINDSPEED'], 'o-', lw=1, ms=0.1, color='b')
    new_xticks = date2num(
        [df['Time'].iloc[0] + dt.timedelta(minutes=60*x) for x in range(len(df)//1800)])
    ax.xaxis.set_major_locator(ticker.FixedLocator(new_xticks))
    ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))
    ax.tick_params(axis='x', rotation=30)
    plt.savefig('./' + str(ymd) + '.png')


# plt_edr(20170905)
# plt_edr(20170910)
# plt_edr(20170915)
# plt_edr(20170920)
# plt_edr(20171005)
plt_edr(20171010)
# %%
