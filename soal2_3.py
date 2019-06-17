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


df=pd.DataFrame(data,columns=['Negara','Populasi','GNP','LuasDaratan'])
print(df)

color=['y','r','g','b','pink','cyan','grey','lime','lightblue','magenta','gold']
x=plt.bar(df['Negara'],df['GNP'],color=color)
plt.title('Pendapatan Bruto Nasional ASEAN')
plt.xticks(rotation=60,fontsize=7)
plt.yticks(fontsize=7)
plt.xlabel('Negara')
plt.ylabel('Gross National Product (US$)')
for x,y in zip(df['Negara'],df['GNP']):
    label = "{:.2f}".format(y)
    plt.annotate(label, (x,y), textcoords="offset points", xytext=(0,5), ha='center', fontsize=6)
plt.show()