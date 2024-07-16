from flask import Flask,render_template,request
#import string
from function import *
 
app = Flask(__name__)

 
@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/caesar', methods = ['POST', 'GET'])
def caesar():
    try:
        # retrieve the form data (with retrieveFormData)
        text, step, direction = retrieveFormData(request.form)

        # If this code was reached with a GET HTTP method, there's no data to work on, so redirect to /form
        if request.method == 'GET':
            return "<h1>The URL /caesar was accessed directly. Try going to <a href=\"/form\">/form</a> to submit data</h1>"
        if request.method == 'POST':
            if direction == "encrypt":
                encrypted_message = ceasarEncrypt(text,step)
                return render_template('data.html',result=encrypted_message)
            else:
                decrypted_message = ceasarDecrypt(text,step)
                return render_template('data.html',result=decrypted_message)
    except Exception as e:
        return "<h1>Error: " + str(e) + "</h1>"

# TODO: HTML for this route
@app.route('/atbash', methods = ['POST', 'GET'])
def atbash():
    # If this code was reached with a GET HTTP method, there's no data to work on, so redirect to /form
    if request.method == 'GET':
        return "<h1>The URL /atbash was accessed directly. Try going to <a href=\"/form\">/form</a> to submit data</h1>"
    if request.method == 'POST':
        form_data = request.form
        text=(form_data['Phrase'].lower())
        
        encrypted_message = atbashEncrypt(text)
        return render_template('data.html',result=encrypted_message)
    
# TODO: HTML & Route handling for "/zigzag"
    
@app.errorhandler(404)
def handle_404(e):
    # handle all other routes here
    return render_template('form.html')
 
app.run(host='0.0.0.0', port=80)