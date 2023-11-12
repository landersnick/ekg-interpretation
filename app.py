from flask import Flask, render_template, request, jsonify
import statistics

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

def calculate_stability(data):
    # Assuming that lower variability in data indicates higher stability
    return max(data) - min(data)  # This represents the amplitude

@app.route('/analyze_ecg', methods=['POST'])
def analyze_ecg():
    # Retrieve data from POST request
    data = request.json.get('data')
    
    # Process the data to get ECG readings (assuming CSV format)
    ecg_data_line = data.split('\n')[0]
    ecg_readings = [float(point) for point in ecg_data_line.split(',') if point]

    # Perform the analysis
    conditions = perform_analysis(ecg_readings)
    
    # Assuming the third line of the CSV contains the previous ECG data
    previous_ecg_data_line = data.split('\n')[2]
    previous_ecg_readings = [float(point) for point in previous_ecg_data_line.split(',') if point]

    current_stability = calculate_stability(ecg_readings)
    previous_stability = calculate_stability(previous_ecg_readings)
    
    # Calculate stability change as a percentage
    # A lower value indicates improvement
    stability_change = ((previous_stability - current_stability) / previous_stability) * 100

    # Assuming the second line contains the date after the age
    patient_info_line = data.split('\n')[1]
    patient_date = patient_info_line.split(',')[2].strip()

    response_data = {
        'conditions': conditions,
        'stability_change': stability_change,
        'date': patient_date
    }

    return jsonify(response_data)

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
