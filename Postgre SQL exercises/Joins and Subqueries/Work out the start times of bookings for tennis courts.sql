QUESTION:
How can you produce a list of the start times for bookings for tennis courts, 
for the date '2012-09-21'? Return a list of start time and facility name pairings, ordered by the time.


ANSWER:
SELECT starttime, facilities.name
FROM cd.bookings
JOIN cd.facilities  ON cd.bookings.facid = cd.facilities.facid
WHERE facilities.name LIKE 'Tennis Court%' AND bookings.starttime::date = '2012-09-21'
ORDER BY bookings.starttime;