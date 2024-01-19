import csv
import os
from io import StringIO

from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.utils import secure_filename
import forms
import api_calls

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
login_manager = LoginManager(app)
login_manager.login_view = 'login'

uploads_folder = 'uploads'


@login_manager.user_loader
def load_user(user_id):
    user = User(user_id)
    return user

class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_pdf():
    form = forms.UploadForm()

    if form.validate_on_submit():
        uploaded_files = request.files.getlist('files')
        empty_uploads_folder()
        for file in uploaded_files:
            # Ensure the file has a secure filename
            filename = secure_filename(file.filename)
            # Save the file to a designated folder
            file.save('uploads/' + filename)
            files = [f for f in os.listdir(uploads_folder) if os.path.isfile(os.path.join(uploads_folder, f))]
            file_list = [('pdf_files', (filename, open(os.path.join(uploads_folder, filename), 'rb'))) for filename in files]

            response = api_calls.dashboard(file_list, current_user.id)
            print(response.json())
            if response.status_code == 200:
                result = response.json()
                # Extract the CSV data from the response
                csv_data = result.get('csv_file', '')

                # Use StringIO to create a file-like object for the csv.reader
                csv_file = StringIO(csv_data)

                # Parse the CSV data into a list of lists
                csv_reader = list(csv.reader(csv_file))

                # The first row contains headers, and the rest are data rows
                headers = csv_reader[0]
                data_rows = csv_reader[1:]
            # Process the uploaded files or redirect to a new page
                xml_data = result.get('xml_file')
        return render_template('result.html', headers=headers, data_rows=data_rows, xml_data=xml_data)
    return render_template('upload_pdf.html', form=form)


def empty_uploads_folder():
    # Remove all files in the uploads folder
    for file in os.listdir(uploads_folder):
        file_path = os.path.join(uploads_folder, file)
        try:
            if os.path.isfile(file_path):
                with open(file_path, 'wb'):
                    pass  # This opens and immediately closes the file to release any locks
                os.unlink(file_path)
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")


@app.route("/login", methods=['GET', 'POST'])
def login():
    print('trying')
    if current_user.is_authenticated:
                return redirect(url_for('upload_pdf'))
    form = forms.LoginForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        response = api_calls.user_login(email, password)

        if (response.status_code == 200):
            token = response.json().get('access_token')
            user = User(user_id=token)
            login_user(user)

            return redirect(url_for('upload_pdf'))
        else:
            flash('Login unsuccessful. Please check email and password.', category='error')

    return render_template('login.html', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    print('trying4')
    form = forms.RegisterForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        response = api_calls.user_register(username, email, password)

        if (response.status_code == 200):
            flash('Registration Successful', category='info')
            return redirect(url_for('login'))
        else:
            flash('Registration unsuccessful. Please check username, email and password.', category='error')

    return render_template('register.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout successful!', 'success')
    return redirect(url_for('login'))


@app.route('/result/<result>')
@login_required
def result():
    result = session.get('result', {})
    return render_template('result.html', result=result)


@app.route("/profile")
@login_required
def profile():
    response = api_calls.get_user_profile(current_user.id)
    if (response.status_code == 200):
       result = response.json()
       username = result.get('username', '')
       email = result.get('email', '')

       return render_template('profile.html', username=username,email = email)


@app.route("/admin-dashboard")
@login_required
def admin_dashboard():
    respo = api_calls.get_user_profile(current_user.id)
    if (respo.status_code == 200):
        admin_detail = respo.json()
        username = admin_detail.get('username', '')
        email = admin_detail.get('email', '')

    response = api_calls.get_all_users(current_user.id)
    if (response.status_code == 200):
        result = response.json()
        print(result)


    return render_template('admin_panel.html',result = result, username=username, email=email)



@app.route('/update_password', methods=['PUT'])
@login_required
def update_password():
    form = forms.UpdatePasswordForm()

    if form.validate_on_submit():
        current_password = form.current_password.data
        new_password = form.new_password.data
        confirm_new_password = form.confirm_new_password.data
        response = api_calls.update_password(current_password, new_password, confirm_new_password, current_user.id)
        print(response.status_code)
        if (response.status_code == 200):
            flash('Registration Successful', category='info')
            return redirect(url_for('login'))
        else:
            flash('Registration unsuccessful. Please check username, email and password.', category='error')

    return render_template('update_password.html', form=form)


@app.route("/admin/login", methods=['GET', 'POST'])
def admin_login():
    print('trying')
    if current_user.is_authenticated:

        return redirect(url_for('admin_dashboard'))
    form = forms.LoginForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        response = api_calls.admin_login(email, password)

        if (response.status_code == 200):
            token = response.json().get('access_token')
            user = User(user_id=token)
            login_user(user)

            return redirect(url_for('admin_dashboard'))
        else:
            flash('Login unsuccessful. Please check email and password.', category='error')

    return render_template('admin_login.html', form=form)






if __name__ == '__main__':
    app.run()

