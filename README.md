# Colonial Williamsburg Travel Guide 🏛️🌳

## Project Overview
Tourists and new college students, like our group, are visiting Colonial Williamsburg and often do not know where to start. Attractions and dining options, along with the weather variable, are scattered across multiple websites, making it difficult to get a clear picture of what to do and when.  

This dashboard solves that by creating a **centralized travel guide** that brings together the following:
- **Attractions** → curated experiences with images, links, and ratings  
- **Restaurants** → searchable by type of food, with contact info, websites, and ratings  
- **Weather** → live forecasts to help visitors plan their day i.e. if the dashboard recommends busch gardens on a rainy day, the user is going to know it cannot do that 

###  Audience
- Tourists and families visiting  Williamsburg
- New students interested in checking out Williamsburg (like our group)
- Local restaurants wanting to see how they stack up against competition

### Value
- One-stop dashboard for Williamsburg trip planning  
- Real-time, data-driven recommendations with restaurant suggestions and weather 
- User-friendly design with interactive cards, dropdowns, and charts  
---

##  How to Run

### 1. Run Locally
1. Clone this repository.  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt

## Data Sources and Dictionary
** These are the API's we used **
- https://www.visitwilliamsburg.com/things-to-do/museums-and-attractions/
Used for webscraping the attractions
- https://overpass-api.de/api/interpreter
Used API for the restaurants 
- https://api.open-meteo.com/v1/forecast
Used API for getting the weather

** Information regarding the API's **
- All data was most recently accessed 9/10
- In terms of file structure, each page is clearly associated with the given API

** Variables within each API ** 
- With attractions, we pulled in the rating, location, and if it was reccommended by someone
- These variables are all posted on the website
- With restaurants, we pulled in the name, rating, number of reviews, phone number, and website
- These variables are all posted on the website
