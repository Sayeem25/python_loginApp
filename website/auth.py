from flask import Blueprint, flash, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login',  methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean=True)
    
@auth.route('/logout')
def logout():
    return render_template("logout.html")
    
@auth.route('/sign-up',  methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        cpassword = request.form.get('cpassword')
        
        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(name) < 2:
            flash('Name must be greater than 2 characters.', category='error')
        elif password != cpassword:
            flash('Password don\'t match', category='error')
        elif len(password) < 7:
            flash('Name must be at least 4 characters.', category='error')
        else:
            flash('Account create done!', category='success')
        
    return render_template("sign_up.html") 
    
    