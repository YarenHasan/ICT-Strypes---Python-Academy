QUESTION:
The Produce a list of costly bookings exercise contained some messy logic: 
we had to calculate the booking cost in both the WHERE clause and the CASE statement.
Try to simplify this calculation using subqueries. For reference, the question was:
  How can you produce a list of bookings on the day of 2012-09-14 which will cost the member (or guest) more than $30? 
  Remember that guests have different costs to members (the listed costs are per half-hour 'slot'), 
  and the guest user is always ID 0. Include in your output the name of the facility, 
  the name of the member formatted as a single column, and the cost. Order by descending cost.



ANSWER:
WITH booking_costs AS (
  SELECT
    f.name AS facility,
    CASE 
      WHEN b.memid = 0 THEN 'GUEST GUEST'
      ELSE m.firstname || ' ' || m.surname
    END AS member,
    CASE 
      WHEN b.memid = 0 THEN f.guestcost * b.slots
      ELSE f.membercost * b.slots
    END AS cost
  FROM cd.bookings b
  JOIN cd.facilities f ON b.facid = f.facid
  JOIN cd.members m ON b.memid = m.memid
  WHERE b.starttime::date = '2012-09-14'
)
SELECT member, facility, cost
FROM booking_costs
WHERE cost > 30
ORDER BY cost DESC, member, facility;