# IKEA Smart Home App Test Automation

# Tools/SW used to develop test cases and generate test report
* Appium server GUI ()
* Appium Inspector ()
* Python 3.12.+
* pytest
* pytest plugin `pytest-html`
* Allure

## Installations steps
* Install IKEA Home smart app from 
[https://play.google.com/store/apps/details?id=com.ikea.inter.homesmart.system2&pcampaignid=web_share]
* Install python
[https://www.python.org/downloads/]
* Install Appium server GUI
[https://github.com/appium/appium-desktop/releases]
* Install appium
[https://appium.io/docs/en/latest/quickstart/install/]
* Install Appium Inspector
[https://github.com/appium/appium-inspector/releases]
* Install PyCharm
[https://www.jetbrains.com/pycharm/download]
* Install allure for test report
[https://allurereport.org/docs/install/]
* Install pytest 
pip install pytest
* Install Android Studio
* [https://developer.android.com/studio/install]

## Execute the test cases

* Android Developer options 
[https://developer.android.com/studio/debug/dev-options]
* Connect your Android device through USB and verify the adb    
* Execute tests : Go to the project folder
* Clone this repository `https://github.com/devrajuyadav/Assessment.git`
* Execute `pytest --alluredir=allure-results` This will run all the test cases and create a allure-results folder with the test result>
* To generate allure report Run `pytest generate allure-results -o allure-report`
* Show the report: Run `allure serve allure-results`