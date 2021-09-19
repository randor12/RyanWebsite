from flask import *

application = app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = 'asdjfksa'

@app.route('/', methods=['GET', 'POST'])
def index():
    # GET Request for Index Template 
    print('Home Page')
    return render_template('index.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    # About page
    print("About Page")
    return render_template('about.html')

@app.route('/experience', methods=['GET', 'POST'])
def experience():
    # Experience Page
    print('Experience Page')
    return render_template('experience.html')

@app.route('/classes', methods=['GET', 'POST'])
def classes():
    # Class Page 
    print('Class Info')
    return render_template('classes.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    # Contact Page 
    print('Contact Info')
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
