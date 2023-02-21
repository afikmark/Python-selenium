# Automation Testing project
This is a testing automation project that tests a fake online store:
https://atid.store/

### Project's language and frameworks 
* Python
* Pytest
* Selenium


### Run:
Clone project to your machine

make sure you have Chrome/Firefox/Edge(default on windows) installed.


for local run add ```local=True``` in basetest.py

<img width="443" alt="local run " src="https://user-images.githubusercontent.com/78296112/219883299-e0d20492-d8b2-464a-8ead-b0345e720645.png">

cd to page_tests directory

enter ```pytest --alluredir=.[project directory]\allure-results``` in the terminal.

### view report:
enter 
```pytest allure serve .\allure-results ``` in the terminal
### parallel run:
add ```-n [number of threads]```
i.e. ``` pytest --alluredir=[project directory]\allure-results -n 4 ```

<img width="1438" alt="allure-report" src="https://user-images.githubusercontent.com/78296112/219883423-6f82f40c-ce8b-442e-90cd-95fe9fcf9e39.png">
