# REST API CRUD Operations with Python-Flask and MySQL
The repository will update soon.

For video tutorial [SUBSCRIBE](https://www.youtube.com/techfryday) to,
[TechFryDay](https://www.youtube.com/techfryday)

# Download and setup

Step-1: Creating venv
Step-2: Running application
Powershell
```bash
  > $env:FLASK_ENV = "development"
  > flask run
```



# Common Errors
1. While activating venv this error occures in Windows:

    ```bash
        + CategoryInfo          : SecurityError: (:) [], PSSecurityException
        + FullyQualifiedErrorId : UnauthorizedAccess
    ```
    Solution:
    Execute this command and retry activating venv.
    ```bash
      Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```
