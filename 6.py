from __future__ import print_function
import requests
import lxml.html
import json
import random
import pandas as pd
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from googletrans import Translator
import time

# hint remove space to run without api key error 
api_key = "xkeysib-e9d880ce13a1f04b91dc28bd2f120f   7c3052376bc967376deb4fbe2354825911-ex3OjChSufIhrerh"
hunter_api_key = "7128efd62bf9e6168a   c7f673bbda03f438cf4626"

# Configure API key authorization
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = api_key
api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

# Set headers
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,kn;q=0.7,ja;q=0.6',
    'cache-control': 'no-cache',
    # 'cookie': '__cmpcpcx15760=__1__; __cmpcpc=__1__; __cmpconsentx15760=CQK86mQQK86mQAfbgBDEBXFoAP_gAEPgAAigJJNT9G_fbWFFOXp3aPskaYUX19hp4kQAAhaAE6AFyBOA8IQG00ASMAygJCAAABAAoTBBIABkCAAEAECAQIgFASDsIACAgAAKIAAEACMQQ0AQAAgIAAAgEAAIhEBMIxAAmAqgYZrkRMBAiIAAAgABAAABAIABAgMAGEEYQAAAAAIAQIAAAgIAEAAAAAEAAQAAAAAAAQSSABINCogAKIEJCCQMIIEAIgrCACgAAAAAkABAAAkCABwAgAooAEAAAAAAAAAAABAkACAAAAAAAIAIAAgQAAAABQAAAAAAAQAAAAAEAAgAAgABAQAAAAAAAAAACIQCABABAAQCAAgIAAAAAABAAAAAACAQAAAAAAIAAQAAAAAAAAAAAAAAQAIAAAAAAAAAAAAAAAAgAA; __cmpcvcx15760=__s1532_s1224_s1227_s936_s1518_c8230_s1852_c7342_s1491_s94_s446_s1052_s40_s64_s914_s335_s640_s1259_s248_s1266_s1494_s100_c7255_c46035_c10039_s2003_s2351_s1474_s405_s45_s457_s65_s849_s23_s1279_s1592_s1581_s571_s1155_s1452_s1100_s1142_s1558_c7334_s56_s314_s123_s1473_s1184_s336_s125_c8038_s987_s127_s7_c8102_s1974_c30435_s487_c7888_s312_s1591_c7412_s1_s26_c24203_s2612_s135_c8231_s1409_s905_s977_s1453_s46_s1637_s14_s1465_s561_s1475_s1442_s369_s765_s2688_s2_c7852_s153_s220_s157_s884_s11_s1049_s588_s1619_s2441_s1553_s885_c7897_s338_c8229_s1365_s2696_s36_s1538_c39505_c39506_c7895_s2560_s562_s741_s267_s883_s170_s49_c8040_s1085_s886_s1595_s76_c7894_s268_s2369_c7909_s460_s1327_s291_s292_c47721_s358_s971_s54_c18164_c7262_s193_s1068_s462_s1181_c7957_s274_c7907_s196_s1216_c7896_s52_s1115_s1432_s203_s32_s739_s60_s1477_s13_s679_c23722_c23721_s34_s35_s30_s217_s1189_s578_s356_U__; __cmpcvc=__s1532_s1224_s1227_s936_s1518_c8230_s1852_c7342_s1491_s94_s446_s1052_s40_s64_s914_s335_s640_s1259_s248_s1266_s1494_s100_c7255_c46035_c10039_s2003_s2351_s1474_s405_s45_s457_s65_s849_s23_s1279_s1592_s1581_s571_s1155_s1452_s1100_s1142_s1558_c7334_s56_s314_s123_s1473_s1184_s336_s125_c8038_s987_s127_s7_c8102_s1974_c30435_s487_c7888_s312_s1591_c7412_s1_s26_c24203_s2612_s135_c8231_s1409_s905_s977_s1453_s46_s1637_s14_s1465_s561_s1475_s1442_s369_s765_s2688_s2_c7852_s153_s220_s157_s884_s11_s1049_s588_s1619_s2441_s1553_s885_c7897_s338_c8229_s1365_s2696_s36_s1538_c39505_c39506_c7895_s2560_s562_s741_s267_s883_s170_s49_c8040_s1085_s886_s1595_s76_c7894_s268_s2369_c7909_s460_s1327_s291_s292_c47721_s358_s971_s54_c18164_c7262_s193_s1068_s462_s1181_c7957_s274_c7907_s196_s1216_c7896_s52_s1115_s1432_s203_s32_s739_s60_s1477_s13_s679_c23722_c23721_s34_s35_s30_s217_s1189_s578_s356_U__; __cmpiab=_92_58_272_40_231_738_539_44_50_790_39_597_14_93_149_9_511_612_264_565_224_6_66_507_211_827_195_27_259_193_501_68_793_780_155_733_728_498_797_394_742_561_956_907_647_1020_771_273_156_12_618_1106_724_128_185_30_94_620_2_315_767_243_416_378_77_56_143_138_630_85_91_938_440_209_397_707_922_122_126_584_796_168_929_213_24_45_413_773_312_1027_1_120_795_781_78_328_87_758_967_755_98_61_787_206_131_606_253_10_479_333_452_278_677_129_811_252_294_62_820_972_325_804_254_148_97_109_95_508_63_228_52_317_791_1122_142_769_358_101_311_898_737_151_20_34_37_468_130_36_23_812_373_388_31_716_509_241_617_602_1049_69_488_227_137_559_164_139_412_727_140_490_1070_297_874_226_76_81_808_835_11_192_800_703_759_108_71_4_16_371_157_84_33_80_111_276_73_82_161_115_531_134_966_937_381_857_104_13_951_655_238_950_1057_136_114_517_712_275_42_962_475_786_132_686_382_21_423_28_242_831_459_26_512_190_302_1009_601_284_282_281_32_25_70_251_154_1170_210_301_; __cmpiabc=__1_2_3_4_5_6_7_8_9_10_r1_11_; __cmpiabli=_92_231_50_790_14_93_511_612_264_195_68_733_728_394_742_907_647_156_724_30_767_378_630_85_440_209_122_126_781_967_755_98_253_452_278_252_804_63_228_52_142_898_20_468_36_23_812_509_137_559_1070_297_76_11_192_71_371_111_276_82_134_381_857_104_655_238_1057_136_475_132_21_28_284_282_32_251_154_1170_597_56_950_; __cmpiabcli=__2_7_8_9_10_11_; _wwar=ti=1736438677&rt=r&src=www.google.com&el=%252F&v=1; _wwas=1736438677; _sharedid=9fb91034-9b74-4430-99bd-3d9a060efc8f; _sharedid_cst=biz9LNosyg%3D%3D; _gcl_au=1.1.285569876.1736438748; was=bautr%C3%A4ger; _wwau=id=2403122921329640400&c=2&ti=1736438677&ti=1736499162&v=1; _wwao=ts=10&v=1; __gads=ID=1dd74b54d431685b:T=1736438748:RT=1736500262:S=ALNI_MbtE35i4siEUNBGBxLBAV7GP5T_Xg; __eoi=ID=6175e0cc5977767e:T=1736438748:RT=1736500262:S=AA-AfjYhIHYtXTvp5UMRkWyr5Q5i; utag_main=v_id:01944bcf3294002003159168e76e0506f001b067007e8$_sn:2$_ss:0$_st:1736502351109$ses_id:1736499161843%3Bexp-session$_pn:15%3Bexp-session; _wwav=ti=1736499162&pc=15&ec=612&le=1736500565&v=1',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

def get_data(): 
    page_array = ["https://www.gelbeseiten.de/suche/bautr%C3%A4ger/bundesweit"]
    final_arr = []

    for page_url in page_array:
        print(f"Scraping page: {page_url}")
        try:
            page_res = requests.get(page_url, headers=headers)
            if not page_res.ok:
                print(f"Error fetching page: {page_url}")
                continue
            page_dom = lxml.html.fromstring(page_res.text)
            
            nodes = page_dom.xpath("//div[contains(@id,'gs_treffer')]//article//@href")[0:20]
            for node in nodes:
                node_url = node if node.startswith("http") else f"https://www.gelbeseiten.de{node}"
                print(f"Fetching details from: {node_url}")
                try:
                    pro_res = requests.get(node_url, headers=headers)
                    if not pro_res.ok:
                        continue
                    pro_dom = lxml.html.fromstring(pro_res.text)
                    
                    hotel_name = pro_dom.xpath("//h1/text()")
                    hotel_name = hotel_name[0] if hotel_name else "N/A"
                    
                    phone_num = pro_dom.xpath("//div[contains(@class,'mod-Kontaktdaten__list-item contains-icon-big-fax')]/span/text()")
                    phone_num = phone_num[0] if phone_num else "N/A"
                    
                    website = pro_dom.xpath("//div[contains(@class,'contains-icon-big-homepage')]//@href")
                    website = website[0] if website else "N/A"
                    
                    email_address = pro_dom.xpath("//div[contains(@id,'email_versenden')]/@data-link")
                    email_address = email_address[0].split('mailto:')[1].split('?subject')[0] if email_address else "N/A"
                    
                    dict_data = {
                        "hotel_name": hotel_name,
                        "source_url": node_url,
                        "website": website,
                        "email_address": email_address,
                        "phone_num": phone_num
                    }
                    final_arr.append(dict_data)
                except Exception as e:
                    print(f"Error fetching or parsing the URL {node_url}: {e}")
                    continue

        except Exception as e:
            print(f"Error processing page {page_url}: {e}")
    
    # Save the data in a JSON file
    with open('scraped_data.json', 'w', encoding='utf-8') as f:
        json.dump(final_arr, f, ensure_ascii=False, indent=4)

    return final_arr

# Initialize the Translator
translator = Translator()

# Base email content (in English)
subject = "Transform Your Projects with Cutting-Edge Architectural Rendering"
html_content = """
<h1>Hello!</h1>
<p>I hope this email finds you well. My name is [Your Name], and I’m reaching out from Property Visualizer, a leading provider of architectural rendering services in the U.S.

We specialize in creating compelling visualizations that give property developers and home builders a competitive edge in showcasing and selling new construction. Our portfolio spans residential, commercial, healthcare, and hospitality projects, and we pride ourselves on helping our clients transform design visions into reality.

Here’s how we stand out:

Fast Turnaround: Deliveries in as little as 2-6 days without compromising quality.
Maximized ROI: Our visualizations turn new constructions into market-ready properties, driving significant returns.
Proven Expertise: Our case studies speak to the value we bring to our satisfied clients.
Whether you're looking to impress potential buyers with 3D tours or elevate your marketing materials, Property Visualizer is here to help.

Would you be open to discussing how we can collaborate on your upcoming projects? I’d love to schedule a quick call to explore how our services can support your goals.

Looking forward to hearing from you!

Best regards,
</p>
<p>
[Your Full Name]
[Your Position]
Property Visualizer
[Your Email Address] | [Your Phone Number]
[Website URL]</p>
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

# Function to verify email addresses using Hunter API
def verify_email(email):
    url = "https://api.hunter.io/v2/email-verifier"
    params = {
        "email": email,
        "api_key": hunter_api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('status', 'invalid')
    else:
        print(f"Error verifying email {email}: {response.text}")
        return 'invalid'

# Main function to send emails
def send_emails():
    final_arr = get_data()  # Get the scraped data
    # Extract email addresses and language preferences
    recipients = [{"email": person["email_address"], "language": person.get("language", "en")} for person in final_arr]

    # Send individual emails to each recipient
    for recipient in recipients:
        time.sleep(5)  # Delay between emails to avoid API rate limits

        # Verify the email address
        email_status = verify_email(recipient['email'])
        if email_status == 'invalid':
            print(f"Skipped email {recipient['email']} - status: invalid")
            continue

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

if __name__ == "__main__":
    send_emails()