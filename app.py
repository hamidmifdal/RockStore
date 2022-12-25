from flask import Flask , render_template as r , request , redirect
import requests
app = Flask(__name__)

@app.route('/')
def route():
    return r('index.html', name='Rock Store')

@app.route('/about')
def about():
    return ' hi ,about me!'

@app.route('/admin/<name>')
def admin(name):
    return r('admin/admin.html', name=name)

@app.route('/buynow', methods=['POST','GET'])
def buy():
    if request.method=='POST':
        name = request.form['name']
        adress   = request.form['address']
        tel      = request.form['tel']
        comm      = request.form['comm']
        TOKEN = "5501495930:AAFdc-5WHgPAhNELTWcRzY_rqmj81x7g3F0"
        chat_id = "1966259244"
        text = f"\n>>>Fullname : \n"+name+"\n>>>Address : \n"+adress+"\n>>>Telephone : \n"+tel + "\n>>>Comments : \n"+ comm
        url = 'https://api.telegram.org/bot'+ TOKEN +'/sendMessage?chat_id='+ chat_id +'&text='+ text
        r = requests.get(url)
        return redirect('/') ,r.json()
    else:
        return 'not found api'

if __name__ == '__main__':
    app.run(debug=True ,)