from flask import Flask, render_template, request

app = Flask(__name__)

#Login
@app.route('/')
def login():
    return render_template('login.html')

#Chat
@app.route('/main',)
def index():
    return render_template('index.html')

#Profile
@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route("/get")
def get_scarlet_renponse():
    #userText = request.args.get('msg')
    return("Callate puta")

if __name__ == '__main__':
    #Mantenerlo en "debug=True" mientras estemos en fase de desarrollo
    app.run(debug=True)