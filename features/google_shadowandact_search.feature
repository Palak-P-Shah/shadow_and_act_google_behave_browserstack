Feature: Search for the S&A in google and browse the home page- BrowserStack

  Scenario: Search for the S&A in google and browse the home page- BrowserStack
      Given the browser is launched and navigating to the Google.com page
      #Then navigate to the Google.com page
      Then search for "Shadow & Act" keyword
      Then Navigate to the Shadow&Act application page from the Google search results
      Then verify the application is launched successfully
      Then navigate to the Film page
      Then verify if all the article links are working as expected on the Film page
      Then verify if the Load More stories button work as expected, also verify the links to the articles works as expected
      Then verify if the Load More stories button work as expected (the second time when clicked), also verify initial link of the article, after clicking load more twice do work as expected
      Then verify footer section is present and displayed
      #Then close the browser