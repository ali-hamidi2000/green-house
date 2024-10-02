import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from flask import flash, session
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, AdminIndexView, expose
# from flask_admin import BaseView, expose
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FieldList, FormField, SubmitField, FileField
from wtforms.validators import DataRequired

"""
export FLASK_APP=app.py
flask db init  -> python manage.py makemigrations
flask db migrate -m "init db" -> python manage.py migrate
flask db upgrade
"""

# db = SQLAlchemy()
# app = Flask(__name__)
# app.secret_key = 'nM2ZYLrWdIMyNCusICeAi4zeGLqcbu4a'

# # Get the absolute path of the image
image_path = os.path.abspath(os.path.join('static', 'Aviculture.jpg'))

app = Flask(__name__)
app.secret_key = 'nM2ZYLrWdIMyNCusICeAi4zeGLqcbu4a'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Use Models for create database
"""
CREATE TABLE dbo.Poultry (
  ID varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
  Name varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  Owner varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  Type varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  LocationPointX varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  LocationPointY varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  Icon varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  CONSTRAINT Poultry_new_pk PRIMARY KEY CLUSTERED (ID)
    WITH (
      PAD_INDEX = OFF, IGNORE_DUP_KEY = OFF, STATISTICS_NORECOMPUTE = OFF,
      ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
)
"""


class Poultry(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(30), nullable=False)
    Owner = db.Column(db.String(30), nullable=False)
    Type = db.Column(db.String(30), nullable=False)
    LocationPointX0 = db.Column(db.String(30), nullable=False)
    LocationPointY0 = db.Column(db.String(30), nullable=False)
    LocationPointX1 = db.Column(db.String(30), nullable=False)
    LocationPointY1 = db.Column(db.String(30), nullable=False)
    LocationPointX2 = db.Column(db.String(30), nullable=False)
    LocationPointY2 = db.Column(db.String(30), nullable=False)
    LocationPointX3 = db.Column(db.String(30), nullable=False)
    LocationPointY3 = db.Column(db.String(30), nullable=False)
    salons = db.relationship('Salon', backref='salons_poultry', lazy=True)


"""
CREATE TABLE dbo.Salon (
  Id varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
  Name varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  Sourface varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  Hight varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  LocationPointX0 varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  LocationPointY0 varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  LocationPointX1 varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  LocationPointY1 varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  LocationPointX2 varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  LocationPointY2 varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  LocationPointX3 varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  LocationPointY3 varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  ID_Poultry varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  PRIMARY KEY CLUSTERED (Id)
    WITH (
      PAD_INDEX = OFF, IGNORE_DUP_KEY = OFF, STATISTICS_NORECOMPUTE = OFF,
      ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
)
"""


class Salon(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(30), nullable=False)
    Sourface = db.Column(db.String(30), nullable=False)
    Hight = db.Column(db.String(30), nullable=False)
    LocationPointX0 = db.Column(db.String(30), nullable=False)
    LocationPointY0 = db.Column(db.String(30), nullable=False)
    LocationPointX1 = db.Column(db.String(30), nullable=False)
    LocationPointY1 = db.Column(db.String(30), nullable=False)
    LocationPointX2 = db.Column(db.String(30), nullable=False)
    LocationPointY2 = db.Column(db.String(30), nullable=False)
    LocationPointX3 = db.Column(db.String(30), nullable=False)
    LocationPointY3 = db.Column(db.String(30), nullable=False)
    image = db.Column(db.String(500), nullable=True)
    length = db.Column(db.String(300), nullable=False)
    width = db.Column(db.String(300), nullable=False)
    high = db.Column(db.String(300), nullable=False)
    ID_Poultry = db.Column(db.Integer, db.ForeignKey('poultry.id'), nullable=True)
    sensory = db.relationship('Sensory', backref='sensory_salon', lazy=True)
    actuator = db.relationship('Actuator', backref='actuator_salon', lazy=True)


"""
CREATE TABLE dbo.Sensory (
  ID varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
  Name varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  LocationPointX varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  LocationPointY varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  Type varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  ValueLow varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  Icon varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  ValueHigh varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  ID_Salon varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
  CONSTRAINT Sensory_new_pk PRIMARY KEY CLUSTERED (ID)
    WITH (
      PAD_INDEX = OFF, IGNORE_DUP_KEY = OFF, STATISTICS_NORECOMPUTE = OFF,
      ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
)
"""


class Sensory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(30), nullable=False)
    LocationPointX = db.Column(db.String(30), nullable=False)
    LocationPointY = db.Column(db.String(30), nullable=False)
    Type = db.Column(db.String(30), nullable=False)
    ValueLow = db.Column(db.String(30), nullable=False)
    Icon = db.Column(db.String(30), nullable=False)
    ValueHigh = db.Column(db.String(30), nullable=False)
    ID_Salon = db.Column(db.Integer, db.ForeignKey('salon.id'), nullable=True)
    action_sensory = db.relationship('ActionSensory', backref='action_sensory', lazy=True)


"""
CREATE TABLE dbo.Actuator (
  ID varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
  Name varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  LocationPointX varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  LocationPointY varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  Type varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  VlaueBoundLow varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  VlaueBoundHigh varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  Icon varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  Id_Salon varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  CONSTRAINT Actuator_new_pk PRIMARY KEY CLUSTERED (ID)
    WITH (
      PAD_INDEX = OFF, IGNORE_DUP_KEY = OFF, STATISTICS_NORECOMPUTE = OFF,
      ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
)
"""


class Actuator(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(30), nullable=False)
    LocationPointX = db.Column(db.String(30), nullable=False)
    LocationPointY = db.Column(db.String(30), nullable=False)
    Type = db.Column(db.String(30), nullable=False)
    ValueBoundLow = db.Column(db.String(30), nullable=False)
    ValueBoundHigh = db.Column(db.String(30), nullable=False)
    Icon = db.Column(db.String(30), nullable=False)
    Id_Salon = db.Column(db.Integer, db.ForeignKey('salon.id'), nullable=False)
    action_actuator = db.relationship('ActionActuator', backref='action_actuator', lazy=True)


"""
CREATE TABLE dbo.ActionSensory (
  ID varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
  ID_Sensory varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  Time datetime NULL,
  Value numeric(18, 0) NULL
)
"""


class ActionSensory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Time = db.Column(db.DateTime, nullable=False)
    Value = db.Column(db.Numeric(18, 0), nullable=False)
    ID_Sensory = db.Column(db.Integer, db.ForeignKey('sensory.id'), nullable=False)


"""
CREATE TABLE dbo.ActionActuator (
  ID varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
  ID_Actuator varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
  Time datetime NOT NULL,
  Value numeric(18, 0) NOT NULL,
  CONSTRAINT ActionActuator_new_pk PRIMARY KEY CLUSTERED (ID)
    WITH (
      PAD_INDEX = OFF, IGNORE_DUP_KEY = OFF, STATISTICS_NORECOMPUTE = OFF,
      ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
)
"""


class ActionActuator(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Time = db.Column(db.DateTime, nullable=False)
    Value = db.Column(db.Numeric(18, 0), nullable=False)
    ID_Actuator = db.Column(db.Integer, db.ForeignKey('actuator.id'), nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    phone_number = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)


# Database setup


def init_sqlite_db():
    conn = sqlite3.connect('users.db')
    print("Opened database successfully")

    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    print("Table created successfully")

    # Check if the default user already exists
    cursor = conn.execute(
        "SELECT * FROM users WHERE email = 'ali.hamidi4859@gmail.com'")
    user = cursor.fetchone()

    if user is None:
        # Insert the default user
        hashed_password = generate_password_hash(
            '12345678', method='pbkdf2:sha256')
        conn.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                     ('farnaz', '20derakhshani@gmail.com', hashed_password))
        conn.commit()
        print("Default user inserted successfully")
    else:
        print("Default user already exists")

    conn.close()


init_sqlite_db()


@app.route('/')
def home():
    return render_template('login.html', image_path=image_path)


@app.route('/register-page/')
def register_page():
    return render_template('./register.html', image_path=image_path)


@app.route('/register/', methods=['POST'])
def register():
    try:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(
            password, method='pbkdf2:sha256')

        with sqlite3.connect('users.db') as con:
            cur = con.cursor()
            cur.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                        (username, email, hashed_password))
            con.commit()
            flash('User registered successfully!', 'success')
            return redirect(url_for('home'))

    except sqlite3.Error as e:
        flash('Error: ' + str(e), 'danger')
        return redirect(url_for('home'))


@app.route('/register-orm/', methods=['POST'])
def register_as_orm():
    username = request.form['username']
    email = request.form['email']
    phone_number = request.form['phone_number']
    password = request.form['password']
    hashed_password = generate_password_hash(
        password, method='pbkdf2:sha256')

    if username and email and password:
        new_user = User(
            username=username,
            email=email,
            phone_number=phone_number,
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))


@app.route('/login/', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    with sqlite3.connect('users.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cur.fetchone()

        if user and check_password_hash(user[3], password):
            session['user_id'] = user[0]
            session['username'] = user[1]
            flash('successful!', 'success')
            print("Redirecting to dashboard")
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials!', 'danger')
            return redirect(url_for('home'))


@app.route('/login-orm/', methods=['POST'])
def login_as_orm():
    email = request.form['email']
    password = request.form['password']

    selected_user = User.query.filter_by(email=email).first()
    # selected_user = User.query.get(email=email)

    print('this is my method')

    if check_password_hash(selected_user.password, password):
        session['user_id'] = selected_user.id
        session['username'] = selected_user.username
        flash('successful!', 'success')
        return redirect(url_for('dashboard'))
    else:
        flash('Invalid credentials!', 'danger')
        return redirect(url_for('home'))


class SensorForm(FlaskForm):
    Name = StringField('name', validators=[DataRequired()])
    LocationPointX = StringField('X coordinates', validators=[DataRequired()])
    LocationPointY = StringField('Y coordinates', validators=[DataRequired()])
    Type = StringField('type', validators=[DataRequired()])
    ValueLow = StringField('Low value', validators=[DataRequired()])
    Icon = StringField('Icon', validators=[DataRequired()])
    ValueHigh = StringField('Valuable amount', validators=[DataRequired()])
    addSensor = SubmitField('Add sensor')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    print("In dashboard route")
    if 'user_id' in session:
        print(f"User ID in session: {session['user_id']}")

        form = SensorForm()

        if form.validate_on_submit():
            new_sensor = Sensory(
                Name=form.Name.data,
                LocationPointX=form.LocationPointX.data,
                LocationPointY=form.LocationPointY.data,
                Type=form.Type.data,
                ValueLow=form.ValueLow.data,
                Icon=form.Icon.data,
                ValueHigh=form.ValueHigh.data,
            )

            db.session.add(new_sensor)
            db.session.commit()

            return redirect(url_for('dashboard'))

        else:
            print('form is not valid')

        if request.method == 'GET':
            sensors = Sensory.query.all()

            salons = Salon.query.all()

            print(sensors)

            return render_template('home.html', username=session['username'], form=form, sensors=sensors, salons=salons)
    else:
        flash('You need to login first', 'danger')
        return redirect(url_for('home'))


@app.route('/logout/')
def logout():
    session.clear()
    flash('You have been logged out!', 'info')
    return redirect(url_for('home'))


class SalonForm(FlaskForm):
    Name = StringField('name', validators=[DataRequired()])
    Sourface = StringField('sourface', validators=[DataRequired()])
    Hight = StringField('hight', validators=[DataRequired()])
    LocationPointX0 = StringField('LocationPointX0', validators=[DataRequired()])
    LocationPointY0 = StringField('LocationPointY0', validators=[DataRequired()])
    LocationPointX1 = StringField('LocationPointX1', validators=[DataRequired()])
    LocationPointY1 = StringField('LocationPointY1', validators=[DataRequired()])
    LocationPointX2 = StringField('LocationPointX2', validators=[DataRequired()])
    LocationPointY2 = StringField('LocationPointY2', validators=[DataRequired()])
    LocationPointX3 = StringField('LocationPointX3', validators=[DataRequired()])
    LocationPointY3 = StringField('LocationPointY3', validators=[DataRequired()])
    image = StringField('image')
    # image = StringField('image', validators=[DataRequired()])
    # image = FileField('Image', validators=[DataRequired()])
    length = StringField('length', validators=[DataRequired()])
    width = StringField('width', validators=[DataRequired()])
    high = StringField('height', validators=[DataRequired()])
    # ID_Poultry = IntegerField('ID Poultry', validators=[DataRequired()])
    # sensory = FieldList(FormField(SensoryForm), min_entries=1)
    # actuator = FieldList(FormField(ActuatorForm), min_entries=1)
    submit = SubmitField('Submit')


import base64


@app.route('/add-salon/', methods=['GET', 'POST'])
def add_salon():
    form = SalonForm()

    if form.validate_on_submit():
        image_file = request.files['image']

        print(f'image is {image_file}')

        if image_file:
            image_data = image_file.read()

            with open(f'static/uploads/{image_file.filename}', 'wb') as f:
                f.write(image_data)

        print(image_file.filename)

        new_salon = Salon(
            Name=form.Name.data,
            Sourface=form.Sourface.data,
            Hight=form.Hight.data,
            LocationPointX0=form.LocationPointX0.data,
            LocationPointY0=form.LocationPointY0.data,
            LocationPointX1=form.LocationPointX1.data,
            LocationPointY1=form.LocationPointY1.data,
            LocationPointX2=form.LocationPointX2.data,
            LocationPointY2=form.LocationPointY2.data,
            LocationPointX3=form.LocationPointX3.data,
            LocationPointY3=form.LocationPointY3.data,
            image=f'static/uploads/{image_file.filename}',
            length=form.length.data,
            width=form.width.data,
            high=form.high.data,
        )

        db.session.add(new_salon)
        db.session.commit()

        return redirect(url_for('add_salon'))
    else:
        print('Form is not valid')

    return render_template('map.html', form=form)


class MyHomeView(AdminIndexView):
    @expose('/')
    def index(self):
        arg1 = 'Hello'
        return self.render('admin/index.html', arg1=arg1)


# admin = Admin()

admin = Admin(app, name='admin', template_mode='bootstrap4', index_view=MyHomeView())
# admin = Admin(app, name='admin', template_mode='bootstrap4')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Salon, db.session))
admin.add_view(ModelView(Poultry, db.session))
admin.add_view(ModelView(Sensory, db.session))
admin.add_view(ModelView(Actuator, db.session))
admin.add_view(ModelView(ActionSensory, db.session))
admin.add_view(ModelView(ActionActuator, db.session))

# region MQTT

import subprocess


@app.route('/sensor-list')
def sensor_list():
    sensors = Sensory.query.all()
    return render_template('sensor_list.html', sensors=sensors)

@app.route('/sensor-control/<sensor_id>')
def sensor_control(sensor_id):
    sensor = Sensory.query.filter_by(id=sensor_id).first()
    return render_template('sensor_detail.html', sensor=sensor)


@app.route('/mqtt-control/', methods=['GET', 'POST'])
def mqtt_control():
    return render_template('mqq_control_page.html')


# end region


if __name__ == '__main__':
    app.run(debug=True)
