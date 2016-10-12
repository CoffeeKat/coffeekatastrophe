#Module includes
from flask import Flask

#Initializations
app = Flask(__name__)

#----------------------------------
#Blog routes go here
#----------------------------------

@app.route('/')
def main():
    return "Main Blog"

@app.route('/proj/<proj>/<int:page_number>')
def proj_blog(proj, page_number):
    return "Project Blog: %s, Page: %s" % (proj, page_number)

#----------------------------------
#Post manipulation routes go here
#----------------------------------

@app.route('/createpost')
def createPost():
    return "Page to create a post"

@app.route('/addpost', methods = ['POST'])
def addPost():
    return "Puts post in database"

@app.route('/editpost')
def editPost():
    return "Page to edit a post"

#----------------------------------
#User manipulation routes go here
#----------------------------------
@app.route('/login')
def logIn():
    return "Page to log into blog"

@app.route('/adduser')
def addUser():
    return "Page to add user to blog"

@app.route('/validateuser', methods = ['POST'])
def validateUser():
    return "Redirects to main blog in user session"


#Start server if called by itself
if __name__ == "__main__":
    app.run()
