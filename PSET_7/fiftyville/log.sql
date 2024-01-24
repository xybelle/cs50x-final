-- Keep a log of any SQL queries you execute as you solve the mystery.

-- To see schema
.schema

-- Check description for any witnesses in the crime_scene_reports for crime that took place
-- on 28th July, 2023
SELECT description
FROM crime_scene_reports
WHERE year = 2023 AND day = 28 AND month = 07;

-- Theft took place 10.15am at the bakery. There are 3 witnesses.
-- Check bakery_security_logs around 10.15am
SELECT hour, minute, activity, license_plate
FROM bakery_security_logs
WHERE year = 2023 AND day = 28 AND month = 07 AND hour = 10;

-- Check interviews of the 3 witnesses
SELECT id, name, transcript
FROM interviews
WHERE year = 2023 AND month = 07 AND day = 28;

-- Ruth (withness) mentioned sometime within 10 mins of the theft, thief got into a car.
-- Eugene (withness) saw thief withdrawing some money on an ATM on Leggett Street.
-- Raymond (witness) saw thief called someone on the phone (< 1 minute). Asked the other person
    -- to purchase flight ticket for earliest flight out of Fiftyville on 19th July.

-- Check people table with license_plate(s) gathered from bakery_security_logs
SELECT name, phone_number, passport_number
FROM people
WHERE license_plate IN ('R3G7486', '13FNH73', '5P2BI95', '94KL13X', '6P58WS2', '4328GD8',
    'G412CB7', 'L93JTIZ', '322W7JE', '0NTHK55', '1106N58');

-- Get origin_airport_id of Fiftyville
SELECT * FROM airports
-- | 8 | CSF | Fiftyville Regional Aiport | Fiftyville |

-- Get flight_id out of Fiftyville on July 29, 2023
SELECT id
FROM flights
WHERE origin_airport_id = 8 AND year = 2023 AND month = 07 AND day = 29;

-- Check passengers table to find if anyone from the people left or booked a flight out
    -- of Fiftyville
SELECT *
FROM passengers
WHERE passport_number in (2963008352, 7526138472, 7874488539, 7049073643, 1695452385,
    1988161715, 8496433585, 3592750733, 8294398571, 5773159633, 3642612721)
    AND flight_id in (18, 23, 36, 43, 53);
