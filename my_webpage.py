from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Home Page</title>
        </head>
        <body>
            <h1 style="color:blue">Welcome to My Website</h1>
            <p>Hello, this is a sample page. </p>
            <a href="/comment">Submit a Comment</a>
        </body>
    </html>
    """

@app.get("/comment", response_class=HTMLResponse)
def comment_page():
    return """
    <html>
        <head>
            <title>Submit Your Comment</title>
        </head>
        <body>
            <h1 style="color:blue">Leave a Comment</h1>
            <form action="/submit" method="post">
                <label for="comment">Your Comment:</label><br>
                <textarea id="comment" name="comment" rows="4" cols="50"></textarea><br><br>
                <button type="submit">Submit</button>
            </form>
        </body>
    </html>
    """

@app.post("/submit", response_class=HTMLResponse)
def submit_comment(comment: str = Form(...)):
    return f"""
    <html>
        <head>
            <title>Thank You</title>
        </head>
        <body>
            <h2 style="color:green">Thank you for your comment!</h2>
            <a href="/">Back to Home</a>
        </body>
    </html>
    """
