#Module includes
from flask import Flask, render_template, request
from flaskext.mysql import MySQL
import os

#Initializations
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ['MYSQL_PASS']
app.config['MYSQL_DATABASE_DB'] = 'BlogPosts'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


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
    admin_val = None
    cursor = conn.cursor()
    if request.method == 'POST':
        admin_val = "admin"
    else:
        admin_val = None
    return render_template('Blog.html', admin = admin_val)

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
@app.route('/login')
def signIn():
    return "Page to log into blog"

@app.route('/signup')
def signUp():
    return "Page to add user to blog"

@app.route('/validateuser', methods = ['POST'])
def validateUser():
    return "Redirects to main blog in user session"


#Start server if called by itself
if __name__ == "__main__":
    app.run()
