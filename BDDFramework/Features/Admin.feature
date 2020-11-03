#noinspection CucumberUndefinedStep
Feature: Login Customer to my application and Perform Admin Functionality.

  Scenario:
    When User navigated to the Login Page
    And User enters username "Admin"
    And User enters password "admin123"
    And User click on the Login button
    Then User should be Logged In Successfully

   Scenario: Enter details of Admin Page
     Given User move cursor to Admin
     When User move cursor to the User Management Text
     And Click on the Users Button
     And Enter username "Admin"
     And Select user Role from drop down
     And Enter Employee Name
     And Select Status from Drop down
     And Click on the Search Button
     And Search Result Displayed
     Then Verify the Values of Status Column