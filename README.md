# belgianTempHistory
Belgian Temperature Comparison between the years 1981-2010 and 2017-2021. Data science project for answering the question : "Has the temperature in Belgium increased when comparing the two periods 1981-2010 and 2017-2021?". The data consists of average temperatures and daily max and min temperatures in Brugge (province of Occidental Flanders, at the sea) and Marche-en-Famennes (province of Luxemburg). The figure TempHistoryBelgium.png was drawn by python script temp_history_belgium.py to answer the forementioned question.

The data comes from the website www.meteo.be of the IRM (Institut Royal Météorologique).

For the years 1981-2010, the data can be found in the following documents:
- Brugge: https://www.meteo.be/resources/climatology/climateCity/pdf/climate_INS31005_fr.pdf (or brugge_climat.pdf in this repository)
- Marche-en-Famennes: https://www.meteo.be/resources/climatology/climateCity/pdf/climate_INS83034_fr.pdf (or marche_famennes_climat.pdf in this repository)
The table and lines of interest can be found respectively in the files brugge_1981_2010.csv and marche-famennes_1981_2010.csv in this repository.

For the years 2017-2021, the data can be found on the page https://opendata.meteo.be/downloadPage.php by choosing:
- for product: Automatic Weather Stations - observations
- for layer: AWS_1day
- for format: CSV

The file is also present in this repository: belgian_climate_2017_2021.csv. In this file, code 6418 is used for Brugge (Zeebrugge to be precise) and code 6472 is used for Marche-en-Famennes.

What we can conclude from the obtained figure is that the temperature in Belgium is slightly higher during period 2017-2021 compared to period 1981-2010. The temperature increase is more significant (around 4°C) at the sea (Brugge) when considering the mean daily minimum temperature. However, the mean daily maximum temperature has slightly decreased at the sea during the summer when comparing the two periods. In Marche-en-Famennes, which is more inland, both daily min and max temperatures, as well as the mean temperature, have increased during the time considered. One should perform statistical tests to conclude if this temperature increase is statistically significant.
