from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)


app.config.update(

    SECRET_KEY = 'praneethraj',
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:qwerty123@localhost:5433/catalog_db',
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)


db = SQLAlchemy(app)

@app.route('/index')
@app.route('/')
def hello_flask():
    return 'Hello Flask'


@app.route('/new/')
def query_strings():
    query_val = request.args.get('greeting')
    return '<h1>the greeting is: {}</h1>'.format(query_val)

@app.route('/user')
@app.route('/user/<name>')
def non_query_strings(name='mina'):
    return 'Hey how are u {}!'.format(name)


# numbers
@app.route('/numbers/<int:num>')
def working_with_numbers(num):
    return '<h1> the number you picked is: ' + str(num) + '</h1>'

# add numbers
@app.route('/add/<int:num1>/<int:num2>')
def adding_integers(num1, num2):
    return '<h1> the sum is : {}'.format(num1 + num2) + '</h1>'


# floats
@app.route('/product/<float:num1>/<float:num2>')
def product_two_numbers(num1, num2):
    return '<h1> the product is : {}'.format(num1 * num2) + '</h1>'


@app.route('/temp')
def rend_templates():
    return render_template('hello.html')

@app.route('/me')
def my_names():
    names_me = ['praneeth','metuku','praneethraj','bunny']
    return render_template('me.html',any_name=names_me,two_any_name='praneethmetuku')

@app.route('/aboutme')
def about_me():
    my_electronics = {'ipad':'apple 7th generation',
                      'phone':'Google pixel 2xl',
                      'laptop':'Dell',
                      'Headphones':'Sony wh-1000xm3'}
    return render_template('aboutme.html',my_electronics=my_electronics)

class Publication(db.Model):
    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self,name):

        self.name = name

    def __repr__(self):

        return 'the id is {} and the name is {}'.format(self.id,self.name)


class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String(400), nullable=False, index=True)
    author = db.Column(db.String(290))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(786))
    image = db.Column(db.String(232), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())
    #relationship

    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))


    def __init__(self,title,author,avg_rating,format,image,num_pages,pub_id):

        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id


    def __repr__(self):
        return '{} by {}'.format(self.title,self.author)









if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)