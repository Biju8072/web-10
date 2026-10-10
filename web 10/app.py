from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary in-memory list to store user data (simulating a database table)
registered_users = [
    {
        "name": "G MARIO SHILSHI RAJ",
        "age": "19",
        "mobile": "7702341392",
        "email": "gubbalamario@karunya.edu.in",
        "gender": "Female",
        "state": "Andhra Pradesh",
        "skills": "quick learner"
    },
    {
        "name": "priya",
        "age": "20",
        "mobile": "7538976320",
        "email": "priya123@gmail.com",
        "gender": "Female",
        "state": "Karnataka",
        "skills": "Dnacing"
    }
]

# Route for rendering the registration form input page
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Safely extract input parameters from the browser request form
        user_record = {
            "name": request.form.get('name'),
            "age": request.form.get('age'),
            "mobile": request.form.get('mobile'),
            "email": request.form.get('email'),
            "gender": request.form.get('gender'),
            "state": request.form.get('state'),
            "skills": request.form.get('skills')
        }
        # Append the new record dataset into memory storage
        registered_users.append(user_record)
        # Direct the user straight to the data table dashboard route
        return redirect(url_for('server_dashboard'))
        
    return render_template('register.html')

# Route for rendering the registered users database grid table
@app.route('/server')
def server_dashboard():
    return render_template('users.html', users=registered_users)

if __name__ == '__main__':
    # Initializing the server framework locally using custom port 5001
    # to avoid the default port 5000 conflict on macOS
    app.run(host='127.0.0.1', port=5001, debug=True)
