# qalab tests

Tests were prepared with [behave](https://behave.readthedocs.io/en/stable/) framework  

To run test insatll requirements and use command `behave`
  
To generate reports install [allure](https://docs.qameta.io/allure/#_installing_a_commandline) and run tests with below command  
`behave -f allure_behave.formatter:AllureFormatter -o %allure reports dir% ./features`
