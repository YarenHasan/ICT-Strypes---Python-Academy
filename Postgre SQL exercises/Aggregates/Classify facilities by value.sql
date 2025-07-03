QUESTION:
Classify facilities into equally sized groups of high, average, and low based on their revenue. 
Order by classification and facility name.



ANSWER:
SELECT
  facility AS name,
  CASE
    WHEN ntile = 1 THEN 'high'
    WHEN ntile = 2 THEN 'average'
    WHEN ntile = 3 THEN 'low'
  END AS revenue
FROM (
  SELECT
    f.name AS facility,
    NTILE(3) OVER (ORDER BY SUM(
      CASE
        WHEN b.memid = 0 THEN b.slots * f.guestcost
        ELSE b.slots * f.membercost
      END
    ) DESC) AS ntile
  FROM cd.bookings b
  JOIN cd.facilities f ON b.facid = f.facid
  GROUP BY f.name
) ranked
ORDER BY
  CASE
    WHEN ntile = 1 THEN 1
    WHEN ntile = 2 THEN 2
    WHEN ntile = 3 THEN 3
  END,
  name;