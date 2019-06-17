import MySQLdb
import matplotlib.pyplot as plt
import pandas as pd
import os 
from flask import Flask
from secret import nama, passwd #import name & password my mysql

#folder to save file
app=Flask(__name__)
app.config['UPLOAD_FOLDER']='./chart'

#CONNECT TO MYSQL
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

#dataframe 
df=pd.DataFrame(data,columns=['Negara','Populasi','GNP','LuasDaratan'])

#Pie Plot
plt.pie(df['Populasi'],labels=df['Negara'], autopct='%1.1f%%',textprops={'fontsize':7})
plt.axis('equal')
plt.title('Persentase Penduduk Asean',fontsize=15)
namafile='soal2_2.png'
plt.savefig(os.path.join(app.config['UPLOAD_FOLDER'],namafile))
plt.show()