import MySQLdb
import matplotlib.pyplot as plt
import pandas as pd
import os 
from flask import Flask
from secret import nama, passwd

#folder to save file
app=Flask(__name__)
app.config['UPLOAD_FOLDER']='./chart'
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

#pie plot
plt.pie(df['LuasDaratan'],labels=df['Negara'], autopct='%1.1f%%',textprops={'fontsize':7})
plt.axis('equal')
plt.title('Luas Daratan ASEAN\n',fontsize=15)
namafile='soal2_4.png'
plt.savefig(os.path.join(app.config['UPLOAD_FOLDER'],namafile))
plt.show()