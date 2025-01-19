{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "2b1e9b87-884f-48a2-ba6b-cc8c49a4934a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import selenium\n",
    "from selenium import webdriver\n",
    "import time\n",
    "\n",
    "from selenium.webdriver.common.by import By\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "\n",
    "from selenium.webdriver.chrome.service import Service\n",
    "from selenium.webdriver.chrome.options import Options\n",
    "\n",
    "from twilio.rest import Client"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "a0a357d2-839f-48ea-a2a9-fe87bc9ebdd0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "94,900\n",
      "Message sent! SID: SM481020a91b517a00ceb5033db94bc79b\n"
     ]
    }
   ],
   "source": [
    "\n",
    "\n",
    "brave_path = r\"C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\Brave.exe\"\n",
    "\n",
    "options = Options()\n",
    "options.binary_location = brave_path\n",
    "options.add_argument(\"--disable-popup-blocking\")\n",
    "\n",
    "chromedriver_path = r\"C:/Users/hp/Downloads/chromedriver-win64/chromedriver.exe\"\n",
    "prefs = {\n",
    "        \"profile.default_content_setting_values.notifications\": 2,  # Block notifications\n",
    "        \"profile.default_content_setting_values.geolocation\": 1,    # Allow location\n",
    "        \"profile.default_content_setting_values.media_stream_camera\": 1,  # Allow camera\n",
    "        \"profile.default_content_setting_values.media_stream_mic\": 1, \n",
    "        \"download.default_directory\": r\"/C:\\Users\\hp\\Downloads\",  # Specify the folder\n",
    "        \"download.prompt_for_download\": False,  # Disable the save dialog\n",
    "        \"download.directory_upgrade\": True,  # Allow automatic downloads\n",
    "        \"safebrowsing.enabled\": True,  \n",
    "    }\n",
    "\n",
    "options.add_experimental_option(\"prefs\", prefs)\n",
    "\n",
    "service = Service(chromedriver_path)\n",
    "driver = webdriver.Chrome(service = service, options = options)\n",
    "\n",
    "driver.get(\"https://www.amazon.in/iPhone-16-Plus-256-GB/dp/B0DGHT4K6Q/ref=sr_1_3?sr=8-3\")\n",
    "\n",
    "cost = driver.find_element(By.XPATH, '//*[@id=\"corePriceDisplay_desktop_feature_div\"]/div[1]/span[3]/span[2]/span[2]')\n",
    "print(cost.text)\n",
    "\n",
    "number = int(cost.text.replace(\",\", \"\"))\n",
    "\n",
    "time.sleep(3)\n",
    "driver.quit()\n",
    "\n",
    "account_sid = 'ACf1a5f9b83e503ad48720637395591e9e' \n",
    "auth_token = '0212c384747f76ce0e3023dedd37284b'    \n",
    "client = Client(account_sid, auth_token)\n",
    "\n",
    "\n",
    "if number < 90000:\n",
    "    message = client.messages.create(\n",
    "        from_='whatsapp:+14155238886',  \n",
    "        body=f\"HeYYYY!! \\n\\nThe Iphone 16 plus 256 gb price has come down!! \\n\\nIt's about {number} ig \\n\\nGo check it out!! \",\n",
    "        to='whatsapp:+919209644282' )\n",
    "    \n",
    "print(f\"Message sent! SID: {message.sid}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "2ccb136b-8202-4d07-ba41-db4e63b1d1e4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Message sent! SID: SM024ee8c0112b61c244d4f9fda25e8788\n"
     ]
    }
   ],
   "source": [
    "account_sid = 'ACf1a5f9b83e503ad48720637395591e9e' \n",
    "auth_token = '0212c384747f76ce0e3023dedd37284b'    \n",
    "client = Client(account_sid, auth_token)\n",
    "\n",
    "message = client.messages.create(\n",
    "    from_='whatsapp:+14155238886',  \n",
    "    body=\"HEYYY!!! \\n\\nDon't be scared lol, this is me Yadh, I'm sending this message from a third party app. \\n\\nDamn this is super fun!! \\n\\nNah don't reply lol, it wouldn't reach me. Just see it and let me know if you got this or not \\n\\nHehe, little dummy, it'll also serve as a reminder each time this code is run. I'm trying to automate it.\",\n",
    "    to='whatsapp:+919175899169' )\n",
    "    \n",
    "print(f\"Message sent! SID: {message.sid}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f7b194a5-a2d0-4ce6-8525-31faf01bee92",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
