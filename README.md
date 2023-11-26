# HackEps2023
<img align="left" src="https://github.com/maariafarelo/HackEps2023/assets/114859584/4f16c887-741b-4725-91df-6065d516967d" height=375px>

## Resum:
Projecte creat durant la HackEPS2023, la qual tracta d'una webapp que formalitza el feedback dels usuaris per obtenir, d'una frase aparentment mancant de sentit, una funcionalitat llesta per enviar a l'equip de desenvolupament de l'eina corresponent d'Ingroup.

## Database:
In order to run the database you need to execute the following command: 
```bash
cd backend/db
docker build -t ifm-db .
docker run -e POSTGRES_PASSWORD=${PASSWORD} -p 5432:5432 -d ifm-db  
```

## Inspiració

El tracte amb clients és una tasca que pot arribar a consumir una gran quantitat de temps i recursos en el món laboral. A causa d'això hem buscat una manera d'optimitzar el procés de feedback per facilitar aquest procés i poder invertir aquests recursos en altres tasques. Mitjançant la categorització i priorització automàtica, es poden reduir considerablement les hores invertides en aquest procediment.
## Què fa?

Donat un usuari amb una queixa o suggeriment sobre un producte d'ingroup. S'analitza aquest feedback i s'obté un processat que permet als treballadors de l'empresa tenir d'una forma més visual i agilitzada quines tasques han de fer per millorar els seus productes seguint els suggeriments dels clients.
## Com s'ha desenvolupat?

El projecte està centrat en un frontend desenvolupat sobre el framework de React, que presenta dues pantalles per a dos rols d'usuari diferent, l'usuari base i l'administrador. Per altra banda, el backend està desenvolupat sobre Flask, i proporciona una diversitat d'endpoints per tal de facilitar la comunicació amb el frontend i gestionar les crides a la base de dades, integrada amb PostgreSQL. Finalment, el tractament de dades es gestiona a través d'una integració amb l'API d'OpenAI utilitzant el model de llenguatge gpt-3.5-turbo. El cicle de vida de l'aplicació finalitza amb una integració amb l'eina de gestió de projectes Asana, explotant les funcionalitats de la seva API.
## Reptes amb els quals ens hem encarat

El repte principal que hem trobat és aconseguir tancar un projecte del qual estem orgullosos partint d'un grup de tres participants amb una integrant que s'iniciava en aquesta ocasió a les hackathons i que té un background de programació reduït. Vam voler que l'oportunitat ens funcionés per igual a tots per aprendre, i per això hem optat per tecnologies que no dominàvem, cosa que ha suposat tot un repte.
## Fites de les que estem orgullosos

Estem molt orgullosos de poder haver finalitzat el projecte i portar a terme la majoria de les idees inicials que havíem plantejat, tenint present que l'equip no dominava tecnologies com Flask, React ni integracions amb models de llenguatge com GPT. Finalment, l'aprenentatge residual del desenvolupament de l'aplicació ha estat tot un orgull i és una victòria que ens emportem del projecte.
## Què hem après

Durant el transcurs d'aquest projecte hem après a programar en dos frameworks molt utilitzats com són React i Flask, però que no dominàvem anteriorment, i principalment hem après a fer servir models de llenguatge per a explotar les dades de les quals disposem, cosa que veiem que té molta utilitat en un futur i que utilitzarem en futurs projectes.
## Següents passos per IFM - Ingroup Feedback Manager

IFM és una primera prova de concepte que permet comprovar que l'eina és d'utilitat i que realment estalvia temps en procediments de feedback i gestió de ressenyes, i pretén ser l'impuls d'una aplicació a major escala que incorpori més funcionalitats i la integració amb altres eines, permetent l'ampliació a multituds d'empreses i equips independentment de les metodologies que s'emprin.
