import MySQLdb
import matplotlib.pyplot as plt
import pandas as pd
from secret import nama, passwd

mydb=MySQLdb.connect(
    host='localhost',
    user=nama,
    passwd=passwd,
    db='world',
    charset='utf8'
)
x=mydb.cursor()
x.execute("select name,population,gnp,surfacearea from country where name in ('Brunei','Cambodia','East Timor','Indonesia','Laos','Malaysia','Myanmar','Philippines','Singapore','Thailand','Vietnam') order by name")
data=list(x.fetchall())
# print(data)

df=pd.DataFrame(data,columns=['Negara','Populasi','GNP','LuasDaratan'])
print(df)

#NOMOR 1
color=['y','r','g','b','pink','cyan','grey','lime','lightblue','magenta','gold']
plt.bar(df['Negara'],df['Populasi'],color=color)
plt.xlabel('Negara')
plt.ylabel('Populasi (x100JtJiwa)')
plt.xticks(rotation=60,fontsize=7)
plt.yticks(fontsize=7)
plt.title('Populasi Negara ASEAN')
for x,y in zip(df['Negara'],df['Populasi']):
    label = "{:.2f}".format(y)
    plt.annotate(label, (x,round(y)), textcoords="offset points", xytext=(0,5), ha='center', fontsize=5)

plt.show()