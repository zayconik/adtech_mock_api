from flask import Flask, jsonify
from datetime import datetime
import random

app = Flask(__name__)

# 📌 Define logical grouped location data
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

@app.route('/campaign-data', methods=['GET'])
def get_campaign_data():
    today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    campaigns = []

    for i in range(500):
        country = random.choice(list(geo_data.keys()))
        state = random.choice(geo_data[country]["states"])
        city, zipcode = random.choice(geo_data[country]["cities"][state])

        campaigns.append({
            "campaign_id": f"cmp{random.randint(100,120)}",
            "ad_id": f"ad{random.randint(1, 20):03}",
            "date": today,
            "brand": random.choice(["BrandA", "BrandB", "BrandC"]),
            "country": country,
            "state": state,
            "city": city,
            "zipcode": zipcode,
            "impressions": random.randint(5000, 15000),
            "clicks": random.randint(100, 500),
            "spend": round(random.uniform(100.0, 500.0), 2),
            "conversions": random.randint(5, 50)
        })

    return jsonify(campaigns)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)