# Automation Testing project
This is a testing automation project that tests a fake online store:
https://atid.store/

### Project's language and frameworks 
* Python
* Pytest
* Selenium


### Runing Tests:
Clone project to your machine

make sure you have Chrome/Firefox/Edge(default on windows) installed.

cd to page_tests directory

This project uses the RUN_ENV environment variable to control whether tests are run locally or on a docker container.
To run tests locally, set the value of the RUN_ENV environment variable to 'local'.
To run tests on a docker container, set the value of the RUN_ENV environment variable to 'docker'.
Add the following prefixes before the pytest command:

### Windows
To run tests locally on a Windows machine, open a command prompt and use the following command:

```set RUN_ENV=local && pytest ```

#### PowerShell:
``` $env:RUN_ENV='local'; pytest```

To run tests on a docker container on a Windows machine, open a command prompt and use the following command:

```set RUN_ENV=docker && pytest ```

#### PowerShell:
``` $env:RUN_ENV='docker'; pytest```


### Linux and macOS

To run tests locally on a Linux or macOS machine, open a terminal and use the following command:

```RUN_ENV=local pytest ```

To run tests on a docker container on a Linux or macOS machine, open a terminal and use the following command:

```RUN_ENV=docker pytest ```

### running tests with allure-report:

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

