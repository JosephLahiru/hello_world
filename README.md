# Flask App with Vulnerability Analysis

A simple Flask application with a "hello world" endpoint and integrated vulnerability analysis.

## Features

- Flask API with health check endpoint
- Vulnerability analysis workflow
- Code quality checks
- Automated testing
- Endpoint testing

## Endpoints

|
Method
|
Path
|
Description
|
|

---

## |

## |

|
|
GET
|
`/hello`
|
Returns "hello world"
|
|
GET
|
`/health`
|
Returns application health status
|

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/flask-app.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
cd app
python -m flask run
```

4. Test the endpoints:

```bash
curl http://localhost:5000/hello
curl http://localhost:5000/health
```

## Development

1. Create a feature branch:

```bash
git checkout -b feature/new-feature
```

2. Make changes and test:

```bash
pytest
flake8 app
```

3. Commit changes:

```bash
git add .
git commit -m "Add new feature"
git push origin feature/new-feature
```

4. Create pull request against main branch
