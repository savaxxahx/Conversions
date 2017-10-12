from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')
    
@app.route("/dollarstoyen")
def render_dollarstoyen():  
   money = float(request.args['money'])*112.15
   reply: "Your amount in Japanese Yen is " + money 
   
   return render_template('dollarstoyen.html', response = reply)
  
    
@app.route("/fahrenheittocelsuis")
def render_fahrenheittocelsuis():
    temp = (float(request.args['temp'])-32)/1.8
    reply: " Your temperature in Celsuis is" + temp
    return render_template('fahrenheittocelsuis.html', response = reply)

@app.route("/inchestocenti")
def render_inchestocenti():
    height = float(request.args['height'])*2.54
    reply: " Your height in centimeters is" + height
     return render_template('inchestocenti.html', response = reply)


    
    if __name__=="__main__":
    app.run(debug=False, port=54321)
