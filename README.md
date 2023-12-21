# Data Analysis and Visualization
## Number of drugs (cocaine) seizures

In the context of the Coursera's [Python for Everybody Specialization](https://www.coursera.org/programs/programme-d-apprentissage-b61eq/specializations/python),
I made an app that allows to visualize the average number of drugs (cocaine) seizures in Europe, over the 
years 2002 to 2021.

The dataset can be found here: https://www.emcdda.europa.eu/data/stats2023/szr_en#displayTable:SZR-1-3-1

Here's a screenshot of the final result (front-end application):
![alt text for screen readers](/screenshots/screenshot.PNG)

These are the steps I implemented for the project:
1. Crawl a HTML page containing the dataset (https://www.emcdda.europa.eu/data/stats2023/szr_en#displayTable:SZR-1-3-1)
2. Store data in local DB (sqlite)
3. Clean and format the data, including fetching the countries coordinates from Google Maps Geocoding API
4. Store the final data in a separate local DB
5. Provide the data to the front end application through a javascript file ️
6. Implement the data visualization front-end application with leaflet.js


Thanks a lot for your attention and your potential feedback!
