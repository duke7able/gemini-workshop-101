# FastAPI Career Path Recommendation API

This repository contains a simple FastAPI application that provides career path recommendations based on user input. The API accepts a user's name, skills, and career goal to generate personalized recommendations.

## Features

- **GET /recommendation**: Accepts `name`, `skills`, and `goal` parameters and returns career path recommendations.

## Installation

To run this application, you need to have Python installed. Follow the steps below to set up and run the API.

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-repository.git
cd your-repository
```
### Step 2: Create a Virtual Environment
It's a good practice to use a virtual environment to manage dependencies. You can create one using the following command:

```
python -m venv env
```

## Activate the virtual environment:

# On Windows:

```
.\env\Scripts\activate
```

# On macOS and Linux:

```
source env/bin/activate
```

### Step 3: Install Dependencies

# Install FastAPI and Uvicorn using pip:

```
pip install fastapi uvicorn
```

### Running the API


## To start the FastAPI server, use the following command:

```
uvicorn main:app --host 0.0.0.0 --port 8080
```

This will start the server on `http://localhost:8080`

### Usage

You can access the recommendation endpoint using the following URL format:

```
http://localhost:8080/recommendation?name=John&skills=Python&goal=DataScientist
```
OR

```
http://0.0.0.0:8080/recommendation?name=John&skills=Finance&goal=Banker
```

Replace John, Python, and DataScientist with your desired values for name, skills, and goal.
