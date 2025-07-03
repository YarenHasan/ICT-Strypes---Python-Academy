QUESTION:
Produce a monotonically increasing numbered list of members (including guests), 
ordered by their date of joining. Remember that member IDs are not guaranteed to be sequential.


ANSWER:
SELECT 
  ROW_NUMBER() OVER (ORDER BY joindate) AS row_number,
  firstname as first_name, surname 
FROM cd.members;