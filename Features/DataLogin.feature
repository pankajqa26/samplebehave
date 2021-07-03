Feature: DataAxel Forget
Scenario: Dataaxle Login
  Given I am now Launch Chrome browser
  When Open Dataaxle Emails pankajrajwaniya@gmail.com  passw Kipl@123
  And Click on Submit button
  Then User must successfully Login to the Home screen
  And close browsers

  Scenario Outline: Dataaxle Login
    Given I am now Launch Chrome browser
    When Open Dataaxle Emails <Emails>  passw <passw>
    And Click on Submit button
    Then User must successfully Login to the Home screen

Examples:
  | Emails | passw |
  | admin | admin123 |
  | admin123 | admin123 |
