from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>VIDHYA</h1>
    <h3>AI Powered Student Learning Platform</h3>
    <p>Welcome to our Hackathon Project</p>
    """

@app.route("/about")
def about():
    return """
    <h2>About VIDHYA</h2>
    <p>VIDHYA helps students learn smarter.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
