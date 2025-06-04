# tabs-lite-ug-import
Import your favorites from Ultimate Guitar Tabs to Tabs Lite import favorites json format.

## Requirements
Python installed - I have only verified that this works with python 3.12, but most other versions probably also work. Make sure you add python to your path when installing.
Python installation page: https://www.python.org/downloads/

## Instructions

### Extract json file
Go to the my tabs page and scroll down to the bottom. Then hit the button labeled "All" next to "Per Page" so that every favorited tab is shown on the html page at the same time.

My tabs link: https://www.ultimate-guitar.com/user/mytabs

Then copy the contents of the javascript file stored in this repository named extract_ug_favorites.js and paste it into the developer console of your browser and press enter.
That will download a tabs.csv to your Downloads folder.

Download the create_tabs_lite_json.py and place it into the same folder as your csv file. Open your operating system's terminal at the file location where your tabs.csv and python file are located. 

Then run the python script by typing

`python create_tabs_lite_json.py` on linux and mac and windows cmd
`python .\create_tabs_lite_json.py` in powershell

### Import json file
transfer the json file to your device where you are running tabs lite (for me it's android, so i emailed it to myself and downloaded it, feel free to also just plug your device into your pc and transfer it, or any other way you want)

Go into tabs lite and hit the guitar icon in the top left and hit import favorites and playlists and select your json file. Wait for it to finish importing, it may take a few minutes if you have many tabs (the progress was shown for me as a orange circle around the tabs icon in the top left)
Finally, enjoy your imported tabs!
