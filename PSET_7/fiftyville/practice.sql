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

-- Get origin_airport_id of Fiftyville
SELECT * FROM airports

-- | 8 | CSF | Fiftyville Regional Aiport | Fiftyville |

-- Check earliest flight out of Fiftyville
SELECT * FROM flights
WHERE origin_airport_id = 8 AND year = 2023 AND month = 07 AND day = 29;

-- Earliest flight out of Fiftyville is flight_id: 36 followed by 43, 23, 53, 18

-- Check passengers who booked flight_id: 36, who also made a call to someone on the 28th July,
    -- 2023 in less than a minute, who may also withdrew money from ATM in Leggett Street,
    -- and also may be around the bakery around 10.15am.
SELECT name, phone_number, license_plate FROM people
WHERE passport_number in (
    SELECT passport_number FROM passengers
    WHERE flight_id = 36
) AND id IN (
    SELECT person_id FROM bank_accounts
    WHERE account_number in (
        SELECT account_number FROM atm_transactions
        WHERE transaction_type = 'withdraw' AND year = 2023 AND month = 07 AND day = 28
    )
) AND phone_number in (
    SELECT caller FROM phone_calls
    WHERE duration <= 60 AND year = 2023 AND month = 07 AND day = 28
) AND license_plate in (
    SELECT license_plate FROM bakery_security_logs
    WHERE year = 2023 AND month = 07 AND day = 28 AND hour = 10
);
