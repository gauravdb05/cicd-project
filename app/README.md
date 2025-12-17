# CI/CD Project

A production-grade CI/CD pipeline demonstration using Github Actions,Docker,Kubernetes

##Features

- FLASK REST API
- Automated testing with pytest
- Docker containerization
- Complete CI/CD pipeline ( publish soon)

## Project Structure
```
├── .github/
│   └── workflows/
│       ├── tests.yml
│       └── deploy.yml
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── test_utils.py
├── .gitignore
├── requirements.txt
├── Dockerfile
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.11
- pip3
- Flask
- Docker
- pytest

### Run locally

```bash
pip3 install -r requirements.txt
python app.py
```

### Run with Docker
docker build -t cicd-app .
docker run -p 5000:5000 cicd-app


### Running Tests

```bash
pytest tests/
```

### Test

```bash
curl http://localhost:5000/health
curl http://localhost:5000/api/users

## CI/CD Pipeline

Publis soon...

MIT