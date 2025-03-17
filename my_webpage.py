from fastapi import FastAPI
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
            <a href="/next">Next Page</a>
        </body>
    </html>
    """

@app.get("/next", response_class=HTMLResponse)
def next():
    return """
    <html>
        <head>
            <title>Thank You</title>
        </head>
        <body>
            <h2 style="color:green">Thank you for visiting!</h2>
            <a href="/">Back to Home</a>
        </body>
    </html>
    """
