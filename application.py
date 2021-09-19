from flask import *

application = Flask(__name__)
# app.config['TEMPLATES_AUTO_RELOAD'] = True
application.secret_key = 'asdjfksa'

@application.route('/', methods=['GET', 'POST'])
def index():
    # GET Request for Index Template 
    print('Home Page')
    return render_template('index.html')

@application.route('/about', methods=['GET', 'POST'])
def about():
    # About page
    print("About Page")
    return render_template('about.html')

@application.route('/experience', methods=['GET', 'POST'])
def experience():
    # Experience Page
    print('Experience Page')
    return render_template('experience.html')

@application.route('/classes', methods=['GET', 'POST'])
def classes():
    # Class Page 
    print('Class Info')
    return render_template('classes.html')

@application.route('/contact', methods=['GET', 'POST'])
def contact():
    # Contact Page 
    print('Contact Info')
    return render_template('contact.html')

if __name__ == '__main__':
    application.run()
