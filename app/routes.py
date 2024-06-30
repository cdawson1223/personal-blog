from app import app
from flask import render_template, request, redirect, url_for

@app.route('/')
@app.route('/index')
def index():
    return render_template('homepage.html', title='Home')

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.form['BackgroundButton'] == 'clicked': #this one is the problem 
        print("Background button clicked")
        return render_template('background.html', title='Home')
    if request.form['AIEButton'] == 'clicked': #this one is the problem 
        print("AIE button clicked")
        return render_template('background.html', title='Home')
    if request.form['PersonalButton'] == 'clicked': #this one is the problem 
        print("PE button clicked")
        return render_template('background.html', title='Home')
    if request.form['PortfolioButton'] == 'clicked':
        print("portfolio ckicked")
        return render_template('portfolio.html', title='Home')
    print("this ran")
    if request.form['HomeButton'] == 'clicked':
        return render_template('homepage.html', title='Home')
    return render_template('homepage.html', title='Home')

'''@app.route('/submit', methods=['POST'])
def submit():
    if request.form['BackgroundButton'] == 'clicked':
        print("this ran")
        return render_template('background.html', title='Home')'''

@app.route('/background', methods=['GET','POST'])
def background():
    if request.form['BackgroundButton'] == 'clicked':
        print("this ran")
        return render_template('background.html', title='Home')


@app.route('/internships',methods=['GET','POST'])
def academic_industry():
    #if request.form['HomeButton'] == 'clicked': #this part is the issue 

       
    if request.form['AIEButton'] == 'clicked':
        print("this button be clickin")
        return render_template('academic_industry.html', title='Home')

@app.route('/personal',methods=['GET','POST'])
def personal_interests():
    #if request.form['HomeButton'] == 'clicked':
     #   return render_template('homepage.html', title='Home')
    if request.form['PersonalButton'] == 'clicked':
        return render_template('personal_interests.html', title='Home')

@app.route('/portfolio',methods=['GET','POST'])
def portfolio():
    if request.form['PortfolioButton'] == 'clicked':
        print("trying this")
        return render_template('portfolio.html', title='Home')

@app.route('/backhome',methods=['GET','POST'])
def backhome():
    if request.form['HomeButton'] == 'clicked':
        return render_template('homepage.html', title='Home')

'''@app.route('/academic_industry')
def index():
    return render_template('academic_industry.html', title='Home')'''

