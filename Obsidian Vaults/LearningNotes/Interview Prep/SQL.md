# SQL

Created: July 29, 2021 12:14 PM

[Mode SQL Tutorial | - Mode](https://mode.com/sql-tutorial/)

[Visual JOIN](https://joins.spathon.com/)

String functions in SQL:

1. % matches anything
2. “-” matches exactly one character (only used with like or not like)
3. “LIKE” for Case insensitive exact string comparison
4. POSITION allows you to specify a substring, then returns a numerical value equal to the index (counting from left) where that substring first appears in the target string. eg - POSITION('A' IN descript) AS a_position
5. SUBSTR(*string*, *starting character position*, *# of characters*)
6. CONCAT(day_of_week, ', ', LEFT(date, 10)) AS day_and_date
7. COALESCE to replace the null values: `COALESCE(descript, 'No Description')`
8.