-- Get origin and destination airport of flight out of Fiftyville on the 29th July, 2023

SELECT * FROM flights
WHERE origin_airport_id in (
    SELECT id FROM airports
    WHERE city = 'Fiftyville'
) AND year = 2023 AND month = 07 AND day = 29;
