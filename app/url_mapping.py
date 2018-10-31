from app import app, db
from flask_login import login_required, current_user, login_user, logout_user
from flask import render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from werkzeug.urls import url_parse
from app.entity_mapping import User


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='HomePage')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    class LoginForm(FlaskForm):
        username = StringField('UserName', validators=[DataRequired()])
        password = PasswordField('Password', validators=[DataRequired()])
        remember_me = BooleanField('remember_me', default=False)
        submit = SubmitField('Sign In')

    form = LoginForm()

    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data).first()
        if u is None or not u.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('index'))
        login_user(u, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form, can_reg=True)


@app.route('/logout')  
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/realTime')
def realTime():
    return render_template('realTime.html')

@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/logs')
def logs():
    return render_template('logs.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')


@app.route('/user/<username>')
@login_required
def userprofile(username):
    u = User.query.filter_by(username=username).first_or_404()
    # first_or_404() implement by flask_sqlalchemy, raising 404 automatically instead of returning none
    return render_template('user.html', user=u, title='UserProfile')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    class RegForm(FlaskForm):
        username = StringField('Username', validators=[DataRequired()])
        password = PasswordField('Password', validators=[DataRequired()])
        password2 = PasswordField(
            'Repeat Password', validators=[DataRequired(), EqualTo('password')])
        submit = SubmitField('Register')

        def validate_username(self, username):
            u = User.query.filter_by(username=username.data).first()
            if u is not None:
                raise ValidationError('Please use a different username.')

    form = RegForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

