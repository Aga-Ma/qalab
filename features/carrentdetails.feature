@fixture.browser.chrome
Feature: Get rent car details
   As a user
   I'd like to verify car rent details
   to verify if the chosen option suits me

  Scenario: a user is able to see car details after clicking "Rent"
    Given a user enters all data on car rent search page
    And results table is displayed
    When a user click the Rent button
    Then the rent details page is displayed
    And car details are available
