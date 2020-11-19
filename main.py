from flask import Flask,render_template,request,make_response

app = Flask(__name__) 

@app.route('/') 
def index(): 
    return render_template('index.html') 

@app.route('/catulate', methods = ['POST', 'GET'])
def calculate():
    if request.method == 'POST' and 'unbusiness' in request.form:
        amount = 0 
        total = 0
        units = int(request.form['unit'] )
        surcharge = 500   

        if(units < 30):
            amount = units * 35 
            content = [amount] 
        elif(units <= 50):
            amount = ((units - 30) * 50)+ 1050
            content = [1050,amount]
        elif(units <= 75):
            amount = ((units - 50) * 70)+ 2050
            content = [1050,1000,amount] 
        elif(units <= 100):
            amount = ((units - 75) * 90)+ 3800
            content = [1050,1000,1750,amount] 
        elif(units <= 150):
            amount = ((units - 100) * 110)+ 6050
            content = [1050,1000,1750,2250,amount]
        elif(units <= 200):
            amount = ((units - 150) * 120)+ 11550
            content = [1050,1000,1750,2250,5500,amount]
        else:
            amount = ((units - 200) * 125)+ 17550
            content = [1050,1000,1750,2250,5500,6000,amount] 
        total = amount + surcharge
        # x = {
        #     'amount':amount,
        #     'surcharge':surcharge,
        #     'units':units,
        #     'total':total,
        #     'horse power':0,
        #     'tax':0,
        # }
        # data = json.dumps(x,sort_keys=True)
        data = (units,total,content,amount,surcharge)
        return render_template('bill.html', data=data ) 
    else:
        amount = 0 
        total = 0
        units = int(request.form['unit'] )
        surcharge = 0   

        if(units < 500):
            amount = units * 125
            content = [amount] 
        elif(units <= 5000):
            amount = ((units - 500) * 135)+ 62500
            content = [62500,amount]
        elif(units <= 10000):
            amount = ((units - 5000) * 145)+ 607500
            content = [62500,607500,amount] 
        elif(units <= 100):
            amount = ((units - 10000) * 155)+ 725000
            content = [62500,607500,725000,amount] 
        elif(units <= 150):
            amount = ((units - 20000) * 165)+ 1550000
            content = [62500,607500,725000,1550000,amount]
        elif(units <= 200):
            amount = ((units - 50000) * 175)+ 4950000
            content = [62500,607500,725000,1550000,4950000,amount]
        else:
            amount = ((units - 200) * 180)+ 8750000
            content = [62500,607500,725000,1550000,4950000,8750000,amount] 
        total = amount + surcharge
        # x = {
        #     'amount':amount,
        #     'surcharge':surcharge,
        #     'units':units,
        #     'total':total,
        #     'horse power':0,
        #     'tax':0,
        # }
        # data = json.dumps(x,sort_keys=True)
        data = (units,total,content,amount,surcharge)
        return render_template('result.html', data=data , total=total) 
if __name__ == '__main__': 
    app.run(debug = True) 
