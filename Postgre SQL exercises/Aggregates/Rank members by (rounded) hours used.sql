QUESTION:
Produce a list of members (including guests), 
along with the number of hours they have booked in facilities, rounded to the nearest ten hours. 
Rank them by this rounded figure, producing output of first name, surname, rounded hours, rank. 
Sort by rank, surname, and first name.


ANSWER:
WITH hours_booked AS (
  SELECT
    b.memid,
    m.firstname,
    m.surname,
    ROUND(SUM(b.slots) * 0.5 / 10.0) * 10 AS rounded_hours
  FROM cd.bookings b
  JOIN cd.members m ON b.memid = m.memid
  GROUP BY b.memid, m.firstname, m.surname
),
ranked_hours AS (
  SELECT
    firstname,
    surname,
    rounded_hours,
    RANK() OVER (ORDER BY rounded_hours DESC) AS rank
  FROM hours_booked
)
SELECT firstname, surname, rounded_hours, rank
FROM ranked_hours
ORDER BY rank, surname, firstname;