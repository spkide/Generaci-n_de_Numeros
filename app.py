from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

FORMATS = {
    "🇺🇸 USA": {
        "code": "+1",
        "areas": ["212","310","415","305","213","646","917","347","718","929",
                  "424","562","714","818","858","619","323","213","408","510"],
        "pattern": lambda area: f"+1 ({area}) {random.randint(200,999)}-{random.randint(1000,9999)}"
    },
    "🇲🇽 México": {
        "code": "+52",
        "areas": ["55","81","33","664","222","442","477","461","686","871"],
        "pattern": lambda area: f"+52 {area} {random.randint(1000,9999)} {random.randint(1000,9999)}"
    },
    "🇬🇧 UK": {
        "code": "+44",
        "areas": ["20","121","161","113","141","151","117","114","116","115"],
        "pattern": lambda area: f"+44 {area} {random.randint(1000,9999)} {random.randint(1000,9999)}"
    },
    "🇪🇸 España": {
        "code": "+34",
        "areas": ["6","7"],
        "pattern": lambda area: f"+34 {area}{random.randint(10,99)} {random.randint(100,999)} {random.randint(100,999)}"
    },
    "🇦🇷 Argentina": {
        "code": "+54",
        "areas": ["11","351","261","341","381","299","343","388","387","376"],
        "pattern": lambda area: f"+54 9 {area} {random.randint(1000,9999)}-{random.randint(1000,9999)}"
    },
    "🇨🇴 Colombia": {
        "code": "+57",
        "areas": ["1","2","4","5","6","7","8"],
        "pattern": lambda area: f"+57 {area} {random.randint(100,999)} {random.randint(1000,9999)}"
    },
    "🇧🇷 Brasil": {
        "code": "+55",
        "areas": ["11","21","31","41","51","61","71","81","85","92"],
        "pattern": lambda area: f"+55 ({area}) {random.randint(90000,99999)}-{random.randint(1000,9999)}"
    },
    "🇩🇪 Alemania": {
        "code": "+49",
        "areas": ["30","40","89","221","211","711","511","351","341","371"],
        "pattern": lambda area: f"+49 {area} {random.randint(10000,99999)}"
    },
    "🇫🇷 Francia": {
        "code": "+33",
        "areas": ["1","2","3","4","5","6","7"],
        "pattern": lambda area: f"+33 {area} {random.randint(10,99)} {random.randint(10,99)} {random.randint(10,99)} {random.randint(10,99)}"
    },
    "🇨🇦 Canadá": {
        "code": "+1",
        "areas": ["416","647","437","905","289","519","226","613","343","514"],
        "pattern": lambda area: f"+1 ({area}) {random.randint(200,999)}-{random.randint(1000,9999)}"
    },
}

@app.route("/")
def index():
    return render_template("index.html", countries=list(FORMATS.keys()))

@app.route("/generate/<country>")
def generate(country):
    if country not in FORMATS:
        return jsonify({"error": "País no encontrado"}), 404
    fmt = FORMATS[country]
    area = random.choice(fmt["areas"])
    number = fmt["pattern"](area)
    return jsonify({"number": number, "country": country, "code": fmt["code"]})

@app.route("/generate_bulk/<country>/<int:count>")
def generate_bulk(country, count):
    if country not in FORMATS:
        return jsonify({"error": "País no encontrado"}), 404
    count = min(count, 50)
    fmt = FORMATS[country]
    numbers = []
    for _ in range(count):
        area = random.choice(fmt["areas"])
        numbers.append(fmt["pattern"](area))
    return jsonify({"numbers": numbers, "country": country})

if __name__ == "__main__":
    print("🚀 Iniciando generador de números...")
    print("📱 Abre: http://localhost:5000")
    app.run(debug=True, port=5000)
