from flask import Flask, jsonify
from datetime import datetime, timedelta
import random

app = Flask(__name__)

# Define logical grouped location data
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

def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')

@app.route('/campaign-data', methods=['GET'])
def get_campaign_data():
    start = datetime.strptime("2025-02-01", "%Y-%m-%d")
    end = datetime.strptime("2025-06-10", "%Y-%m-%d")

    campaigns = []

    for _ in range(300_000):
        country = random.choice(list(geo_data.keys()))
        state = random.choice(geo_data[country]["states"])
        city, zipcode = random.choice(geo_data[country]["cities"][state])

        impressions = maybe_null(random.randint(5000, 15000))
        clicks = maybe_null(random.randint(0, impressions if impressions else 500))
        conversions = maybe_null(random.randint(0, clicks if clicks else 100))

        campaigns.append({
            "campaign_id": maybe_null(f"cmp{random.randint(100,120)}"),
            "ad_id": maybe_null(f"ad{random.randint(1, 20):03}"),
            "date": random_date(start, end),
            "brand": maybe_null(random.choice(["BrandA", "BrandB", "BrandC"])),
            "country": maybe_null(country),
            "state": maybe_null(state),
            "city": maybe_null(city),
            "zipcode": maybe_null(zipcode),
            "impressions": impressions,
            "clicks": clicks,
            "spend": maybe_null(round(random.uniform(100.0, 500.0), 2)),
            "conversions": conversions
        })

    return jsonify(campaigns)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)