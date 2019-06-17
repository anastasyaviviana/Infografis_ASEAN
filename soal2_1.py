import MySQLdb
import matplotlib.pyplot as plt
import pandas as pd
import os 
from flask import Flask
from secret import nama, passwd

#folder to save file
app=Flask(__name__)
app.config['UPLOAD_FOLDER']='./chart'

#Connect to mysql
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

#Dataframe
df=pd.DataFrame(data,columns=['Negara','Populasi','GNP','LuasDaratan'])

#NOMOR 1
plt.figure(figsize=(10,8))
plt.style.use('ggplot')
color=['y','r','g','b','pink','cyan','grey','lime','lightblue','magenta','gold']
plt.bar(df['Negara'],df['Populasi'],color=color)
plt.xlabel('Negara',fontsize=9)
plt.ylabel('Populasi (x100JtJiwa)',fontsize=9)
plt.xticks(rotation=70,fontsize=7)
plt.yticks(fontsize=7)
plt.grid(True)
plt.title('Populasi Negara ASEAN\n')
for x,y in zip(df['Negara'],df['Populasi']):
    label = "{:.2f}".format(y)
    plt.annotate(label, (x,round(y)), textcoords="offset points", xytext=(0,5), ha='center', fontsize=7)
namafile='soal2_1.png'
plt.savefig(os.path.join(app.config['UPLOAD_FOLDER'],namafile))
plt.show()