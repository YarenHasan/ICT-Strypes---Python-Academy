QUESTION:
How can you produce a list of the start times for bookings by members named 'David Farrell'?


ANSWER:
SELECT starttime
FROM cd.bookings
JOIN cd.members on cd.bookings.memid = cd.members.memid
WHERE members.firstname = 'David' and members.surname = 'Farrell';