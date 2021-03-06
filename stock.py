
'''
0   2020-07-08T13:25:00+0530  82.25  82.35  82.20  82.30   176821    0
1   2020-07-08T13:35:00+0530  82.30  82.30  82.00  82.15   372451    0
2   2020-07-08T13:45:00+0530  82.15  82.30  82.05  82.20   228665    0
3   2020-07-08T13:55:00+0530  82.20  82.25  82.10  82.15   180082    0
4   2020-07-08T14:05:00+0530  82.15  82.30  82.10  82.15   360550    0
5   2020-07-08T14:15:00+0530  82.15  82.20  82.10  82.10   384443    0
6   2020-07-08T14:25:00+0530  82.15  82.15  81.60  81.65   783184    0
7   2020-07-08T14:35:00+0530  81.65  82.05  81.55  81.70  1107222    0
8   2020-07-08T14:45:00+0530  81.70  81.90  81.40  81.55   927582    0
9   2020-07-08T14:55:00+0530  81.60  82.00  81.20  81.55  1163898    0
10  2020-07-08T15:05:00+0530  81.55  81.80  81.10  81.10   858623    0
11  2020-07-08T15:15:00+0530  81.15  81.15  81.00  81.10   924860    0
12  2020-07-08T15:25:00+0530  81.10  81.30  81.00  81.25   608408    0
70.99
'''


import pandas as pd
df=pd.DataFrame({'open':[82.30,82.15,82.20,82.15,82.15,82.15,81.65,81.70,81.60,81.55,81.15,81.10,81.60,81.80,81.35,81.35,81.45,81.70,81.60,81.40,81.25,81.25,81.10,80.90,81.15,81.00,81.10,80.90,80.95,81.00,80.95,80.95,81.10,81.00,81.05,80.95,80.90,80.90,80.90,80.85,80.60,80.60,80.50,80.45,80.50,80.55,80.45,80.10,80.35,80.40],'high':[82.30,82.30,82.25,82.30,82.20,82.15,82.05,81.90,82.00,81.80,81.15,81.30,82.25,81.80,81.35,81.50,81.70,81.85,81.65,81.45,81.45,81.30,81.25,81.15,81.15,81.15,81.10,81.05,81.10,81.00,81.05,81.15,81.10,81.10,81.10,80.95,80.95,81.00,81.00,80.90,80.70,80.60,80.60,80.50,80.65,80.60,80.50,80.45,80.45,80.50],'low':[82.00,82.05,82.10,82.10,82.10,81.60,81.55,81.40,81.20,81.10,81.00,81.00,81.50,81.20,81.10,81.25,81.35,81.55,81.30,81.25,81.20,81.10,80.80,80.90,80.90,80.95,80.85,80.90,80.90,80.90,80.90,80.95,80.90,80.95,80.80,80.85,80.85,80.80,80.80,80.40,80.40,80.45,80.35,80.35,80.45,80.40,80.10,79.90,80.20,80.35],'close':[82.15,82.20,82.15,82.15,82.10,81.65,81.70,81.55,81.55,81.10,81.10,81.25,81.80,81.35,81.30,81.40,81.65,81.60,81.40,81.25,81.25,81.15,80.95,81.15,81.00,81.05,80.95,81.00,81.00,80.95,81.00,81.05,80.95,81.00,80.95,80.90,80.95,80.90,80.80,80.55,80.60,80.50,80.45,80.50,80.55,80.45,80.10,80.30,80.35,80.50]})

HH = df.high.rolling(window=6).max()
LL = df.low.rolling(window=6).min()
HL = HH - LL
M = (HH + LL) / 2
D = df.close - M

#D_MA_1 = D.rolling(window=3).mean()
#D_MA = D_MA_1.rolling(window=3).mean()
#D_SMOOTH_1 = D_MA.rolling(window=3).mean()
#D_SMOOTH = D_SMOOTH_1.rolling(window=3).mean()

#HL_MA_1 = HL.rolling(window=3).mean()
#HL_MA = HL_MA_1.rolling(window=3).mean()
#HL_SMOOTH_1 = HL_MA.rolling(window=3).mean()
#HL_SMOOTH = HL_SMOOTH_1.rolling(window=3).mean()

multiplier = np.array([1/2**9, 1/2**9, 1/2**8, 1/2**7, 1/2**6, 1/2**5, 1/2**4, 1/2**3, 1/2**2, 1/2])
#D_MA_1 = D.rolling(window=3).mean()
#D_MA = D_MA_1.rolling(window=3).mean()
D_MA = D.rolling(window=10).apply(lambda x: sum(x * multiplier))
#HL_MA_1 = HL.rolling(window=3).mean()
#HL_MA = HL_MA_1.rolling(window=3).mean()
HL_MA = HL.rolling(window=10).apply(lambda x: sum(x * multiplier))
#D_SMOOTH_1 = D_MA.rolling(window=3).mean()
#D_SMOOTH = D_SMOOTH_1.rolling(window=3).mean()
D_SMOOTH = D_MA.rolling(window=10).apply(lambda x: sum(x * multiplier))
#HL_SMOOTH_1 = HL_MA.rolling(window=3).mean()
#HL_SMOOTH = HL_SMOOTH_1.rolling(window=3).mean()
HL_SMOOTH = HL_MA.rolling(window=10).apply(lambda x: sum(x * multiplier))

HL2 = HL_SMOOTH / 2
SMI = 100 * D_SMOOTH[49] / HL2[49]
print(SMI)

SMI_1 = 100 * D_SMOOTH[48] / HL2[48]
SMI_2 = 100 * D_SMOOTH[47] / HL2[47]
SMI_3 = 100 * D_SMOOTH[46] / HL2[46]
SMI_4 = 100 * D_SMOOTH[45] / HL2[45]

SMI_SIGNAL = (SMI + SMI_1 * 2 + SMI_2 * 3 + SMI_3 * 2 + SMI_4) / 9
print(SMI_SIGNAL)

indicators['smi'] = SMI
indicators['smi_signal'] = SMI_SIGNAL


