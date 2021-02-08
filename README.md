# qalab tests

Tests were prepared with [behave](https://behave.readthedocs.io/en/stable/) framework  

## Installation
[Python3](https://www.python.org/downloads/)  
[Virtualenv](https://virtualenv.pypa.io/en/stable/) or [Pipenv](https://github.com/pypa/pipenv)  
[requirements](./requirements.txt) with `pip install -r requirements.txt` in your virtual environement  
### Download  
[Chrome](https://www.google.com/intl/pl_pl/chrome/) and matching [chromedriver](https://chromedriver.chromium.org/downloads)   
  
## Tests execution  
[Run tests](https://behave.readthedocs.io/en/stable/tutorial.html) with command `behave`
  
## Optional
To generate reports install [allure](https://docs.qameta.io/allure/#_installing_a_commandline) and run tests with below command  
`behave -f allure_behave.formatter:AllureFormatter -o %allure reports dir% ./features`
