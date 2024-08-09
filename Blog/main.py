from flask import Flask, render_template
from requests  import *
from flask import request
import smtplib


app = Flask(__name__)

@app.route('/')
#Homepage
def homepage():
    response = get(url = "https://api.npoint.io/c790b4d5cab58020d391")
    data = response.json()
    return render_template("index.html", posts = data)

@app.route('/post/<int:id_no>')
def blog_posts(id_no):
    url_blog = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = get(url = url_blog)
    all_posts = blog_response.json()[id_no]
    return render_template("post.html", posts = all_posts, blog_id = id_no)

@app.route('/login', methods=['POST'])
def form_action():
    if request.method  == 'POST':
        name = request.form['username']
        email = request.form['email']
        text =  request.form['text']
        from_mail = "" #YOUR MAIL 1
        password = "" #YOUR PASSKEY 
        to_mail = "" #YOUR MAIL @
        subject = "Message from your blog readers"
        message = f"Subject: {subject}\n\n Name : {name} \n Email : {email} \n Message : {text}"
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls() 
                connection.login(from_mail, password) 
                connection.sendmail(from_mail, to_mail, message)  
                print("Email sent successfully")
        except smtplib.SMTPAuthenticationError:
            print("Authentication failed. Please check your email and password.")
        except smtplib.SMTPConnectError:
            print("Failed to connect to the SMTP server. Check your server address and port.")
        except Exception as e:
            print(f"An error occurred: {e}")
        return render_template('contact-me.html', msg = True)
    return render_template('contact-me.html', msg = False)
        
@app.route('/AboutMe')
def about_me():
    return render_template('about-me.html')

@app.route('/contactme')
def contact_me():
    return render_template('contact-me.html')



if __name__ =="__main__":
    app.run(debug = True)