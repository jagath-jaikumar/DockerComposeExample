# Simple Docker example

## Project Structure

```
.
├── README.md
├── docker-compose.yml
├── server
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
└── tester
    ├── Dockerfile
    ├── requester.py
    └── requirements.txt
```

## Commands:


### Containers:


```
docker build -t server:latest server
docker build -t tester:latest tester
docker run -p 5000:5000 server
docker run tester
```

### Compose:

```
docker-compose build
docker-compose up
```
