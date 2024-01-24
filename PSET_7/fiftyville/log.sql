-- Keep a log of any SQL queries you execute as you solve the mystery.

-- To see schema
.schema

-- Check description for any witnesses in the crime_scene_reports for crime that took place
-- on 28th July, 2023
SELECT description
FROM crime_scene_reports
WHERE year = 2023 AND day = 28 AND month = 07;

-- It was mentioned there are 3 witnesses who were present at the time and all mentions the bakery

