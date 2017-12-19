from flask import Flask
from flask import request

app = Flask(__name__)


html = """
<center>
<form action='/convert' method='POST'>
<h1>Welcome!</h1>
Pound: <input type='text' name='pound' value='{pound}'> = <span id='kilo'>{kilo}</span> kg<br>
<br>
<input type='submit' value='Submit'>
</form>
"""


@app.route("/")
def index():
    lb = 0
    kg = 0
    return html.format(pound=lb, kilo=kg)

@app.route("/convert", methods=['POST'])
def convert():
    # you can retrieve the pound value from request.form["pound"]
    # Now complete the logic here
    try:
        lb = int(request.form['pound'])
        if lb < 0 :
            print("Value is nagative")
            lb='throw exception'
        
    except ValueError:
        if lb is None:
            print("No value")
        print('Here exception start')
    
    finally:
        kg = 4.535923700000001*lb    
        return html.format(pound=lb, kilo=kg)


@app.errorhandler(Exception)
def handle_global_error(e):
    lb = 'error'
    kg = 0
    html = """
    
<center>
<form action='/convert' method='POST'>
<h1>
Error: Please enter an integer</h1>

Pound: <input type='text' name='pound' value='{pound}'> = <span id='kilo'>{kilo}</span> kg<br>
<br>
<input type='submit' value='Submit'>
</form>
"""
    return html.format(pound=lb, kilo=kg)

if __name__== "__main__":
	app.run(host='0.0.0.0', port=4000)