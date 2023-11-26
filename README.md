# HackEps2023

## Database
In order to run the database you need to execute the following command: 
```bash
cd backend/db
docker build -t ifm-db .
docker run -e POSTGRES_PASSWORD=${PASSWORD} -p 5432:5432 -d ifm-db  
```