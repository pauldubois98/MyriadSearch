from flask import Flask, request

app = Flask(__name__, static_url_path='')

@app.route('/')
@app.route('/index')
def index():
    f = open("search_page.html", 'r')
    page=f.read()
    f.close()
    return page


@app.route('/search')
def query():
    query = request.args.get('q')
    return "hello, you searched:<br>\n"+query




if __name__ == "__main__":
    app.run()
