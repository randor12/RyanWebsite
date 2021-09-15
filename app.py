from flask import *

app = Flask(__name__)
app.secret_key = 'asdjfksa'

@app.route('/', methods=['GET', 'POST'])
def index():
    # GET Request for Index Template 
    print('Home Page')
    return render_template('index.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    print("About Page")
    return render_template('about.html')

@app.route('/experience', methods=['GET', 'POST'])
def experience():
    print('Experience Page')
    return render_template('experience.html')

@app.route('/classes', methods=['GET', 'POST'])
def classes():
    print('Class Info')
    return render_template('classes.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    print('Contact Info')
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
