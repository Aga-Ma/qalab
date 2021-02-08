@fixture.browser.chrome
Feature: Confirm car rent
   As a user
   I"d like give personal data in car rent form
   to finalize rent for chosen car

  Background: Car rent form setup
    Given a user searched for a car to rent

  Scenario: a user is able to provide personal data in the rent form
    Given a user goes to rent form
    When a user enters the personal data
    And a user click rent
    Then car rent is successful

  Scenario: a user cannot rent car without filling out the name
    Given a user goes to rent form
    When a user enters last name, card number and email
    And a user click rent
    Then alert "Name is required" is displayed

  Scenario: a user cannot rent a car without filling out the last name
    Given a user goes to rent form
    When a user enters name, card number and email
    And a user click rent
    Then alert "Last name is required" is displayed

  Scenario: a user cannot rent a car without filling out the card number
    Given a user goes to rent form
    When a user enters name, last name and email
    And a user click rent
    Then alert "Card number is required" is displayed

  Scenario: a user cannot rent a car without filling out the email address
    Given a user goes to rent form
    When a user enters name, last name and card number
    And a user click rent
    Then alert "Email is required" is displayed

  Scenario: a user cannot rent a car with giving invalid email address
    Given a user goes to rent form
    When a user enters name, last name, card number and invalid email
    And a user click rent
    Then alert "Please provide valid email" is displayed

  Scenario: a user cannot rent a car with giving invalid card number
    Given a user goes to rent form
    When a user enters name, last name, invalid card number and email
    And a user click rent
    Then alert "Card number contains wrong chars" is displayed