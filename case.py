#место для твоего кода
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Space_Corrected.csv')
df.info()
#названия компаний 
rs =(df['Company Name'].value_counts())
print(rs)
Eve = df['Company Name'].min()
#print(Eve)
#локация
rp = (df['Location'].value_counts())
#print(rp)
#дата полёта
dw = (df['Datum'].value_counts())
print(dw)
#нозвания рокеты
dr = (df['Detail'].value_counts())
#print(dr)
#исход запуска и др.
ds = (df[' Rocket'].value_counts())
#print(ds)
#гипотеза про первый полет и последний

#print(dw,dss)
#гипотеза про компаний лучше
rs =(df['Company Name'].value_counts())
rd = rs['SpaceX']
rd_2 = rs['Rocket Lab']
rd_3 = rs['Virgin Orbit']
rd_4 = rs['Blue Origin']
rd_5 = rs['OneSpace']
ar = (rd+rd_2+rd_3+rd_4+rd_5)
print('Частные компании:',rd,rd_2,rd_3,rd_4,rd_5)


rb = rs['NASA']
rb_2 = rs['RVSN USSR']
rb_3 = rs['JAXA']
rb_4 = rs['Arianespace']
print('ГОС компаний:',rb,rb_2,rb_3,rb_4)
ab = (rb+rb_2+rb_3+rb_4)
if ab > ar:
    print('ГОС компаний больше запуска и опыта')
else:
    print('Частные компаний больше запуска да и Илон хорош')\

#граффики


dss = (df['Datum'].value_counts())
dss.plot(kind = 'scatter')
plt.show()


s = pd.Series(data = [rb,rb_2,rb_3,rb_4,rd,rd_2,rd_3,rd_4,rd_5])

s.plot(kind = 'bar')
plt.show()