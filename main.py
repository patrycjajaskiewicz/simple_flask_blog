from flask import Flask,render_template, request
import pip._vendor.requests


app = Flask(__name__)
#requesting blogs api and saving it as a json data
api = pip._vendor.requests
respond = api.get('https://api.npoint.io/c790b4d5cab58020d391')
json_data = respond.json()

@app.route('/')
def home():
    return render_template('index.html', json_data=json_data)


@app.route('/about')
def about():
    return render_template('about.html')

#creating contact form
@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
            return render_template('contact.html', msg_sent=True)
    return render_template('contact.html', msg_sent=False)

#route to separate blog post with title and body text
#using number variable(contain post id) created in index.html to create specific blog page
@app.route('/post/<int:num>')
def post(num):
     #looping through all blog posts and checking if blog id is indentical to number variable 
    for blog in json_data:
        if blog['id'] == num:
            return render_template('post.html', json_data=json_data, num=num)






if __name__ == '__main__':
    app.run(debug=True)