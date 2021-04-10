endpoints, HTTP methods and HTTP codes
======================================
users
    POST 201 # ok
    GET 200 # ok
    PATCH 200 # ok
    DELETE 204 # ok
login
    POST 201 # ok
    # GET
    # PATCH
    DELETE 204 # ok
one-time-tasks
    POST 201 # ok
    GET 200 # ok
    PATCH 200 # ok
    DELETE 204 # ok


foreign keys
============
id (in the users table)
–id in user_sessions
–userId in one_time_tasks
