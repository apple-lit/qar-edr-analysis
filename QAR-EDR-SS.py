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
    df = pd.read_csv('../python_data/csv2/' + str(ymd) + '.csv',
                     delimiter=',', encoding="shift_jis")
    # 先頭行を削除
    df = df.drop(df.index[0])
    # 不要な列を削除
    # df = df.drop(columns=['AC_TAIL1', 'AC_TAIL2',
    #              'AC_TAIL3', 'AC_TAIL4', 'DATECLKYR', 'DATECLKMON', 'DATECLKDAY', 'GMT_HR', 'GMT_SEC', 'RALTC', 'SAT', 'TAT', 'TAS', 'CAS', 'MACH', 'HEAD_MAG', 'HEAD_TRUE', 'TOTFW', 'LATG_C', 'LONG_C'])

    df['ALT_diff'] = df['ALT_ADIRU'].astype('float64').diff(-1)
    df['ALT_diff_Ave'] = df['ALT_diff'].rolling(
        10, center=True).mean().shift(-1)
    df['STDEV'] = df['ALT_diff_Ave'].rolling(10, center=True).std().shift(-1)
    df['V_a'] = df['WINDSPEED'].astype('float64')**(2/3)
    w_1 = 0.1
    w_2 = 2
    constant = w_1**(-2/3) - w_2**(-2/3)
    df['denominator'] = np.sqrt(1.05 * df['V_a'] * constant)
    df['EDR'] = df['STDEV'] / df['denominator']
    df['Time'] = df['Time'].replace(' ', '', regex=True)
    df['Time'] = pd.to_datetime(df['Time'], format="%H:%M:%S")
    df = df.fillna(0)
    print(df)

    fig = plt.figure(dpi=300)
    ax = fig.add_subplot()
    ax.plot(df['Time'], df['EDR'], 'o-', lw=1, ms=0.1, color='r')
    # ax.plot(df['Time'], df['ALT_ADIRU'].astype(
    #     'float64'), 'o-', lw=1, ms=0.1, color='blue')
    # ax.plot(df['Time'], df['WINDSPEED'].astype(
    #     'float64'), 'o-', lw=1, ms=0.1, color='orange')
    ax.set_xlabel('Time')
    ax.set_ylabel('EDR')
    # ax.set_ylabel('Altitude [ft]')
    # ax.set_ylabel('Windspeed [kt]')
    fig.suptitle('EDR based on QAR data of ' + str(ymd))
    # fig.suptitle('Altitude based on QAR data of ' + str(ymd))
    # fig.suptitle('Windspeed based on QAR data of ' + str(ymd))
    new_xticks = date2num(
        [df['Time'].iloc[0] + dt.timedelta(minutes=60*x) for x in range(len(df)//1800)])
    ax.xaxis.set_major_locator(ticker.FixedLocator(new_xticks))
    ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))
    ax.tick_params(axis='x', rotation=30)
    plt.savefig('../python_data/EDR_fig/' + str(ymd) + '.png')
    # plt.savefig('../python_data/altitude_fig/' + str(ymd) + '.png')
    # plt.savefig('../python_data/windspeed_fig/' + str(ymd) + '.png')


plt_edr(20170910)
plt_edr(20170915)
plt_edr(20170920)
plt_edr(20170925)
plt_edr(20171005)
plt_edr(20171010)
plt_edr(20171015)
plt_edr(20171020)
plt_edr(20171025)
plt_edr(20171105)
plt_edr(20171110)
plt_edr(20171115)
plt_edr(20171120)
plt_edr(20171125)
plt_edr(20171205)
plt_edr(20171210)
plt_edr(20171215)
plt_edr(20171220)
plt_edr(20171225)
plt_edr(20180105)
plt_edr(20180110)
plt_edr(20180115)
plt_edr(20180120)
plt_edr(20180125)
plt_edr(20180205)
plt_edr(20180210)
plt_edr(20180215)
plt_edr(20180220)
plt_edr(20180225)
plt_edr(20180305)
plt_edr(20180310)
plt_edr(20180315)
plt_edr(20180320)
plt_edr(20180325)
plt_edr(20180405)
plt_edr(20180410)
plt_edr(20180415)
plt_edr(20180420)
plt_edr(20180425)
plt_edr(20180505)
plt_edr(20180510)
plt_edr(20180515)
plt_edr(20180520)
plt_edr(20180525)
plt_edr(20180605)
plt_edr(20180610)
plt_edr(20180615)
plt_edr(20180620)
plt_edr(20180625)
plt_edr(20180705)
plt_edr(20180710)
plt_edr(20180715)
plt_edr(20180720)
plt_edr(20180725)
plt_edr(20180805)
plt_edr(20180810)
plt_edr(20180815)
plt_edr(20180820)
plt_edr(20180825)


# %%
