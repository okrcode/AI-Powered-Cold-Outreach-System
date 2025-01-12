# Lead Generation Plan
Data Sources (Publicly Available):

  Real Estate Websites: Scrape platforms like Immobilienscout24, Immowelt, and Makler for new construction projects and developer contact details.
  
  Examples: Dodge Data & Analytics, BidClerk, or state-specific platforms like the California Department of General Services (for public construction projects).
  Extract project details and company contact info.
  Business Directories:
  
  Platforms like LinkedIn, Yellow Pages, or Houzz often include profiles of real estate developers and construction companies.
  News Websites and PR Platforms:
  
example urls:
    https://www.gelbeseiten.de/suche/bautr%C3%A4ger/bundesweit
    https://www.bautraeger24.de/bautraeger-plz-1.html



# Main Components
   ## API Setup:
    (https://www.brevo.com/pricing/) - (can send 300 Emails Per Day for free)
    Sendinblue API: Used to send transactional emails. The API key is configured for authentication.
    (https://hunter.io/pricing) - (can verify 50 Emails Per Day for free)
    Hunter API: Used to verify email addresses before sending an email.
  
  ## Email Translation:
    Uses the Googletrans library to translate the subject and HTML content of the email from English to German if the recipient's preferred language is not German.
  
  ## Email Verification:
    Each email is validated using the Hunter API. If the email is invalid, it is skipped.
  
  ## Email Sending:
    Emails are sent individually using the Sendinblue API. There is a 5-second delay between emails to prevent API rate limits.

# Workflow
  ## Load JSON Data:
  Reads the recipient list from a getdata() and prepares a list of dictionaries containing email addresses and language preferences.
  ## Loop Through Recipients:
  # For each recipient:
  #### Verify Email: The email is validated using the Hunter API. Invalid emails are skipped.
  #### Translate Content: Translates the email content based on the recipient's language preference.
  #### Send Email: Constructs the email using the Sendinblue API and sends it.
  #### Error Handling:If the getdata() is not found, the script exits with an error message.Errors during email sending are caught and printed.
  #### Rate Limiting:Introduces a 5-second delay between emails to avoid API rate limits.


# Key Features
  #### Personalization: Adapts email language based on recipient preferences.
  #### Validation: Ensures emails are sent only to valid addresses using Hunter API.
  #### Automation: Automates email translation and sending for multiple recipients.
  #### Error Handling: Includes mechanisms to handle common errors like invalid JSON paths or email delivery failures.


# Dependencies
  ## Libraries:  
    sib_api_v3_sdk: For interacting with the Sendinblue API.
    googletrans: For translating email content.
    requests: For sending HTTP requests to the Hunter API.
  ## APIs:
    Sendinblue for email delivery.
    Hunter for email verification.
  Other Notes:
    Ensure the JSON file path is correct.
    Replace API keys (api_key and hunter_api_key) with valid keys.

      
