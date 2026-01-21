# Understanding FastAPI
Note to me: Forget learning by taking random notes that you won't understand. Instead focus on the concept, build a mental model, use an example, then mutate.

__What is FastAPI and what problem does it solve?__
FastAPI is a high-performance web framework for creating APIs using the Python language. It created by Sebastián Ramirez as he wanted to combine the features of Starlette (web) and Pydantic (data). Additionally, `Typer` was also created as a CLI API. FastAPI was built on top of Python's type hints, which allows data validation, serialisation, and documentation.
__Why does it exist when Flask already exists?__

__Why is async a first-class citizen?__

__What is FastAPI actually doing under the hood?__

Install FastAPI:
```bash
# This method ensures it works on all terminals and OS
pip install "fastapi[standard]"
```
```bash
# Run in development mode
fastapi dev ping.py

# Run in production mode
fastapi run ping.py
```
`N.B`: Two links would be provided: one with documentation and the other, the actual response. Dont forget to add the "/[address]" when testing the links.

Learning Loop:
1. What problem does this solve?
2. Where does it live in the system?
3. What breaks if I remove it?
4. What trade-off does it make?

⚠️ IMPORTANT GUARDRAILS:
- Never learn two phases at once
- Never move forward without explaining why
- Never optimize early
- Never chase completeness
- Calm understanding beats speed

Learning Objectives:
- [Intro and Control](#phase-1--orientation--control)

## PHASE 1 — ORIENTATION & CONTROL
`Goal`: Understand what FastAPI is doing when a request hits the server.

These concepts give you ground. Do not skip them.
1. FastAPI application object
2. Request → response lifecycle
3. Path operations (GET, POST, PUT, DELETE)
4. Path parameters
5. Query parameters
6. Status codes
7. JSON serialization
8. Request and Response objects

✔️ After this phase, you should be able to:
- Explain what happens when a request arrives
- Predict why a 404 or 422 happens
- Build a tiny API without guessing

### FastAPI Application Object
The application object acts as the __central hub__ of the web system where it maps different parts together. It receives incoming HTTP requests, forwards them to the correct route, and coordinates validation, dependencies, and responses. Without the object, there would just be a bunch of code essentially doing nothing as they do not have a conductor to direct them to the problem that they need to solve. In real world systems, servers need a stable entry point for constant requests which the app object allows as it communicates with the server processes. FastAPI adopts a design suited for clarity through the use of explicit application instances (`app = FastAPI()`) which aids with:
- __Testing__: It makes testing the object easy to ensure it forwards and receives the correct requests without needing to run the entire system.
- __Modularization__: The objects can be easily separated.
- __Discovery__: It informs the web-server where to find the logic by the server simply searching for the object's name (app).
- Configuration is centralised and routes can be registered deliberately.

🧠 Mental Model: The app instance exists before any requests. It's a funnel which everything runs through and the routing functions do not run on their own.
```bash
Uvicorn (server)
 → FastAPI app object
   → routing table
     → validation
       → your function
         → response
```
_The app is not the code, the code plugs into the app_

It's a very simple system to set up:
```python
from fastapi import FastAPI

app = FastAPI() # Object: that't the funnel
```
FastAPI is a class that creates an application __container__ where `app` is an instance of the class that will hold configurations, store registered routes, and manage middleware and dependencies. It provides a callable `ASGI` application for the server to communicate with. The app instance is the front door to the backend as:
- frontend requests targets it
- databases: the app manages lifecycle hooks
- HTTP requests are handed to the app by the server

_Routes are not global, they only exists within a specific app instance_

### Lifecycle: Request -> Response
The __lifecycle__ is a round trip that starts outside of the code defining how a single request travels through the system. When clients send a message the server must be able to receive, interpret, make a decision, and return something meaningful. Without a defined lifecycle, systems become unpredictable and debugging becomes a nightmare. This issue is important in the real world because production systems may fail at specific points, where a defined lifecycle makes it easier to determine where the issue may arise. FastAPI is designed with correctness, safety, and observability, allowing a lifecycle to be layered through:
- validation before logic
- dependencies before execution
- serialisation after execution

🧠 Mental Model:
```bash
Client
 → HTTP request
 → ASGI server (Uvicorn)
 → FastAPI app
   → middleware
     → routing
       → validation
         → dependencies
           → your path function
             → response creation
               → serialization
 → HTTP response
```
__Many steps occur before and after any function is run, where errors can arise before code execution__

The lifecycle control whether the code in the file is allowed to run.

### Path Operations
Path Operations like `GET`, `PUT`, `DELETE`, and `POST` allows to declare intent to a system as requests can be different.
|Client Needs  | Server needs |
|:------------:|:------------:|
|<ul> <li>read data</li> <li>create data</li> <li>update data</li> <li>delete data</li> </ul> | <ul> <li>distinguish intent</li> <li>apply specific rules</li> <li>avoid misuse</li> </ul> |

Path operations ensures a specific action is taken as it pairs: __a URL path + an HTTP method__. Methods provide predictability and safety as without them:
- Every request would look identical
- Reads could accidentally mutate data
- Caching would be impossible
- Security rules would be vague

FastAPI aligns strictly with HTTP semantics which allows automatic documentation, accurate client behaviour, and tooling support:
- @app.get() means “retrieve”
- @app.post() means “create”
- @app.put() means “replace/update”
- @app.delete() means “remove”
- __Secondary Operators__: The middleware or browser handles most of them:
  - @app.options() used for toolings and browsers, CORS requests, and capability discovery
  - @app.head() used for caching and metadata verification
  - @app.patch()
  - @app.trace()

🧠 Mental Model: Think in pairs
```bash
(PATH, METHOD) → function # Routing Concept
(METHOD, PATH) -> function # Syntax
```
`Routing` is path + method.
```python
# FastAPI register two routes
# A wrong method equals an automatic error
from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
def get_items():
    return {"action": "read"}

@app.post("/items")
def create_item():
    return {"action": "create"}
```

### Path Parameters
Path parameters allow the __URL__ to provide meaning itself. Static paths like "/items" only provide categories while real-world system may need specific things like users, orders, and addresses. Path parameters solve this by embedding `identity` directly into the URL like _items number 6_. Path parameters allow URLs to be readable, bookmarkable, and semantically rich. Without them:
- every request would need query strings or bodies
- URLs would lose meaning
- caching and debugging would degrade
- APIs would feel opaque

FastAPI treats path parameters as mandatory, positional, and type-validated which matches with how identity works: an ID must exists, it must be valid, it must be understood before logic runs.

🧠 Mental Model: Think of path paremters as patterns and not strings.
FastAPI does:
- pattern match
- extract item_id
- validate its type
- inject it into your function

_Your function receives meaning, not raw text_
```bash
/items/{item_id}
# At runtime
/items/06
```

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}") # declares variable in path
def read_item(item_id: int): # declares type contract
    return {"item_id": item_id}
```
FastAPI extracts the value from the URL, converts it to _int_, and rejects invalid input before execution. This allows the function to receive a clean value.

__SYSTEM CONNECTION (ZOOM OUT)__:
- __HTTP__: URLs encode identity
- __Databases__: Path parameters often map to primary keys
- __Frontend__: UI navigation naturally maps to path parameters
- This is the backbone of RESTful design.

`Pydantic` performs all the data validation under the hood

### Query Parameters
Query parameters allow optional, flexible input without changing the resource itself. It addresses how something should be viewed. It provides a way to filter, sort, or paginate (number) a response.

🧠 Mental Model: Give me this thing (path), but with these preferences (query)
```bash
/items/06?include_reviews=true
# It is the set of key value pairs in the URL after "?"
# ...separated by "&"
http://127.0.0.1:8000/items/?skip=0&limit=10
```

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {"limit": limit}
```
_GET /items?_ and _GET /items/?skip=2&limit=5/_ will go to the same route but return different behavior, as these are not default values that were declared as the paramters. It a value is not given for the parameter, then it is __required__ and no longer optional:
```python
def read_items(limit: int):
```
A simple query of _GET/items/_ would not work as FastAPI would enforce the contract where a value is needed. The order of query parameters do not matter but the name of them do. They aren't positional paramters but rather `named` ones.

They are normally mapped to database filters, pagination, sorting, and feature toggles:
```sql
SELECT * FROM items LIMIT 10 OFFSET 20;
```

### Request Body
A request body is data that is sent to the API from the client, it defines _with what data_. They allow intent and structure to be carried into the system as they can address structured data, large payloads, sensitive information, and complex objects. Operations such as __POST__, __PUT__, __DELETE__, and __PATCH__ use request bodies because they require data, structure, and validation.

🧠 Mental Model: Think of HTTP like a postal system:
- _path -> address_
- _query -> instructions_
- _body -> package_
- A package allows the system to remember something

Request bodies are declared with Pydantic models by importing the `BaseModel` class: [Example](../fastapi_practice/code_practice/phase1/reqbody.py). If a data type is defined without the None it is `required` data for the request, otherwise a `422` error will occur.
```python
description: str | None = None # optional, no error is missing
name: str # required
```
Additionally, if the data type is violated like an int is given where a string is required, the function will never execute and a 422 error will occur.

__Pydantic__ is used to create models because it provides schema of intent:
- define structure
- enforce correctness
- document your API automatically
- become reusable building blocks

The request body may have a few status codes that express outcomes:
- `200`: Okay, the __PUT__ request was successful
- `201`: Created(POST)
- `400`: Malformed request
- `422`: Invalid body

Request bodies allow APIs to move from read-only to `stateful systems` as they map to databases, domain objects, and business rules. It's the part of backend development that allows you to clearly define what lives the system.

### Response Body and Status Code
Response bodies and status codes make APIs trustworthy, where response bodies define API contracts, decouple frontend and backend, and allow independent evolution, while status codes guide client behaviour, integrate with tooling, and reduce ambiguity(doubtfulness). For the response body use the `response_model` parameter with an __OUT__ object: [Example](../fastapi_practice/code_practice/phase1/resmodel.py). It enforces security by habit.

__Status codes__ tells the client:
- whether to retry
- whether to cache
- whether to show errors
- whether logic should continue

|Group   | Types |
|:-----:|:-----------|
|`Information`| <ul> <li>__100__: Generic</li> </ul> |
|`Success` | <ul> <li>__200__: Okay, standard success</li> <li>__201__: Created</li> <li>__204__: No Content (success, no body)</li> </ul> |
|`Redirect`| <ul> <li>__304__: Not Modified</li> </ul> |
|`Client` | <ul> <li>__400__: Bad Request</li> <li>__401__: Not authorised</li> <li>__403__: Forbidden</li> <li>__404__: Not Found</li> <li>__422__: Can't process (validation failed)</li> </ul> |
|`Server` | <ul> <li>__500__: Bug (internal server error)</li> <li></li> <li>__503__: Service unavailable (temporary failure)</li> </ul> |

Status codes are a parameter of the decoration and not of the function:
```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}

# This can also be used: status_code=status.HTTP_201_CREATED
```
### JSON Serialisation
It is the act of converting Python object to JSON data. This is important beause HTTP communicates in bytes that are structured as JSON and not any specific programming language. FastAPI can serialise Python data types like:
- int, str, float, bool, dict, list, and None
- __Cannot Serialise__: sets, tuples, datetime, database session, generator, file handle, custom object

Serialisation forces discipline:
- APIs must speak a shared language
- internal representations must be translated
- boundaries stay clean

`Pydantic` aids with this by guaranteeing data shape, validating data before serialisation, and converting comples Python objects to serialisable data.

Datetime object can be serialised by using `isoformat()` method:
```python
@app.get("/time-fixed")
def time_fixed():
    return {"now": datetime.now().isoformat()}
```
When an object of type X is not serialised, ask:
1. What Python concept am I using?
2. Does JSON understand it?
3. How do I translate it?

### Request and Response Objects
They exist for moments when the raw data needs to be controlled or viewed. FastAPI typically abstracts the data that HTTP contains like metadata, headers, cookies, raw bytes, and method information. The [Request](../fastapi_practice/code_practice/phase1/reqobject.py) and [Response](../fastapi_practice/code_practice/phase1/resobject.py) objects allow these to be viewed. The __Request__ object contains _immutable, read-only_ data that cannot be changed but observed. The body can be accessed manually:
```python
@app.post("/raw")
async def raw_body(request: Request):
    body = await request.body()
    return {"raw_bytes": body.decode()}
```

__Response__ control is needed on cases of:
- setting cookies
- controlling caching
- sending custom headers
- returning non-standard status codes
- integrating with external systems

__N.B__: Use Request/Response sparingly and intentionally.

__pycache__ contains Python’s temporary compiled files and should never be version-controlled.


## PHASE 2 — DATA AS CONTRACT
`Goal`: Understand why FastAPI feels “strict” and why that’s a feature.
This phase is about trust between systems.
1. Pydantic models (deeply)
2. Request body parsing (why it feels strict)
3. Field validation rules
4. Type hints as contracts
5. Automatic error responses
6. Input vs output schemas
7. Response models as boundary protection

✔️ After this phase, you should be able to:

Explain why invalid data is rejected early

Design request/response shapes intentionally

Feel relief when errors happen automatically

PHASE 3 — STRUCTURE & COMPOSITION

(Weeks 3–4)
Goal: Learn how FastAPI avoids tangled code as systems grow.

This is where beginners usually panic. You won’t, because you’ll know why.

Dependency injection (Depends)

Dependency lifetimes

Shared dependencies

Dependency execution order

Dependency overrides (conceptual)

✔️ After this phase, you should be able to:

Explain why global variables are dangerous

Build modular, testable routes

Understand how FastAPI “wires” systems together

PHASE 4 — FAILURE AS SIGNAL

(Week 4)
Goal: Learn how systems communicate problems clearly.

HTTPException

Custom error messages

Validation error handling

Global exception handlers

Logging basics

✔️ After this phase, you should be able to:

Read errors calmly

Decide where errors belong

Explain the difference between client vs server errors

PHASE 5 — IDENTITY & ACCESS

(Weeks 5–6)
Goal: Understand identity without getting lost in security rabbit holes.

Authentication concepts (what it is, not how first)

Password hashing (conceptual)

OAuth2 flow (high level)

Token-based auth (JWT concepts)

Role-based access control

Security dependencies

✔️ After this phase, you should be able to:

Explain how users prove identity

Explain why tokens exist

Protect routes intentionally

PHASE 6 — PERSISTENCE & REALITY

(Weeks 6–7)
Goal: Connect your API to durable memory.

Database concepts (why not files)

ORM mental model

Database sessions

CRUD patterns

Connection management

Async vs sync DB access

✔️ After this phase, you should be able to:

Explain how data lives beyond requests

Build real CRUD APIs

Avoid common DB mistakes

PHASE 7 — TIME & WORK

(Week 7)
Goal: Understand concurrency without fear.

Async vs sync endpoints

Background tasks

Event loop (conceptual)

I/O-bound vs CPU-bound

✔️ After this phase, you should be able to:

Explain why async exists

Decide when to use it

Avoid blocking your app accidentally

PHASE 8 — FLOW & INTERCEPTION

(Week 8)
Goal: Understand cross-cutting concerns.

Middleware concept

Request/response interception

CORS

Timing & logging middleware

PHASE 9 — CONFIGURATION & SAFETY

(Week 8)

Environment variables

Settings management

Secrets handling

Dev vs prod separation

PHASE 10 — TRUST THROUGH TESTING

(Week 9)

Test client

Dependency overrides

Unit vs integration tests

Mocking external services

PHASE 11 — DEPLOYMENT & RUNTIME

(Week 10)

Uvicorn

ASGI servers

Gunicorn (conceptual)

Docker (conceptual)

Reverse proxy (conceptual)

PHASE 12 — COMMUNICATION & DX

(Week 10)

OpenAPI schema

Swagger UI

ReDoc

API versioning

