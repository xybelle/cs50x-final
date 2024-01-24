SELECT name FROM people ORDER BY birth
JOIN stars ON people.id = stars.person_id
WHERE stars.movies_id in (
    SELECT id FROM movies
    WHERE year = '2004'
);
