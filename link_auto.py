import requests as re

user_email = input("Please enter an email to find LinkedIn account of: ")

url = "https://www.linkedin.com/checkpoint/lg/login-submit"
headers= {"Host": "www.linkedin.com",
"Cookie": 'li_rm=AQFgmKjP1C0IWwAAAX-G3sIRXEpwzDajaN-n4_K_2rCB6UVRnvxf3JoRf2PmoBKTriWk1NAfD3EL0ERo-CmwS5J3Al-eJ_EioLamKkNbfjp4gkssmwSytmKv; bcookie="v=2&375fca82-fcf6-446a-8235-7520aa1e5a53"; bscookie="v=1&20220314052019d70fbc1d-3da3-45f1-84db-c72a881b3201AQGavQxvdd13MQb36x7tEmB43e6jRTpq"; aam_uuid=48348941286481132201509647802196001533; _gcl_au=1.1.947841861.1647270736; G_ENABLED_IDPS=google; lidc="b=TGST01:s=T:r=T:a=T:p=T:g=2792:u=1:x=1:i=1648093222:t=1648179622:v=2:sig=AQFBsUcB55h8LG7pih02UYGkDWXFJHlb"; chp_token=AgEEn0jtpd4PGAAAAX-6D8xeunORltyvUa4UQ2k90zCI8vtmTz0SJd4jGdEOXOi2_-CFEc2dBz_foa00K1MxesN4ORI; lang=v=2&lang=en-us; JSESSIONID=ajax:1192403761480292085; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19075%7CMCMID%7C48886064540488661911458171847322726710%7CMCAAMLH-1648723043%7C12%7CMCAAMB-1648723043%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1648125443s%7CNONE%7CvVersion%7C5.1.1',
"Content-Length": "11727",
"Cache-Control": 'max-age=0',
"Sec-Ch-Ua": '"(Not(A:Brand";v="8", "Chromium";v="99"',
"Sec-Ch-Ua-Mobile": "?0",
"Sec-Ch-Ua-Platform": '"Windows"',
"Upgrade-Insecure-Requests": "1",
"Origin": "https://www.linkedin.com",
"Content-Type": "application/x-www-form-urlencoded",
"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
"Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
"Sec-Fetch-Site":"same-origin",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-User": "?1",
"Sec-Fetch-Dest": "document",
"Referer": "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "en-US,en;q=0.9"}

params = {"csrfToken":"ajax%3A1192403761480292085","session_key":user_email,"ac":"0","sIdString":"aedd79d9-401a-49ed-88df-1fde88bc8ea1","parentPageKey":"d_checkpoint_lg_consumerLogin","pageInstance":"urn%3Ali%3Apage%3Ad_checkpoint_lg_consumerLogin%3BkUGcdhHMReuiv5xpCmVvJA%3D%3D","trk":"guest_homepage-basic_nav-header-signin","loginCsrfParam":"375fca82-fcf6-446a-8235-7520aa1e5a53","fp_data":"default","_d":"d","showGoogleOneTapLogin":"true","controlId":"d_checkpoint_lg_consumerLogin-login_submit_button","session_password":"123123123"}

res = re.post(url,headers=headers,data=params)

#print(res.text)
print(res.status_code)

if("Couldn’t find a LinkedIn account associated with this email. Please try again." in res.text):
    print("\nThere is no Linkedin account linked to this email!")
else:
    print("\nThere is exists an account linked with this email")
