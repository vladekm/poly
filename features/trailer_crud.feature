Feature: Trailer management
AS A manager
I WANT TO be able to manage my trailers
SO THAT my trailers are available for review

Scenario: can add a trailer
    GIVEN trailer data
    WHEN I enter the data
    THEN a trailer is instantiated

Scenario: can edit a trailer
    GIVEN trailer_id
    AND trailer data
    WHEN I enter the if and the data
    THEN trailer's data is updated

Scenario: can remove a trailer
    GIVEN trailer_id
    WHEN I call the delete interface
    THEN the trailer is removed from the system

Scenario: can search for a trailer
    GIVEN a search term
    WHEN I use the search interface while providing the search term
    THEN a list of matching trailers is presented
