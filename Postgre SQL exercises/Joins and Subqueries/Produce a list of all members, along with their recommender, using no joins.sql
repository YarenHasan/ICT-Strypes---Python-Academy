QUESTION:
How can you output a list of all members, including the individual who recommended them (if any), 
without using any joins? Ensure that there are no duplicates in the list, 
and that each firstname + surname pairing is formatted as a column and ordered.


ANSWER:
SELECT DISTINCT
  m.firstname || ' ' || m.surname AS member,
  (
    SELECT r.firstname || ' ' || r.surname
    FROM cd.members r
    WHERE r.memid = m.recommendedby
  ) AS recommender
FROM cd.members m
ORDER BY member;