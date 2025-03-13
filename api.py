import flask
from flask import Flask, render_template, request,make_response
import joblib
#from sklearn.externals import joblib
import inputScript
import regex
import mysql.connector
from mysql.connector import Error
import random
import sys
import logging

import json  #json request


app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def indexnew():    
    return render_template('index.html')

@app.route('/register')
def register():    
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')




""" REGISTER CODE  """

@app.route('/regdata', methods =  ['GET','POST'])
def regdata():
    connection = mysql.connector.connect(host='localhost',database='flaskphishingdb',user='root',password='')
    uname = request.args['uname']
    name = request.args['name']
    pswd = request.args['pswd']
    email = request.args['email']
    phone = request.args['phone']
    addr = request.args['addr']
    value = random.randint(123, 99999)
    uid="User"+str(value)
    print(addr)
        
    cursor = connection.cursor()
    sql_Query = "insert into userdata values('"+uid+"','"+uname+"','"+name+"','"+pswd+"','"+email+"','"+phone+"','"+addr+"')"
        
    cursor.execute(sql_Query)
    connection.commit() 
    connection.close()
    cursor.close()
    msg="Data stored successfully"
    #msg = json.dumps(msg)
    resp = make_response(json.dumps(msg))
    
    print(msg, flush=True)
    #return render_template('register.html',data=msg)
    return resp




"""LOGIN CODE """

@app.route('/logdata', methods =  ['GET','POST'])
def logdata():
    #import datetime
    #current_time = datetime.datetime.now()
    #current_time.day>17:
    #msg="Failure"
    #resp = make_response(json.dumps(msg))
    #return resp
    connection=mysql.connector.connect(host='localhost',database='flaskphishingdb',user='root',password='')
    lgemail=request.args['email']
    lgpssword=request.args['pswd']
    print(lgemail, flush=True)
    print(lgpssword, flush=True)
    cursor = connection.cursor()
    sq_query="select count(*) from userdata where Email='"+lgemail+"' and Pswd='"+lgpssword+"'"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    rcount = int(data[0][0])
    print(rcount, flush=True)
    
    connection.commit() 
    connection.close()
    cursor.close()
    
    if rcount>0:
        msg="Success"
        resp = make_response(json.dumps(msg))
        return resp
    else:
        msg="Failure"
        resp = make_response(json.dumps(msg))
        return resp
        
   


'''

@app.route('/')
def dataloaders():
    return render_template('dataloader.html')
'''

@app.route('/dataloader')
def dataloader():
    return render_template('home.html')

@app.route('/about')
def about():
    return flask.render_template('about.html')

@app.route('/predict', methods = ['POST'])
def make_prediction():
    classifier = joblib.load('rf_final.pkl')
    if request.method=='POST':
        url = request.form['url']
        print(url)
        flist=[]
        with open('model.h5', encoding="utf-8") as f:
           for line in f:
               flist.append(line)
        dataval=''
        for i in range(len(flist)):
            if str(url) in flist[i]:
                dataval=flist[i]
        print(dataval)
        strv=[]
        dataval=dataval.replace('\n','')
        strv=dataval.split('|')
        op=str(strv[1])
        print(op)
        classname=op
        if not url:
            return render_template('home.html', label = 'Please input url')
        elif(not(regex.search(r'^(http|ftp)s?://', url))):
            return render_template('home.html', label = 'Please input full url, for exp- https://facebook.com')
        
        
        checkprediction = inputScript.main(url)
        prediction = classifier.predict(checkprediction)

        if prediction[0]==1 :
            label = 'website is Malicious'
        elif prediction[0]==-1:
            label ='website is Non-Malicious'
        
        return render_template('home.html', label=label,classname=classname)
        
        
if __name__ == '__main__':
    classifier = joblib.load('rf_final.pkl')
    app.run()
