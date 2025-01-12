from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
import json
from googletrans import Translator
import time

# API key (replace with your actual API key)
api_key = "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"

# Configure API key authorization
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = api_key
api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

# Load email addresses from the JSON file
json_file_path = 'C:/Users/X1YOGA/New AGODA/scraped_data.json'

try:
    with open(json_file_path, 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: JSON file not found. Please check the file path.")
    exit(1)

# Extract email addresses and language preferences
recipients = [{"email": person["email_address"], "language": person.get("language", "en")} for person in data]

# Initialize the Translator
translator = Translator()

# Base email content (in English)
subject = "Welcome to Data"
html_content = """
<h1>Hello!</h1>
<p>We're thrilled to have you onboard.</p>
<p>Thank you for joining us!</p>
"""

# Function to translate email content into German
def translate_to_german():
    translated_subject = translator.translate(subject, src='en', dest='de').text
    translated_html_content = translator.translate(html_content, src='en', dest='de').text
    return translated_subject, translated_html_content

# Function to manually trigger the translation
def translate_email(recipient):
    # If the recipient's preferred language is not specified or is not German, translate content to German
    if recipient["language"] != "de":
        print(f"Translating email to German for {recipient['email']}...")
        return translate_to_german()
    else:
        # If the language is already German, skip translation
        print(f"Sending email in German to {recipient['email']}")
        return subject, html_content

# Send individual emails to each recipient
for recipient in recipients:
    time.sleep(5)  # Delay between emails to avoid API rate limits

    # Trigger the translation when needed (manual process)
    translated_subject, translated_html_content = translate_email(recipient)

    email = sib_api_v3_sdk.SendSmtpEmail(
        sender={"name": "Data", "email": "thanishali1234@gmail.com"},
        to=[{"email": recipient["email"]}],
        subject=translated_subject,
        html_content=translated_html_content
    )

    try:
        # Send the email
        api_response = api_instance.send_transac_email(email)
        print(f"Email sent to {recipient['email']} with message ID: {api_response.message_id}")
    except ApiException as e:
        print(f"Error sending email to {recipient['email']}: {e}")
