QUESTION:
How can you output a list of all members who have recommended another member? 
Ensure that there are no duplicates in the list, and that results are ordered by (surname, firstname).


ANSWER:
SELECT DISTINCT member_who_recomments.firstname, member_who_recomments.surname
FROM cd.members as recommended_member
JOIN cd.members as member_who_recomments ON recommended_member.recommendedby = member_who_recomments.memid
ORDER BY member_who_recomments.surname, member_who_recomments.firstname;