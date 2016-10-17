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
#Helper stuff go here
#----------------------------------
def getBlogs(proj, page_number):
    return

#store user data after validation
def storeUserData(data):
    userdata = dict()
    userdata['firstlastname'] = data[0][1]
    userdata['username'] = data[0][2]
    userdata['emailaddres'] = data[0][3]
    if request.form['inputUsername'] == os.environ['BLOG_ADMIN_USERNAME']:
        userdata['isadmin'] = "Admin"
    else:
        userdata['isadmin'] = None
    return userdata

#determines, based on userdata, whether the user is signed in
def isSignedOut():
    return 'userdata' not in session or session.get('userdata') == None


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
    return render_template('Blog.html', userdata = session.get('userdata'))

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
    if isSignedOut():
        return redirect('/')
    else:
        return render_template('CreatePost.html', userdata = session.get('userdata'))

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
    if isSignedOut():
        return render_template('SignIn.html', userdata = None)
    else:
        return redirect("/")

@app.route('/signout')
def signOut():
    if isSignedOut():
        return redirect("/")
    else:
        session['userdata'] = None
        return redirect("/")

@app.route('/signup')
def signUp():
    if isSignedOut():
        return render_template('SignUp.html', userdata = None)
    else:
        return redirect("/")

@app.route('/validateuser', methods = ['POST'])
def validateUser():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_validateLogin', (request.form['inputUsername'],))
    data = cursor.fetchall()

    if hashing.check_value(str(data[0][4]), request.form['inputPassword'], salt=os.environ['HASH_SALT']):
        session['userdata'] = storeUserData(data)
    return redirect("/")

@app.route('/createuser', methods = ['POST'])
def createUser():
    conn = mysql.connect()
    cursor = conn.cursor()

    val_name = request.form['inputName']
    val_username = request.form['inputUsername']
    val_email = request.form['inputEmail']
    val_hash = hashing.hash_value(request.form['inputPassword'], salt=os.environ['HASH_SALT'])

    cursor.callproc('sp_createUser',(val_name, val_username, val_email, val_hash))
    data = cursor.fetchall()
    print(data)
    if len(data) is 0:
        conn.commit()
        cursor.callproc('sp_validateLogin', (request.form['inputUsername'],))
        data = cursor.fetchall()
        session['userdata'] = storeUserData(data)
    return redirect("/")


#Start server if called by itself
if __name__ == "__main__":
    app.run()
