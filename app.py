from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

# Simulated API call (replace with real API call later)
def get_patients():
    time.sleep(0.5)
    return [
        {"first_name": "Hiroshi", "last_name": "Kimura", "patient_id": "edf8so8872", "treatment": "Surgery from a minor car accident.", "admission_date": "-----"},
        {"first_name": "Isabella", "last_name": "Fernandez", "patient_id": "sdf8320j43", "treatment": "Treatment for a respiratory infection and showing significant improvement.", "admission_date": "-----"},
        {"first_name": "Rahul", "last_name": "Patel", "patient_id": "ssf922m24", "treatment": "Fainting episode. No underlying serious medical condition presumed.", "admission_date": "-----"},
        {"first_name": "Liam", "last_name": "O'Reilly", "patient_id": "ale434m11", "treatment": "Broken arm and necessary follow-up care, physical therapy.", "admission_date": "-----"},
        {"first_name": "Sofia", "last_name": "Santos", "patient_id": "lkjeriwo39", "treatment": "----", "admission_date": "-----"},
        {"first_name": "Natalia", "last_name": "Petrovich", "patient_id": "msdfjho903", "treatment": "Evaluation and treatment for presumed mild case of pneumonia.", "admission_date": "-----"},
        {"first_name": "Diego", "last_name": "González", "patient_id": "juo9332b21", "treatment": "Dehydration and intravenous fluids.", "admission_date": "-----"},
        {"first_name": "Doe", "last_name": "John", "patient_id": "lkj0244824", "treatment": "Dehydration and intravenous fluids.", "admission_date": "-----"},
        {"first_name": "Diego", "last_name": "González", "patient_id": "pocs7fhgik1", "treatment": "Dehydration and intravenous fluids.", "admission_date": "-----"},
    ]

@app.route('/')
def index():
    patients = get_patients()
    return render_template('index.html', patients=patients, total=len(patients))

@app.route('/api/patients')
def api_patients():
    patients = get_patients()
    return jsonify(patients)

if __name__ == '__main__':
    app.run(debug=True)
