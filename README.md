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

<img width="1920" alt="allure-report" src="https://user-images.githubusercontent.com/78296112/220448531-4586d13f-09dc-4a90-a1e2-9aee1bc6db3a.png">


### Screenshot when a test fails:

<img width="1907" alt="test failed screenshot allure" src="https://user-images.githubusercontent.com/78296112/220425275-e50be92c-4f11-4ac6-a9fe-dc418b443d18.png">

