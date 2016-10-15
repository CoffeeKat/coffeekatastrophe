#Module includes
from flask import Flask, render_template, request, redirect, session
from flask_hashing import Hashing
from flaskext.mysql import MySQL
import os

#Initializations
app = Flask(__name__)
app.secret_key = os.environ['SESSION_SECRET_KEY']
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ['MYSQL_PASS']
app.config['MYSQL_DATABASE_DB'] = 'ProjBlog'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['HASHING_METHOD'] = 'sha256'
mysql = MySQL()
mysql.init_app(app)
hashing = Hashing(app)
hashing.init_app(app)


#----------------------------------
#Helper Functions go here
#----------------------------------
def getBlogs(proj, page_number):
    return

#----------------------------------
#Blog routes go here
#----------------------------------

################################################################
# main
# Takes: GET or POST requests
# Returns: HTML page displaying welcome message and blog posts
# from all projects.
# Inherits: Base.html
# Notes:
# This page will, by default, be the same as proj_blog but with
# and optional message.  It will have a blog page navigation
# which will link to proj_blog.
################################################################
@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('Blog.html', admin = session.get('admin'))

################################################################
# proj_blog
# Takes: Project label; Page number describing range of posts
# to display ( (page number x posts per page) - posts per page
#                         TO     page number x posts per page)
# Returns: HTML page displaying blog posts by project and page
# Inherits: Base.html
# Notes:
# The main blog page will contain all posts in numeric order.
# This will be achieved by setting the "proj" variable to
# "all."
################################################################
@app.route('/proj/<proj>/<int:page_number>')
def proj_blog(proj, page_number):
    return "Project Blog: %s, Page: %s" % (proj, page_number)

################################################################
# displayPost
# Takes: Numeric Post ID from the database
# Returns: HTML page displaying the post
# Inherits: Base.html
# Notes:
# Calls stored procedure to return post by id.
# Fills in template based on post data.
################################################################
@app.route('/post/<int:post_id>')
def displayPost(post_id):
    return render_template('Post.html', postdata=post)

#----------------------------------
#Post manipulation routes go here
#----------------------------------
@app.route('/createpost')
def createPost():
    return "Page to create a post"

@app.route('/editpost')
def editPost():
    return "Page to edit a post"

@app.route('/addpost', methods = ['POST'])
def addPost():
    return "Puts post in database"

#----------------------------------
#User manipulation routes go here
#----------------------------------
@app.route('/signin')
def signIn():
    return render_template('SignIn.html', admin = session.get('admin'))

@app.route('/signup')
def signUp():
    return render_template('SignUp.html', admin = session.get('admin'))

@app.route('/validateuser', methods = ['POST'])
def validateUser():
    global admin_val
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_validateLogin', (request.form['inputUsername'],))
    data = cursor.fetchall()

    if hashing.check_value(str(data[0][4]), request.form['inputPassword'], salt=os.environ['HASH_SALT']):

        if request.form['inputUsername'] == os.environ['BLOG_ADMIN_USERNAME']:
            session['admin'] = "Admin"
        else:
            session['admin'] = None

    return redirect("/")

@app.route('/createuser', methods = ['POST'])
def createUser():
    conn = mysql.connect()
    cursor = conn.cursor()
    if request.method == 'POST':

        val_name = request.form['inputName']
        val_username = request.form['inputUsername']
        val_email = request.form['inputEmail']
        val_hash = hashing.hash_value(request.form['inputPassword'], salt=os.environ['HASH_SALT'])

        cursor.callproc('sp_createUser',(val_name, val_username, val_email, val_hash))
        data = cursor.fetchall()
        print(data)
        if len(data) is 0:
            conn.commit()
    return redirect("/")


#Start server if called by itself
if __name__ == "__main__":
    app.run()
