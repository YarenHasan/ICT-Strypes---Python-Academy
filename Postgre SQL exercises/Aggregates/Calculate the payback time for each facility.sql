QUESTION:
Based on the 3 complete months of data so far, 
calculate the amount of time each facility will take to repay its cost of ownership. 
Remember to take into account ongoing monthly maintenance. 
Output facility name and payback time in months, order by facility name. 
Do not worry about differences in month lengths, we are only looking for a rough value here!



ANSWER:
SELECT 	f.name AS name,
	f.initialoutlay/((SUM(CASE
			WHEN memid = 0 THEN slots * f.guestcost
			ELSE slots * membercost
		END)/3) - f.monthlymaintenance) AS months
	FROM cd.bookings b
	JOIN cd.facilities f
		ON b.facid = f.facid
	GROUP BY f.facid
ORDER BY name;