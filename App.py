from unicodedata import category
from flask import Flask, redirect, request, render_template
import pickle

app = Flask(__name__)
model = open('model.pkl', 'rb')     
model= pickle.load(model)

@app.route('/')
def login():
    return render_template('page-login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/handle_login')
def login_check():
    return render_template('index.html')

@app.route('/stock/login')
def stockLogin():
    return render_template('stock/login.html')


@app.route('/graph')
def viewGraph():
    return render_template('graph/graph.html')

@app.route('/calender')
def viewCalender():
    return render_template('calender.html')


@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method=='POST':
        pro_id=request.form['product-id']
        dept_id=request.form['dept-id']
        outlet=request.form['outlet']
        sell_price=request.form['sell-price']
        state=request.form['state']
        category=request.form['category']
        month=request.form['month']
        
        res=round(model.predict([[pro_id,dept_id,outlet,sell_price,state,category,month]])[0],4)*100
        print('---------')
        print(res)

    return render_template('prediction.html',res=res)

if __name__ == '__main__':
   app.run(debug=True)






































