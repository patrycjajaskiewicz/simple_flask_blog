from flask import Flask,render_template
import pip._vendor.requests


app = Flask(__name__)
#requesting blogs api and saving it as a json data
request = pip._vendor.requests
respond = request.get('https://api.npoint.io/c790b4d5cab58020d391')
json_data = respond.json()

@app.route('/')
def home():
    return render_template('index.html', json_data=json_data)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:num>')
def post(num):
    for blog in json_data:
        if blog['id'] == num:
            return render_template('post.html', json_data=json_data, num=num)






if __name__ == '__main__':
    app.run(debug=True)