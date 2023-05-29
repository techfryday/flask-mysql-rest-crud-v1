# REST API CRUD Operations with Python-Flask and MySQL (Version-1)

For video tutorial [SUBSCRIBE](https://www.youtube.com/techfryday) to,
[TechFryDay](https://www.youtube.com/techfryday)

# Download and setup

Step-1: Creating & activating venv
  Windows:
  ```powershell
    python -m venv venv
    ./venv/Scripts/activate
  ```
  
  Linux:
  ```bash
    python -m venv venv
    source venv/bin/activate
  ```

Step-2: Installing Dependencies
  ```bash
    pip install -r requirements.txt
  ```
Step-3: Running application
Windows:
```bash
  > $env:PYTHONDONTWRITEBYTECODE=1;$env:FLASK_APP="app";$env:FLASK_ENV = "development"
  > flask run
```

Linux:
```bash
  > export PYTHONDONTWRITEBYTECODE=1 FLASK_APP="app" FLASK_ENV="development"
  > flask run
```

# Installing Dependencies
  ```bash
    pip install -r requirements.txt
  ```
# Common Issues
1. Creating __pycache__ files
  Windows-powershell-Solution:
  ```bash
    $env:PYTHONDONTWRITEBYTECODE=1
  ```
  Linux:
  ```bash
  export PYTHONDONTWRITEBYTECODE=1
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
