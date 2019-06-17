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

plt.pie(df['LuasDaratan'],labels=df['Negara'], autopct='%1.1f%%',textprops={'fontsize':7})
plt.axis('equal')
plt.title('Luas Daratan ASEAN\n',fontsize=15)
plt.show()