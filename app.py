# Step 1: Create all necesary files
# Step 2: Create Virtual Environment


# Step 3: Import all necessary modules and classes
from flask import Flask, render_template, request, url_for, redirect
from email.mime.text import MIMEText
import smtplib
from email.message import EmailMessage

# Step 4. Define our Flask app
app = Flask(__name__)

# Step 5. Create our route to render our index.html upon loading
@app.route("/")
def index():
    return render_template("index.html")

# Create a rount that loads when the user clicks the Submit button on the form
# We will send data here using the POST method
@app.route('/sendemail/', methods=['POST'])
# Define the function for the route
def sendemail():
    if request.method == "POST":
        name = request.form['name']
        subject = request.form['Subject']
        email = request.form['_replyto']
        message = request.form['message']

        # ! Set your credentials (note: security here, do not upload your passwords to GitHub)
        yourEmail = "jamflynt@gmail.com"
        yourPassword = "###########"
        # Setting up an App Password with Gmail
        # use URL from google support, etc.

        # Logging into our email (GMAIL) account
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.log(yourEmail, yourPassword)

        