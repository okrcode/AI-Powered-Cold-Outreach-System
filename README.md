# AI-Powered-Cold-Outreach-System
This script automates AI-driven cold email outreach with personalized, multilingual support. It verifies emails via the Hunter API, translates content using Googletrans, and sends emails via Sendinblue. Invalid emails are skipped, and delays ensure compliance with API rate limits for efficient communication

# Email Sender Script

This script is designed to scrape data from a website, verify email addresses, and send personalized emails in multiple languages. It uses various APIs like Sendinblue and Hunter.io to send and verify emails.

## Features
- Scrapes business data (names, emails, websites, phone numbers) from a webpage.
- Translates email content into German using Google Translate API.
- Verifies email addresses using the Hunter API.
- Sends personalized emails using Sendinblue API.

## Requirements
To run this script, you need the following Python libraries:

- `requests`
- `lxml`
- `json`
- `random`
- `pandas`
- `sib_api_v3_sdk`
- `googletrans==4.0.0-rc1`
- `time`


## hint remove space to run without api key error 
api_key = "xkeysib-e9d880ce13a1f04b91dc28bd2f120f   7c3052376bc967376deb4fbe2354825911-ex3OjChSufIhrerh"
hunter_api_key = "7128efd62bf9e6168a   c7f673bbda03f438cf4626"
