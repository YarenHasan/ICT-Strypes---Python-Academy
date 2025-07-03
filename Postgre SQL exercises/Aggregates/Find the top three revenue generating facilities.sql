QUESTION:
Produce a list of the top three revenue generating facilities (including ties). 
Output facility name and rank, sorted by rank and facility name.



ANSWER:
WITH facility_revenue AS (
  SELECT
    f.name AS facility,
    SUM(
      CASE
        WHEN b.memid = 0 THEN b.slots * f.guestcost
        ELSE b.slots * f.membercost
      END
    ) AS revenue
  FROM cd.bookings b
  JOIN cd.facilities f ON b.facid = f.facid
  GROUP BY f.name
),
ranked_facilities AS (
  SELECT
    facility,
    RANK() OVER (ORDER BY revenue DESC) AS rank
  FROM facility_revenue
)
SELECT facility, rank
FROM ranked_facilities
WHERE rank <= 3
ORDER BY rank, facility;