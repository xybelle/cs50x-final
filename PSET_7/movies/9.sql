SELECT name FROM people ORDER BY birth
WHERE id IN (
    SELECT person_id FROM stars
    WHERE movie_id = (
        SELECT id FROM movies
        WHERE year = '2004'
    )
);
