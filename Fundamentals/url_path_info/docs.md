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
Now we are going to have the decorators to define our routes and http method to be used which is simply `GET`
```python
@app.routes("/user/<string:name>", methods=["GET"])
```

