Feature: Load management
AS A manager
I WANT TO be able to manage my loads
SO THAT my loads are available for review

Scenario: can add a load
    GIVEN load data
    WHEN I enter the data
    THEN a load is instantiated

Scenario: can edit a load
    GIVEN load_id
    AND load data
    WHEN I enter the if and the data
    THEN load's data is updated

Scenario: can remove a load
    GIVEN load_id
    WHEN I call the delete interface
    THEN the load is removed from the system

Scenario: can search for a load
    GIVEN a search term
    WHEN I use the search interface while providing the search term
    THEN a list of matching loads is presented
