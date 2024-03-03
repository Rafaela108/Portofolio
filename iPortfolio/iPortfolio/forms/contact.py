from flask import Flask, request
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

receiving_email_address = 'rafaelaestera@yahoo.com'

# Configure Flask Mail
app.config['MAIL_SERVER'] = 'your_mail_server.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your_username'
app.config['MAIL_PASSWORD'] = 'your_password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@example.com'

# Check if the Email Form library exists
email_form_path = '../assets/vendor/email-form/email-form.py'
if not app.config['MAIL_SERVER']:
    raise ValueError('Unable to load the "PHP Email Form" Library!')

# Create Flask route for handling the contact form
@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    # Create a message object
    msg = Message(subject=subject, recipients=[receiving_email_address])
    msg.body = f"From: {name}\nEmail: {email}\nMessage: {message}"

    try:
        # Send the email
        mail.send(msg)
        return 'Email sent successfully!'
    except Exception as e:
        return f'Error: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
