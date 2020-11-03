#noinspection CucumberUndefinedStep
Feature: Login Customer to my application and Perform Job Page Functionality.

   Scenario: Enter details of Job Title Page
     Given User move cursor to the Job Menu Text
     When Click on the Job Title Button
     And Click Add Button
     And Enter Job Title "Software Engineers"
     And Enter Job Description "Testing Engineer"
     And Select Job File
     Then Click Save Button

   Scenario: Enter Details of Pay Grade Page
     Given User move cursor to Admin
     When User move cursor to the Job Menu Text
     And Click on the Pay Grade Button
     Then Check Pay Grade Column Presence
     And Click Add Button
     And Enter Pay Grade Name "Engineers"
     Then Click Save Button

   Scenario: Enter Details of Employment Page
     Given User move cursor to Admin
     When User move cursor to the Job Menu Text
     And Click on the Employment Status Button
     Then Check Employment Status Column Presence
     And Click Add Button
     And Enter Employment Name "Engineers"
     Then Click Save Button

   Scenario: Enter Details of Job Category Page
     Given User move cursor to Admin
     When User move cursor to the Job Menu Text
     And Click on the Job Category Button
     Then Check Job Category Column Presence
     And Click Add Button
     And Enter Job Category Name "Engineers"
     Then Click Save Button

   Scenario: Enter Details of Work Shift Page
     Given User move cursor to Admin
     When User move cursor to the Job Menu Text
     And Click on the Work Shift Button
     Then Check Shift Name Column Presence
     And Click Add Button
     And Enter Work Shift Name "Engineers"
     And Select Work Shift Timings From
     And Select Work Shift Timings To
     Then Check Presence Of Duration
     And Select Available Employee
     And Click AddEmployee Button
     And Select Assigned Employee
     Then Click Save Button