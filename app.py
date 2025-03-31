from flask import Flask, render_template, request, redirect, make_response
import base64

app = Flask(__name__)

FLAG = "SSEC{b4s364_c00k13_h4ck}"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/admin')
def admin():
    auth_cookie = request.cookies.get("auth")
    
    if not auth_cookie:
        return "Unauthorized Access! Admins Only!", 403

    decoded_auth = base64.b64decode(auth_cookie).decode()

    if decoded_auth == "role:admin":
        return f"Welcome Admin! Here is your flag: {FLAG}"
    else:
        return "Unauthorized Access! Admins Only!", 403

@app.route('/set_cookie')
def set_cookie():
    resp = make_response(redirect('/'))
    user_role = base64.b64encode("role:user".encode()).decode()
    resp.set_cookie("auth", user_role)
    return resp

if __name__ == '__main__':
    app.run(debug=True)
