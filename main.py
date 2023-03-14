from flask import Flask, render_template
import pip._vendor.requests 


app = Flask(__name__)

# requesting api with all blogs and saving it as a json 
request = pip._vendor.requests
respond = request.get('https://api.npoint.io/c790b4d5cab58020d391')
blogs = respond.json()


#route to main page with all blogs title and subtitle
@app.route('/')
def home():
    return render_template("index.html", all_blogs=blogs)


#route to separate blog post with title and body text
#using number variable(contain post id) created in index.html to create specific blog page
@app.route('/post/<int:number>')
def post(number):
        #looping through all blog posts and checking if blog id is indentical to number variable 
        for blog in blogs: 
            if blog['id'] == number:
                return render_template('post.html', all_blogs=blogs, number=number)
                    

if __name__ == "__main__":
    app.run(debug=True)
