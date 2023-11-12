from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/analyze_ecg', methods=['POST'])
def analyze_ecg():
    # Retrieve data from POST request
    data = request.json.get('data')
    
    # Process the data to get ECG readings (assuming CSV format)
    ecg_data_line = data.split('\n')[0]
    ecg_readings = [float(point) for point in ecg_data_line.split(',') if point]

    # Perform the analysis
    conditions = perform_analysis(ecg_readings)

    return jsonify(conditions)

def perform_analysis(data):
    # Example: Basic analysis based on heart rate
    average_rate = sum(data) / len(data)
    conditions = {
        "Normal Sinus Rhythm": 0,
        "Atrial Fibrillation": 0,
        "Ventricular Tachycardia": 0
    }

    if average_rate > 0.5:
        # High likelihood of Ventricular Tachycardia
        conditions["Ventricular Tachycardia"] = 70
        conditions["Atrial Fibrillation"] = 20
        conditions["Normal Sinus Rhythm"] = 10
    elif average_rate < -0.2:
        # Higher likelihood of Atrial Fibrillation
        conditions["Atrial Fibrillation"] = 60
        conditions["Normal Sinus Rhythm"] = 30
        conditions["Ventricular Tachycardia"] = 10
    else:
        # Most likely Normal Sinus Rhythm
        conditions["Normal Sinus Rhythm"] = 80
        conditions["Atrial Fibrillation"] = 10
        conditions["Ventricular Tachycardia"] = 10

    return conditions

if __name__ == "__main__":
    app.run(debug=True)
