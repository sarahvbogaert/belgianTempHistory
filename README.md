# belgianTempHistory
Belgian Temperature Comparison between the years 1981-2010 and 2017-2021. Data science project for answering the question : "Has the temperature in Belgium increased when comparing the two periods 1981-2010 and 2017-2021?". The data consists of average temperatures and daily max and min temperatures in Brugge (province of Occidental Flanders, at the sea) and Marche-en-Famennes (province of Luxemburg)

The data comes from the website www.meteo.be of the IRM (Institut Royal Météorologique).

For the years 1981-2010, the data can be found in the following documents:
- Brugge: https://www.meteo.be/resources/climatology/climateCity/pdf/climate_INS31005_fr.pdf (or brugge_climat.pdf in this repository)
- Marche-en-Famennes: https://www.meteo.be/resources/climatology/climateCity/pdf/climate_INS83034_fr.pdf (or marche_famennes_climat.pdf in this repository)
The table and lines of interest can be found respectively in the files brugge_1981_2010.csv and marche-famennes_1981_2010.csv in this repository.

For the years 2017-2021, the data can be found on the page https://opendata.meteo.be/downloadPage.php by choosing:
- for product: Automatic Weather Stations - observations
- for layer: AWS_1day
- for format: CSV

The file is also present in this repository: belgian_climate_2017_2021.csv

What we can conclude from the obtained figure (TempHistoryBelgium.png) is that the temperature is higher for the latest period, especially the mean daily minimum temperature at the sea (Brugge).
