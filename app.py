from flask import Flask, render_template, request, redirect, url_for, session
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_patients():
    time.sleep(0.5)
    return [
        {"first_name": "Raj", "last_name": "Icu", "patient_id": "edf8so8872", "treatment": "Surgery from a minor car accident.", "admission_date": "--AWAITING_AISHWARYA---"},
        {"first_name": "Camila", "last_name": "Lopez", "patient_id": "sdf8320j43", "treatment": "Treatment for a respiratory infection and showing significant improvement.", "admission_date": "--AWAITING_AISHWARYA---"},
        {"first_name": "Theodore", "last_name": "Mychart", "patient_id": "ssf922m24", "treatment": "Fainting episode. No underlying serious medical condition presumed.", "admission_date": "--AWAITING_AISHWARYA---"},
        {"first_name": "Liam", "last_name": "O'Reilly", "patient_id": "ale434m11", "treatment": "Broken arm and necessary follow-up care, physical therapy.", "admission_date": "05.23.2025"},
        {"first_name": "Sofia", "last_name": "Santos", "patient_id": "lkjeriwo39", "treatment": "Stomach virus, administered intravenous fluids, prolonged recovery from dehydration and weakness", "admission_date": "05.07.2025"},
        {"first_name": "Natalia", "last_name": "Petrovich", "patient_id": "msdfjho903", "treatment": "Evaluation and treatment for presumed mild case of pneumonia, monitoring for worsening.", "admission_date": "05.01.2025"},
        {"first_name": "Diego", "last_name": "González", "patient_id": "juo9332b21", "treatment": "Dehydration and intravenous fluids, high difficulty maintaining weight and nutrition.", "admission_date": "04.24.2025"},
        {"first_name": "Doe", "last_name": "John", "patient_id": "lkj0244824", "treatment": "Hypotensive and tachycardic upon arrival, monitoring for hypovolemic shock or cardiogenic shock.", "admission_date": "03.29.2025"},
        {"first_name": "Parthi", "last_name": "Haq", "patient_id": "pocs7fhgik1", "treatment": "Broken hip from large fall, underwent surgery and continued monitoring for pain and complications.", "admission_date": "03.16.2025"},
    ]

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'S0phia':
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    patients = get_patients()
    return render_template('dashboard.html', patients=patients, total=len(patients))

@app.route('/patients')
def patients():
    if 'user' not in session:
        return redirect(url_for('login'))
    patients = get_patients()
    return render_template('patients.html', patients=patients, total=len(patients))

@app.route('/reports')
def reports():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('reports.html')

@app.route('/analytics')
def analytics():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('analytics.html')

@app.route('/settings')
def settings():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('notifications.html')

@app.route('/orchestrate/<patient_id>')
def orchestrate(patient_id):
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('orchestrate.html', patient_id=patient_id)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/assistant/<patient_name>')
def assistant(patient_name):
    return render_template('assistant.html', patient_name=patient_name)


if __name__ == '__main__':
    # *** IMPORTANT CHANGE HERE ***
    # Bind to 0.0.0.0 to make the Flask app accessible from outside the container's localhost
    app.run(host='0.0.0.0', port=5000, debug=True) # Ensure port matches EXPOSE in Dockerfile
