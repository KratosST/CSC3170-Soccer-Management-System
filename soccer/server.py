from flask import Flask, render_template
 
app = Flask(__name__)
 
 
@app.route('/')
def hello_world():
    return 'hello world'
 
 
@app.route('/user')
def user():
    user_info = {
        'name': 'letian',
        'email': '123@aa.com',
        'age':0,
        'github': 'https://github.com/letiantian'
    }
    return render_template('homepage.html', page_title='soccer')
 
 
if __name__ == '__main__':
    app.run(port=5000, debug=True)