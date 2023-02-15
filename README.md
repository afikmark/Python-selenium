# Automation Testing project
This is a testing automation project that tests a fake online store:
https://atid.store/

### Project's language and frameworks 
* Python
* Pytest
* Selenium

### Run:
cd to page_tests directory

enter ```"pytest --alluredir=.\allure-results"```
in the terminal
### view report:
enter 
```" pytest allure serve .\allure-results" ``` 
in the terminal
### parallel run:
add ```-n "number of threads"```
i.e. ``` pytest allure serve .\allure-results -n 4 ```

<img width="1915" alt="allure report " src="https://user-images.githubusercontent.com/78296112/218312301-c5210c62-1b92-4f59-95e4-1209915cd8e0.png">
