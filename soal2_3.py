import MySQLdb
import matplotlib.pyplot as plt
import pandas as pd
import os 
from flask import Flask
from secret import nama, passwd

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

#bar plot
plt.figure(figsize=(10,8))
plt.style.use('ggplot')
color=['y','r','g','b','pink','cyan','grey','lime','lightblue','magenta','gold']
x=plt.bar(df['Negara'],df['GNP'],color=color)
plt.title('Pendapatan Bruto Nasional ASEAN\n')
plt.xticks(rotation=60,fontsize=7)
plt.yticks(fontsize=7)
plt.xlabel('Negara')
plt.ylabel('Gross National Product (US$)')
for x,y in zip(df['Negara'],df['GNP']):
    label = "{:.2f}".format(y)
    plt.annotate(label, (x,y), textcoords="offset points", xytext=(0,5), ha='center', fontsize=7)
namafile='soal2_3.png'
plt.savefig(os.path.join(app.config['UPLOAD_FOLDER'],namafile))
plt.show()
