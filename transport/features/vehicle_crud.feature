Feature: Vehicle management
AS A manager
I WANT TO be able to manage my vehicles
SO THAT my vehicles are available for review

Scenario: can add a vehicle
    GIVEN vehicle data
    WHEN I enter the data
    THEN a vehicle is instantiated

Scenario: can edit a vehicle
    GIVEN vehicle_id
    AND vehicle data
    WHEN I enter the if and the data
    THEN vehicle's data is updated

Scenario: can remove a vehicle
    GIVEN vehicle_id
    WHEN I call the delete interface
    THEN the vehicle is removed from the system

Scenario: can search for a vehicle
    GIVEN a search term
    WHEN I use the search interface while providing the search term
    THEN a list of matching vehicles is presented
