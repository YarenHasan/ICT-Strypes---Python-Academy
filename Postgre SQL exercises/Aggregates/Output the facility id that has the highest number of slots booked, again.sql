QUESTION:
Output the facility id that has the highest number of slots booked. 
Ensure that in the event of a tie, all tieing results get output.


ANSWER:
WITH slots_per_facility AS (
  SELECT facid, SUM(slots) AS total_slots
  FROM cd.bookings
  GROUP BY facid
),
max_slots AS (
  SELECT MAX(total_slots) AS max_total
  FROM slots_per_facility
)
SELECT facid, total_slots as total
FROM slots_per_facility
WHERE total_slots = (SELECT max_total FROM max_slots);