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
