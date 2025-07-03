QUESTION:
For each day in August 2012, calculate a rolling average of total revenue over the previous 15 days. 
Output should contain date and revenue columns, sorted by the date. 
Remember to account for the possibility of a day having zero revenue.


ANSWER:
SELECT 	dategen.date,
	(
		SELECT SUM(CASE
			WHEN memid = 0 THEN slots * facs.guestcost
			ELSE slots * membercost
		END) AS rev

		FROM cd.bookings bks
		JOIN cd.facilities facs
			ON bks.facid = facs.facid
		WHERE bks.starttime > dategen.date - interval '14 days'
			AND bks.starttime < dategen.date + interval '1 day'
	)/15 AS revenue
	FROM
	(
		SELECT CAST(generate_series(TIMESTAMP '2012-08-01',
			'2012-08-31','1 day') AS DATE) AS DATE
	)  AS dategen
ORDER BY dategen.date;