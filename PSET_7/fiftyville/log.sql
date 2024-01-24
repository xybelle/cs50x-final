-- Keep a log of any SQL queries you execute as you solve the mystery.

-- To see schema
.schema

-- Check crime_scene_reports for crime that took place on 28th July, 2023 on Humphrey Street
SELECT *
FROM crime_scene_reports
WHERE year = '2023' AND day = '28' AND month = 'July';


