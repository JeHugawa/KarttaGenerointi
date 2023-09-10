# Määrittelydokumentti
Projektikieli on Suomi. Opinto-ohjelma on tietojenkäsittelytieteen kandidaatti (TKT).
## ohjelmointikieli
Projekti toteutetaan Pythonilla. Osaan myös Javaa, C++, C#, ja koen että voin vertaisarvioida projekteja myös muilla kielillä tarvittaessa.
## Ohjelmakuvaus
Ohjelman on tarkoitus generoida satunnaisia karttoja. Ohjelmalle annetaan satunnaisavain (halutessaan ohjelma voi arpoa senkin) ja ohjelma luo sen pohjalta kartan. Ohjelmassa voidaan myös kertoa esim. haluttujen jokien määrä.
Ensiksi ohjelma luo korkeuskartan, josta katsotaan meret vuoret yms. Tämä korkeuskartta luodaan käyttäen perlin kohinaa.
Tulvatäyttö (flood fill) algoritmilla täytetään meret yms. alueet niiden korkeuden perusteella.
Sitten luodaan biomit eli alueen tyypit. Tämä tehdään Voronoimalla pisteitä joiden perusteella alueet valitaan.
Viimeisenä toteutetaan jokia Satunnaiskävelyllä (random walk).
## lähteet
- https://en.wikipedia.org/wiki/Perlin_noise
- https://en.wikipedia.org/wiki/Jump_flooding_algorithm voronointia varten
- https://en.wikipedia.org/wiki/Random_walk
- https://en.wikipedia.org/wiki/Flood_fill
