from flask import Flask,render_template,request
#import string
from function import *
 
app = Flask(__name__)

 
@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/data', methods = ['POST', 'GET'])
def data():
    # If this code was reached with a GET HTTP method, there's no data to work on, so redirect to /form
    if request.method == 'GET':
        return "<h1>The URL /data was accessed directly. Try going to <a href=\"/form\">/form</a> to submit data</h1>"
    if request.method == 'POST':
        form_data = request.form
        text=(form_data['Phrase'].lower())
        try:
            step=int(form_data['Step'])
        except ValueError:
            return "<h1>You did not choose an integer value for the step, <a href=\"/form\">try again</a></h1>"
    if form_data['Op'] == "Encrypt":
        encrypted_message = ceasarEncrypt(text,step)
        return render_template('data.html',result=encrypted_message)
    else:
        decrypted_message = ceasarDecrypt(text,step)
        return render_template('data.html',result=decrypted_message)

@app.route('/atbash', methods = ['POST', 'GET'])
def atbash():
    # If this code was reached with a GET HTTP method, there's no data to work on, so redirect to /form
    if request.method == 'GET':
        return "<h1>The URL /atbash was accessed directly. Try going to <a href=\"/form\">/form</a> to submit data</h1>"
    if request.method == 'POST':
        form_data = request.form
        text=(form_data['Phrase'].lower())
        
        encrypted_message = atbashCrypt(text)
        return render_template('data.html',result=encrypted_message)
    
@app.errorhandler(404)
def handle_404(e):
    # handle all other routes here
    return render_template('form.html')
 
app.run(host='0.0.0.0', port=80)
#'0.0.0.0'
