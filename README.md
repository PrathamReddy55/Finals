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
**These are the API's we used**
- https://www.visitwilliamsburg.com/things-to-do/museums-and-attractions/
Used for webscraping the attractions
- https://overpass-api.de/api/interpreter
Used API for the restaurants 
- https://api.open-meteo.com/v1/forecast
Used API for getting the weather

**Information regarding the API's**
- All data was most recently accessed 9/10
- In terms of file structure, each page is clearly associated with the given API

**Variables within each API** 
- With attractions, we pulled in the rating, location, and if it was reccommended by someone
- These variables are all posted on the website
- With restaurants, we pulled in the name, rating, number of reviews, phone number, and website
- These variables are all posted on the website

## AI Assistance 
   The majority of AI assistance we had was used in our styles sheet, however we did have minor help with it in some of our pages. The majority of the work in our pages comes from class examples and/or the presentations Dr. Schlosser had on screen. I will now list on each page how we had AI assist us.

**Attractions Page**
The majority of the attractions page revolves around pulling in from an API and to work around errors we made a dictionary with some of the major attractions in Williamsburg. Here, since we are just returning one of the attractions, it is randomized each time the button is pressed. This is where AI comes into play. In order to showcase the rating on the website, we implemented the use of a shaded star. The shaded star represents how high or low a rating was, a neat and simple touch to convey it to the user. Outside of this, we implemented lots of classNames to help us with styling for the styles sheet on our project. 

**Restaurant Page**
Again, you can see lots of familiarity with what we did in class and the code we have presented. Similarly to above, we used a phone emoji to have the phone number appear nicer on the website. Additionally, we added lots of classNames to help with the style sheet, some of these we did not have time to style. 

**Weather Page** 
This page was adapted from the weather app that we created in class. Now, it just looks at Williamsburg as opposed to options. 
