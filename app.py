from flask import *

app = Flask(__name__)
app.secret_key = 'asdjfksa'

@app.route('/', methods=['GET', 'POST'])
def index():
    # GET Request for Index Template 
    return render_template('index.html')


