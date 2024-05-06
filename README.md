# HF-API

The purpose of this API service is to store models from Hugging Face in a DB and expose it via endpoints.


## Docker
Build and start:
```
docker compose up --build
```

Cleanup:
```
docker compose down
```

Cleanup (clean volumes):
```
docker compose down --volumes
```

Build separate docker image:
```
docker build . -f ./api/Dockerfile -t iperezx/hg-api:0.1.0 --platform=linux/amd64
```

## Kubernetes
Create secrets from postgress:
```
kubectl create secret generic hf-env --from-env-file=.env-k8s
```

Create postgres pvc:
```
kubectl apply -f kubernetes/postgres-pvc.yaml
```

Deploy postgres:
```
kubectl apply -f kubernetes/postgres.yaml
```

Deploy api service:
```
kubectl apply -f kubernetes/api.yaml
```


## API Usage:
Get models
```
curl -X GET http://127.0.0.1:8000/v1/models
```