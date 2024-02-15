from flask import Flask, redirect, request, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Department, Employee, get_directory, get_directory_join, get_directory_join_class, get_directory_all_join
from forms import AddSnackForm, NewEmployeeForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///employees_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  =  False
app.config['SQLALCHEMY_ECHO'] =  True
app.config['SECRET_KEY'] = "praveen"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
app.app_context().push()


@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/phones')
def list_phones():
    emps = Employee.query.all()
    return render_template('phones.html', emps=emps)


@app.route('/snacks/new', methods=["GET", "POST"])
def add_snack():
    form = AddSnackForm()
    
    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        flash(f"Added {name} at {price}")
        return redirect("/")
    
    else:
        raise
        return render_template("snack_add_form.html", form=form)
    

@app.route('/employees/new', methods=["GET", "POST"])
def add_employee():
    form = NewEmployeeForm()
    depts = db.session.query(Department.dept_code, Department.dept_name)
    choices = [(dept.dept_code, dept.dept_name) for dept in depts]
    form.dept_code.choices = choices
    if form.validate_on_submit():
        name = form.name.data
        state = form.state.data
        dept_code = form.dept_code.data

        emp = Employee(name=name, state=state, dept_code=dept_code)
        db.session.add(emp)
        db.session.commit()
        return redirect('/phones')
    else:
        return render_template('add_employee_form.html', form = form)