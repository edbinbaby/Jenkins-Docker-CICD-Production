from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# --- Vehicle inventory (matches the Dirt Draft frontend) ----------------
cars = [
    {"code": "LC-100", "name": "Toyota Land Cruiser", "cls": "Premium SUV",
     "engine": "4.7L V8", "drive": "Full-Time 4WD", "clearance_mm": 225},
    {"code": "FE-3.2", "name": "Ford Endeavour", "cls": "Adventure SUV",
     "engine": "3.2L Diesel", "drive": "4x4 Shift-on-Fly", "clearance_mm": 228},
    {"code": "HX-4D", "name": "Toyota Hilux", "cls": "Pickup Truck",
     "engine": "2.8L Turbo-D", "drive": "Part-Time 4WD", "clearance_mm": 216},

    {"code": "TH-15", "name": "Mahindra Thar", "cls": "Off-Road SUV",
     "engine": "2.2L mHawk Diesel", "drive": "4WD Shift-on-Fly", "clearance_mm": 226},
    {"code": "TH-RX", "name": "Mahindra Thar Roxx", "cls": "Off-Road SUV",
     "engine": "2.2L mHawk Diesel", "drive": "4XPLOR 4WD", "clearance_mm": 226},
    {"code": "SC-N7", "name": "Mahindra Scorpio-N", "cls": "SUV",
     "engine": "2.2L mHawk Diesel", "drive": "4WD Low Ratio", "clearance_mm": 222},
    {"code": "SC-CL", "name": "Mahindra Scorpio Classic", "cls": "SUV",
     "engine": "2.2L mHawk Diesel", "drive": "4WD Shift-on-Fly", "clearance_mm": 180},
    {"code": "BL-CP", "name": "Mahindra Bolero Camper", "cls": "Pickup Truck",
     "engine": "1.5L mHawk Diesel", "drive": "RWD Heavy Duty", "clearance_mm": 187},
    {"code": "XV-700", "name": "Mahindra XUV700", "cls": "SUV",
     "engine": "2.2L mHawk Diesel", "drive": "AWD Adaptive", "clearance_mm": 200},

    {"code": "SF-DT", "name": "Tata Safari", "cls": "SUV",
     "engine": "2.0L Kryotec Diesel", "drive": "FWD / Terrain Response", "clearance_mm": 205},
    {"code": "HR-DT", "name": "Tata Harrier", "cls": "SUV",
     "engine": "2.0L Kryotec Diesel", "drive": "FWD / Terrain Response", "clearance_mm": 205},
    {"code": "SR-EV", "name": "Tata Sierra", "cls": "SUV",
     "engine": "1.5L Turbo Petrol", "drive": "AWD Available", "clearance_mm": 209},
    {"code": "XN-XT", "name": "Tata Xenon XT", "cls": "Pickup Truck",
     "engine": "2.2L DICOR Diesel", "drive": "4x4 Part-Time", "clearance_mm": 210},

    {"code": "GK-XT", "name": "Force Gurkha", "cls": "Off-Road Jeep",
     "engine": "2.6L Turbo Diesel", "drive": "Shift-on-Fly 4WD", "clearance_mm": 244},

    {"code": "JM-4X", "name": "Maruti Suzuki Jimny", "cls": "Off-Road SUV",
     "engine": "1.5L K15B Petrol", "drive": "ALLGRIP PRO 4WD", "clearance_mm": 210},
    {"code": "GY-MK", "name": "Maruti Suzuki Gypsy", "cls": "Off-Road Jeep",
     "engine": "1.3L Petrol", "drive": "Part-Time 4WD", "clearance_mm": 210},

    {"code": "FT-LG", "name": "Toyota Fortuner", "cls": "SUV",
     "engine": "2.8L Turbo Diesel", "drive": "Part-Time 4WD", "clearance_mm": 224},
    {"code": "PR-4L", "name": "Toyota Land Cruiser Prado", "cls": "Premium SUV",
     "engine": "2.8L Turbo Diesel", "drive": "Full-Time 4WD", "clearance_mm": 220},

    {"code": "DM-VC", "name": "Isuzu D-Max V-Cross", "cls": "Pickup Truck",
     "engine": "1.9L RZ4E Diesel", "drive": "Shift-on-Fly 4WD", "clearance_mm": 235},
    {"code": "MX-7S", "name": "Isuzu MU-X", "cls": "SUV",
     "engine": "1.9L RZ4E Diesel", "drive": "Terrain Command 4WD", "clearance_mm": 230},

    {"code": "CP-TH", "name": "Jeep Compass Trailhawk", "cls": "Off-Road SUV",
     "engine": "2.0L MultiJet Diesel", "drive": "Active Drive Low 4x4", "clearance_mm": 198},
    {"code": "WR-RB", "name": "Jeep Wrangler Rubicon", "cls": "Off-Road Jeep",
     "engine": "2.0L Turbo Petrol", "drive": "Rock-Trac 4x4", "clearance_mm": 252},
    {"code": "MD-5S", "name": "Jeep Meridian", "cls": "SUV",
     "engine": "2.0L MultiJet Diesel", "drive": "4x4 Selec-Terrain", "clearance_mm": 199},

    {"code": "DF-110", "name": "Land Rover Defender 110", "cls": "Premium SUV",
     "engine": "3.0L Turbo Diesel", "drive": "Terrain Response 2", "clearance_mm": 291},

    {"code": "TR-4X", "name": "Nissan Terrano", "cls": "SUV",
     "engine": "1.5L dCi Diesel", "drive": "FWD / AWD Option", "clearance_mm": 205},
    {"code": "DS-4X", "name": "Renault Duster", "cls": "SUV",
     "engine": "1.3L Turbo Petrol", "drive": "AWD Available", "clearance_mm": 205},

    {"code": "TG-GT", "name": "Volkswagen Taigun", "cls": "SUV",
     "engine": "1.5L TSI Petrol", "drive": "FWD / DSG", "clearance_mm": 188},
    {"code": "GL-8S", "name": "MG Gloster", "cls": "Premium SUV",
     "engine": "2.0L Twin-Turbo Diesel", "drive": "Full-Time 4WD", "clearance_mm": 224},
]

# --- In-memory store for enquiries (swap for a real DB in production) ---
enquiries = []


@app.route("/")
def home():
    return jsonify({
        "service": "Dirt Draft Backend",
        "status": "running",
        "endpoints": {
            "GET /cars": "list full vehicle inventory",
            "GET /cars/<code>": "get a single vehicle by unit code",
            "POST /contact": "submit a customer enquiry (name, phone, message, car_code)",
            "GET /enquiries": "list saved enquiries (admin/debug)"
        }
    })


@app.route("/cars")
def get_cars():
    return jsonify({"count": len(cars), "cars": cars})


@app.route("/cars/<code>")
def get_car(code):
    for car in cars:
        if car["code"].lower() == code.lower():
            return jsonify(car)
    return jsonify({"error": f"No vehicle found with code '{code}'"}), 404


@app.route("/contact", methods=["POST"])
def contact():
    data = request.get_json(silent=True) or {}

    name = data.get("name", "").strip()
    phone = data.get("phone", "").strip()
    message = data.get("message", "").strip()
    car_code = data.get("car_code", "").strip()

    if not name or not phone:
        return jsonify({"error": "Both 'name' and 'phone' are required"}), 400

    enquiry = {
        "id": len(enquiries) + 1,
        "name": name,
        "phone": phone,
        "message": message,
        "car_code": car_code or None,
        "received_at": datetime.utcnow().isoformat() + "Z"
    }
    enquiries.append(enquiry)

    return jsonify({
        "message": "Customer enquiry saved",
        "enquiry_id": enquiry["id"]
    }), 201


@app.route("/enquiries")
def get_enquiries():
    return jsonify({"count": len(enquiries), "enquiries": enquiries})


@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Route not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
