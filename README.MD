### The basic initial steps
- install virtual env and activate it <i>(env\Scripts\Activate)</i>
- install fastapi and uvicorn as needed to run the application 
- in main.py import fastapi and use its instance to make a simple function 
- run the application <i>(uvicorn main:app)</i>

### Breaking it down 
- app is the instance created to use FASTAPI in the directory 
- what does uvicorn main:app mean? 
- - we all know fast api is a fast web framework for building APIs with Python3.7+ and hence uvicorn is a lightning ASGI(asynchronous server gateway interface) server implementation for running FastAPI applications. 
- - main here represents the name of the main file of the application and app stands for the fastAPI instance we declared in the main file
- - note of main.py was named project.py then we would be running the command like : <i>uvicorn project : app</i>, thus name can be set according to users need. 

- what does @app.get('/') mean?
- - @ represents path decorator 
- - '/' represents the path or more specifically the route to which the user is directed according to there needs . while '/' represents the root path , we could add different paths in the application with there respective name. 
- - .get() reperesents the operation on the path. we can also have other operations like post , delete or put
- - below the operation comes the path operation function defining what function will be applied when the directed path is opened. 

### Path and Query parameters 
- we can pass path parameters like {id} but also to make sure we pass them in function as (id) for them to be directed to that path 
- Just like that we can also pass query parameters and we usually do that by starting the query with '?' in the url and also setting the desired parameters in the function of that path 
- refer to query function in main.py file for this 

### Request Body 
- for request body i.e creating a post request we need to import BaseModel from 'pydantic model'
- using this we can create a class to define what are the necessary values needed during function execution
- make sure to make a request from BaseModel in the function extract things in it
- we can refer to variables using '.' operator 
- refer to 'content class' and 'content function' for this 