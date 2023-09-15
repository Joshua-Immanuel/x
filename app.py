from flask import Flask, request, render_template


app = Flask(__name__)


# @app.route('/static/<filename>')
# def serve_static(filename):
#   return app.send_static_file(filename)

# @app.route('/')
# def search_form():
#   return render_template('search_form.html')


# @app.route('/')
# def search():
#     query = request.args.get('query')
#     results="hello"
#     return render_template('search_results.html', query=query, results=results)
@app.route('/')
def index():
   return "hello"

if __name__ == '__main__':
  app.run()
