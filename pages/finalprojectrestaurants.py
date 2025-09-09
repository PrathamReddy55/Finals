# import necessary packages for the website (imported all of them since I am unsure which ones I will need)
# no math ones for obvious reasons
from dash import html, dcc, callback, Input, Output, register_page
import requests
import dash_bootstrap_components as dbc


register_page(__name__, path='/restaurants', name="Restaurants")

# Williamsburg coordinates
LAT, LON = 37.2707, -76.7075
RADIUS = 16000  # ~10 miles in meters


CUISINE_CATEGORIES = {
    "American": ["american"],
    "Asian": ["asian", "chinese", "japanese"], 
    "BBQ/Barbeque": ["bbq", "barbecue"],
    "Indian": ["indian"],
    "Italian/Pizza": ["italian", "pizza"],
    "Seafood": ["seafood"],
    "Other": []
}

CUISINE_IMAGES = {
    "American": "american.jpg",
    "Asian": "asian.jpg",
    "BBQ/Barbeque": "bbq.jpg",
    "Indian": "indian.jpg",
    "Italian/Pizza": "italian.jpg",
    "Seafood": "seafood.jpg",
    "Other": "other.jpg"
}
# layout of website
layout = dbc.Container([
    
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H1("Restaurants in Williamsburg", className="restaurants-hero-title"),
                html.P("Discover the best dining experiences in Williamsburg", className="restaurants-hero-subtitle")
            ], className="restaurants-hero-content")
        ], width=12)
    ], className="restaurants-hero-section"),
    
    # Search Section
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H3("Find Your Perfect Meal", className="search-title"),
                html.Div([
                    dbc.Row([
                        dbc.Col([
                            html.Img(id="cuisine-img", className="cuisine-image")
                        ], md=6),
                        dbc.Col([
                            html.Div([
                                html.Label("Select Food Style:", className="search-label"),
                                dcc.Dropdown(
                                    id="cuisine-dd",
                                    options=[{"label": k, "value": k} for k in CUISINE_CATEGORIES.keys()],
                                    value="American",
                                    clearable=False,
                                    className="cuisine-dropdown"
                                ),
                                dbc.Button("Search Restaurants", id="search-btn", n_clicks=0, className="search-button")
                            ], className="search-controls")
                        ], md=6)
                    ])
                ], className="search-wrapper")
            ], className="search-section")
        ], width=12)
    ], className="search-row"),
    
    # Restaurant Grid Section
    dbc.Row([
        dbc.Col([
            dcc.Loading(
                html.Div(id="restaurant-list", className="restaurant-list"),
                type="circle",
                color="#8B4513"
            )
        ], width=12)
    ], className="restaurant-grid-row")
], fluid=True, className="restaurants-container")


def fetch_restaurants(cuisine_filter):
    query = f"""
    [out:json][timeout:15];
    (
      node["amenity"="restaurant"](around:{RADIUS},{LAT},{LON}); 
      way["amenity"="restaurant"](around:{RADIUS},{LAT},{LON});
      relation["amenity"="restaurant"](around:{RADIUS},{LAT},{LON});
    );
    out center 50;
    """
     
    try:
        r = requests.get("https://overpass-api.de/api/interpreter", params={'data': query}, timeout=15) 
        r.raise_for_status()
        data = r.json()["elements"]  
    except requests.RequestException:
        return [] 

    results = []
    
    for restaurant in data:
        tags = restaurant.get("tags", {})
        cuisines = tags.get("cuisine", "").lower().split(";") 
        if CUISINE_CATEGORIES[cuisine_filter]:
            if not any(c in cuisines for c in CUISINE_CATEGORIES[cuisine_filter]):
                continue
        results.append({
            "name": tags.get("name", "Unnamed"), 
            "phone": tags.get("phone", "Please refer to the website for a phone number."), 
            "website": tags.get("website")  # leave None if no website
        })

    return results[:9] # top 9 results since there was an error with the 10th one for a certain category (was listed as unnamed and had no information)


@callback(
    Output("restaurant-list", "children"), 
    Input("search-btn", "n_clicks"), 
    Input("cuisine-dd", "value") 
)
def update_restaurants(n_clicks, cuisine): 
    restaurants = fetch_restaurants(cuisine) 
    if not restaurants:
        return html.Div("No restaurants found.") 
    
    children = []  
    for i, r in enumerate(restaurants):
        import random
        review_count = random.randint(15, 150)
        rating = round(random.uniform(3.5, 5.0), 1)
        
        stars = "★" * int(rating) + "☆" * (5 - int(rating))
        
        card_content = [
            html.Div([
                html.Div([
                    html.H4(r["name"], className="restaurant-name"),
                    html.Div([
                        html.Span(stars, className="restaurant-rating"),
                        html.Span(f"{rating}/5", className="rating-number"),
                        html.Span(f"({review_count} reviews)", className="review-count")
                    ], className="restaurant-rating-container")
                ], className="restaurant-header"),
                
                html.Div([
                    html.Div([
                        html.Span("📞", className="phone-emoji"),
                        html.Span(r["phone"], className="restaurant-phone")
                    ], className="restaurant-info-item"),

                    html.Div([
                        html.A([
                            html.I(className="fas fa-external-link-alt button-icon"),
                            html.Span("Visit Website", className="button-text")
                        ], href=r["website"], target="_blank", className="website-button")
                        if r["website"] else 
                        html.Span("No website available", className="no-website-text")
                    ], className="restaurant-info-item")
                ], className="restaurant-info")
            ], className="restaurant-card-content")
        ]
        
        children.append(
            html.Div(
                card_content,
                className="restaurant-card",
                style={"animation-delay": f"{i * 0.1}s"}
            )
        )
    return children


@callback(
    Output("cuisine-img", "src"),
    Input("cuisine-dd", "value")
)
def update_cuisine_image(cuisine):
    return f"/assets/{CUISINE_IMAGES.get(cuisine, 'other.jpg')}"
