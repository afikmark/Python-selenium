# Automation Testing project
This is a testing automation project that tests a fake online store:
https://atid.store/

### Project's language and frameworks 
* Python
* Pytest
* Selenium

### Run:
cd to page_tests directory

enter ```pytest --alluredir=.\allure-results```
in the terminal
### view report:
enter 
```" pytest allure serve .\allure-results ``` 
in the terminal
### parallel run:
add ```-n [number of threads]```
i.e. ``` pytest pytest --alluredir=[directory] -n 4 ```


<img width="1916" alt="allure-report" src="https://user-images.githubusercontent.com/78296112/219169409-16c304ea-0322-4dcb-8352-00185e4d6912.png">
