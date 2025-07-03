QUESTION:
How can you produce a list of bookings on the day of 2012-09-14 which will cost the member (or guest) more than $30? 
Remember that guests have different costs to members (the listed costs are per half-hour 'slot'), 
and the guest user is always ID 0. 
Include in your output the name of the facility, the name of the member formatted as a single column, and the cost. 
Order by descending cost, and do not use any subqueries.


ANSWER:
SELECT 
  m.firstname || ' ' || m.surname AS member,
  f.name AS facility,
  CASE 
    WHEN b.memid = 0 THEN f.guestcost * b.slots
    ELSE f.membercost * b.slots
  END AS cost
FROM cd.bookings b
JOIN cd.facilities f ON b.facid = f.facid
JOIN cd.members m ON b.memid = m.memid
WHERE b.starttime::date = '2012-09-14'
  AND (
    CASE 
      WHEN b.memid = 0 THEN f.guestcost * b.slots
      ELSE f.membercost * b.slots
    END
  ) > 30
ORDER BY cost DESC, member, facility;

