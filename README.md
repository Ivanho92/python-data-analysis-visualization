# Data Analysis and Visualization
## Number of drugs (cocaine) seizures

I made an app that allows to visualize the average number of drugs (cocaine) seizure in Europa, over the 
years 2002 to 2021.

The dataset can be found here: https://www.emcdda.europa.eu/data/stats2023/szr_en#displayTable:SZR-1-3-1

Here's a screenshot of the final result (front-end application) for you to have an idea:

The project is actually not finished but here is the full process I eventually want to implement:
- Crawl data from dataset HTML page (https://www.emcdda.europa.eu/data/stats2023/szr_en#displayTable:SZR-1-3-1) >> DONE ✔️
- Parse data >> DONE ✔️
- Store data in DB >> TO DO ✔️
- Model (clean and format) data as necessary >> DONE ✔️
- For each country, fetch the coordinates from Google Maps Geocoding API >> DONE ✔️
- Store the prepared data in DB >> DONE ✔️
- Provide the data to the front end application through some medium (in my case javascript file) >> DONE ✔️
- (optional) : update step 6 by providing a more robust web API so any app could fetch it
- Implement the data visualization front-end application with leaflet.js library >> DONE ✔️

As soon as the project is properly finalized, I'll update this [github repository](https://github.com/Ivanho92/python-data-analysis-visualization).
So stay tuned! :)

Thanks a lot for reading this and your potential feedback!
