#  Test Automation for IKEA Home Smart App

# Tools/SW used to develop test cases and generate test report
* Appium server GUI ()
* Appium Inspector ()
* Python 3.12.+
* pytest
* pytest plugin `pytest-html`
* Allure - for test case

## Installations steps
* Install IKEA Home smart app from 
[https://play.google.com/store/apps/details?id=com.ikea.inter.homesmart.system2&pcampaignid=web_share]
* Install Java
[https://www.oracle.com/java/technologies/downloads/]
* Install Android Studio and additional SDK tools
[https://developer.android.com/studio/install]
* Install Python
[https://www.python.org/downloads/]
* Install Appium server GUI
[https://github.com/appium/appium-desktop/releases]
* Install Appium Desktop client
[https://appium.io/docs/en/latest/quickstart/install/]
* Install Appium Inspector
[https://github.com/appium/appium-inspector/releases]
* Install PyCharm
[https://www.jetbrains.com/pycharm/download]
* Install allure for test report
[https://allurereport.org/docs/install/]
* Install pytest 
  pip install pytest
* Install pytest-ordering
  pip install pytest-ordering
* Install Vysor app
* [https://www.vysor.io/download/]

## Execute the test cases

* Android Developer options 
[https://developer.android.com/studio/debug/dev-options]
* Connect your Android device through USB and verify the adb    
* Execute tests : Go to the project folder
* Clone repository `git clone https://github.com/devrajuyadav/Assessment.git`
* Execute `pytest --alluredir=allure-results` This will run all the test cases and create a allure-results folder with the test result>
* To generate allure report Run `pytest generate allure-results -o allure-report`
* Show the report: Run `allure serve allure-results`