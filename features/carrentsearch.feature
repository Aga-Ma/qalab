@fixture.browser.chrome
Feature: Search car for rent
   As a user
   I'd like to search for a car to rent
   to compare available options

  Background: Car rent form setup
    Given a user visit car rent search page

  Scenario Outline: a user is able to search for a car in a specific country and city
    Given a user choose the "<Country>" and "<City>"
    And a user fill in required date fields: "07.02.2021", "28.02.2021"
    And a user click the search button
    Then results table is displayed

    Examples: Country, city pairs
    | Country | City    |
    | France  | Paris   |
    | Germany | Berlin  |
    | Poland  | Cracow  |
    | Poland  | Wroclaw |

  Scenario Outline: a user cannot chose city from another country than selected
    Given a user choose the "<Country>" and "<City>"
    And a user fill in required date fields: "07.02.2021", "28.02.2021"
    And a user click the search button
    Then results table isn't displayed

    Examples: Country, city pairs
    | Country | City   |
    | France  | Cracow |
    | Poland  | Berlin |

  Scenario: a user needs to provide dates
    Given dates fields are empty
    When a user click the search button
    Then missing date fields alert is displayed
    And results table isn't displayed

  Scenario: a user cannot set pick up date value before the drop off date value
    Given dates fields are empty
    When a user fill in required date fields: "28.02.2021", "07.02.2021"
    Then date fields alert is displayed
    And results table isn't displayed

  Scenario Outline: a user get car rent results for desired car model
    Given a user choose the "<Country>" and "<City>"
    And a user fill in required date fields: "07.02.2021", "28.02.2021"
    When a user gives car model "<Model>"
    Then the result table shows the expected model "<Model>" for rent

    Examples: Model
    | Model         |
    | Alfa Romeo    |
    | Scoda Octavia |
