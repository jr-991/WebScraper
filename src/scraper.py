from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
from enum import Enum
from typing import Optional

class State(Enum):
    QLD = "qld"
    NSW = "nsw"
    VIC = "vic"
    TAS = "tas"
    SA = "sa"
    WA = "wa"
    NT = "nt"
    ACT = "act"

def fetch(state: State = State.QLD, page_num: int = 1) -> list[dict[str, Optional[str]]]:

    url = f"https://www.realestate.com.au/buy/in-{state.value}/list-{page_num}"
    response = requests.get(
        url,
        timeout=20,
        headers={"User-Agent": "Mozilla/5.0"},
        )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    listings = soup.find_all("article", attrs={"data-testid": "ResidentialCard"})

    # Debug information
    print("Response status:", response.status_code) # Print the HTTP response status code
    print("HTML length:", len(response.text)) # Print the length of the HTML response
    print("Listings found:", len(listings)) # Print the number of listings found
    print(response.text) # Print the full HTML response for debugging purposes

    properties = []

    print("Fetching properties from:", url) # Log the URL being fetched / debug information
    for listing in listings:
        price_tag = listing.select_one(".property-price")
        address_link = listing.select_one("a.residential-card__details-link")

        property_data = {
            "price": price_tag.get_text(" ", strip=True) 
            if price_tag 
            else None,

            "address": address_link.get_text(" ", strip=True) 
            if address_link 
            else None,

            "url": (
                urljoin("https://www.realestate.com.au", address_link.get("href"))
                if address_link
                else None,
            ),
            
        }
        properties.append(property_data)
        print("Fetched property:", property_data)

    return properties
