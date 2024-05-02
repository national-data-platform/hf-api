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

## API Usage:
Get models
```
curl -X GET http://127.0.0.1:8000/v1/models
```