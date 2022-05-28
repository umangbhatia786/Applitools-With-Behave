Feature: Search Book Page

@CheckRegion
Scenario Outline: To Search for a book and verify Search Result Region
  Given We enter the search text as <text>
  Then Verify the book result region using applitools eyes


Examples:
    | text          |
    | Google        |

@FilterBooks
Scenario Outline: To Search for a book and verify Search Results
  Given We enter the search text as <text>
  Then We verify the books by title as <title>

Examples:
    | text          | title            |
    | Agile         | Agile Testing    |

