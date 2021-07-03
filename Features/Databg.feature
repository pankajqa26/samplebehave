Feature: DataAxel Multi scenario
  Background: Comon steps
    Given I am now new Launch Chrome browser


Scenario: Dataaxle Login with multiple
  When Open Dataaxle Emails pankajrajwaniya@gmail.com  passw Kipl@123
  And Click on Submit button
  Then User must successfully Login to the Home screen
  And close browsers

  Scenario: Forget on Dataaxel page with multiple
    When open DataAxel Forget pankaj@yopmail.com
    And  click on Next Button
    Then verify that the user Forget successfully
    And close browsers