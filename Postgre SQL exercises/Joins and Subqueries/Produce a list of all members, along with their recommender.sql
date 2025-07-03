QUESTION:
How can you output a list of all members, including the individual who recommended them (if any)? 
Ensure that results are ordered by (surname, firstname).


ANSWER:
SELECT 
  main_member.firstname AS member_first_name,
  main_member.surname AS member_surname,
  recommender.firstname AS recommender_first_name,
  recommender.surname AS recommender_surname
FROM cd.members main_member
LEFT JOIN cd.members recommender ON main_member.recommendedby = recommender.memid
ORDER BY main_member.surname, main_member.firstname;