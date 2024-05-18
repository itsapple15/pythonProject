from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Your existing routes go here

@app.route('/search')
def search():
    query = request.args.get('q', '')
    if query:
        # Redirect to Google search with the query parameter
        return redirect(f"https://www.google.com/search?q={query}", code=302)
    else:
        return "No query provided."

