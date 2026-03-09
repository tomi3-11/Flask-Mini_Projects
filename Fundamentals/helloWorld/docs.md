# Creating a simple hello world app

here is jst creating a simple hello world app that returns a dictionary jst like any api would do.

## Implementation
here we jst implement the hello app

The code below only imports the `Flask` framework class so as we can start using it
```python
from flask import Flask
```

The next is creating and object of the Flask class, also class instanciating a class.<br>
if wondering about the `__name__`: it simply makes all the contents of the Flask framework availble to us.
```python
app = Flask(__name__)
```

Next we use decorators to create our routes with a `GET` http method.
```python
@app.route("/", methods=["GET"])
```

next we create our view function that is responsble for our route logic and behaviour
```python
def index():
    return {
        "message": "Hello from flask 2026! :)"
    }
```

Now finally you run the application from the root dir, be sure you are inside an activated virtual environment.
```sh
flask run
```

You can access it via this and get the output,
```sh
http://127.0.0.1:5000
# OR
http://localhost:5000
```


Nice one, now you have your very first hello app

documented by: [Tomi](https://github.com/tomi3-11)
