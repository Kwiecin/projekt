from tkinter import *
from tkinter import ttk, messagebox
import tkintermapview
from geopy.geocoders import Nominatim

hurtownie = []
pracownicy = []
klienci = []

geolocator = Nominatim(user_agent="hurtownie_app") # tworzenie obiektu

def get_coordinates(street, city): # definicja funkcji
    try:
        if not city.strip():
            raise ValueError("Brak miasta")
        query = f"{street.strip()}, {city.strip()}, Polska" if street else f"{city.strip()}, Polska" # tworzenie obiektu
        loc = geolocator.geocode(query, timeout=10) # tworzenie obiektu
        if loc:
            return [loc.latitude, loc.longitude]
    except Exception as e:
        print(f"[Błąd geolokalizacji] {street}, {city}: {e}")
    return [52.23, 21.0]

