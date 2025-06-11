from flask import Flask, jsonify
from datetime import datetime
import random

app = Flask(__name__)

#  Define logical grouped location data
geo_data = {
    "US": {
        "states": ["California", "Texas"],
        "cities": {
            "California": [("Los Angeles", "90001"), ("San Diego", "92101")],
            "Texas": [("Houston", "77001"), ("Dallas", "75001")]
        }
    },
    "CA": {
        "states": ["Ontario"],
        "cities": {
            "Ontario": [("Toronto", "M5A1A1"), ("Ottawa", "K1A0B1")]
        }
    },
    "IN": {
        "states": ["Maharashtra", "Karnataka"],
        "cities": {
            "Maharashtra": [("Mumbai", "400001"), ("Pune", "411001")],
            "Karnataka": [("Bengaluru", "560001"), ("Mysore", "570001")]
        }
    }
}

def maybe_null(value, null_chance=0.1):
    return value if random.random() > null_chance else None

@app.route('/campaign-data', methods=['GET'])
def get_campaign_data():
    today = datetime.now().strftime('%Y-%m-%d')

    campaigns = []

    for i in range(1000):
        country = random.choice(list(geo_data.keys()))
        state = random.choice(geo_data[country]["states"])
        city, zipcode = random.choice(geo_data[country]["cities"][state])

        campaigns.append({
            "campaign_id": maybe_null(f"cmp{random.randint(100,120)}"),
            "ad_id": maybe_null(f"ad{random.randint(1, 20):03}"),
            "date": today,
            "brand": maybe_null(random.choice(["BrandA", "BrandB", "BrandC"])),
            "country": maybe_null(country),
            "state": maybe_null(state),
            "city": maybe_null(city),
            "zipcode": maybe_null(zipcode),
            "impressions": maybe_null(random.randint(5000, 15000)),
            "clicks": maybe_null(random.randint(100, 500)),
            "spend": maybe_null(round(random.uniform(100.0, 500.0), 2)),
            "conversions": maybe_null(random.randint(5, 50))
        })

    return jsonify(campaigns)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)