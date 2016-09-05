Feature: Load management
    As a manager
    I want to be able to manage my loads
    So that my loads are available for review

Scenario: Manager can add a load
    Given load data
    When I enter the data
    Then a load is instantiated

Scenario: Manager can edit a load
    Given load_id
    And load data
    When I enter the if and the data
    Then load's data is updated

Scenario: Manager can remove a load
    Given load_id
    When I call the delete interface
    Then the load is removed from the system

Scenario: Manager can search for a load
    Given a search term
    When I use the search interface while providing the search term
    Then a list of matching loads is presented
