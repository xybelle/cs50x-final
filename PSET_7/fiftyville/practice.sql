-- Keep a log of any SQL queries you execute as you solve the mystery.

-- To see schema
.schema

-- Check for more info in the crime_scene_reports for theft that took place on 28th July, 2023
SELECT description
FROM crime_scene_reports
WHERE year = 2023 AND day = 28 AND month = 07;

-- Theft took place 10.15am at the bakery. There are 3 witnesses.

-- Check interviews of the 3 witnesses if there are more info
SELECT id, name, transcript
FROM interviews
WHERE year = 2023 AND month = 07 AND day = 28;

-- Ruth (withness) mentioned sometime within 10 mins of the theft, thief got into a car.
-- Eugene (withness) saw thief withdrawing some money on an ATM on Leggett Street.
-- Raymond (witness) saw thief called someone on the phone (< 1 minute). Asked the other person
    -- to purchase flight ticket for earliest flight out of Fiftyville on 29th July.


