# HackEps2023
<img align="left" src="https://github.com/maariafarelo/HackEps2023/assets/114859584/4f16c887-741b-4725-91df-6065d516967d" height=275px>

## Resum:
Projecte creat durant la HackEPS2023, la qual tracta d'una webapp que formalitza el feedback dels usuaris per obtenir, d'una frase aparentment mancant de sentit, una funcionalitat llesta per enviar a l'equip de desenvolupament de l'eina corresponent d'Ingroup.

## Database:
In order to run the database you need to execute the following command: 
```bash
cd backend/db
docker build -t ifm-db .
docker run -e POSTGRES_PASSWORD=${PASSWORD} -p 5432:5432 -d ifm-db  
```
