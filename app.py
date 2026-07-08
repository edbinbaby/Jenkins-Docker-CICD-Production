from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Edbin Motors</title>

<style>

body{
    margin:0;
    background:#111;
    color:white;
    font-family:Arial;
}

.header{
    background:black;
    padding:20px;
    text-align:center;
}

.hero{
    text-align:center;
    padding:80px;
}

h1{
    font-size:50px;
    color:#ff3333;
}

.car{
    font-size:28px;
}

.box{
    display:flex;
    justify-content:center;
    gap:20px;
}

.card{
    background:#222;
    padding:25px;
    width:250px;
    border-radius:15px;
}

.footer{
    background:black;
    text-align:center;
    padding:15px;
    margin-top:50px;
}

</style>

</head>


<body>


<div class="header">
<h2>🚗 EDBIN MOTORS</h2>
</div>


<div class="hero">

<h1>Premium 4x4 Vehicles</h1>

<p class="car">
Luxury | Performance | Adventure
</p>


<div class="box">

<div class="card">
<h2>Land Cruiser</h2>
<p>
V8 Engine<br>
Offroad Capability<br>
Premium SUV
</p>
</div>


<div class="card">
<h2>Ford Endeavour</h2>
<p>
3.2 4x4 Diesel<br>
Terrain Management<br>
Adventure Ready
</p>
</div>


<div class="card">
<h2>Toyota Hilux</h2>
<p>
Pickup Truck<br>
Extreme Durability<br>
4WD Power
</p>
</div>


</div>

</div>


<div class="footer">

Production Website Deployed using Jenkins + Docker + AWS 🚀

</div>


</body>
</html>
"""


app.run(host="0.0.0.0", port=5000)
