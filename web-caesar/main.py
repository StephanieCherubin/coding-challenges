from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
       <form action="/rotate" method="post">
            <label for="RotateBy">Rotate by:</label>
            <input id= "RotateBy" type="text"  name="rot" value = 0><br><br>
            <textarea id="textarea" name="text">{0}</textarea><br>
            <input type="submit" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/rotate", methods=['POST'])
def encrypt():
    text = request.form['text']
    rotate = int(request.form['rot'])
    encrypt = rotate_string(text,rotate)
    return form.format(encrypt)

app.run()