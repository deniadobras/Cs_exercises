# Created by denia.dobras at 06/02/2020
Feature: Google search test

  Scenario: Test google search
    Given I am on google search page
    When I type in text to search
    And I hit search button
    Then I should be on the search results page