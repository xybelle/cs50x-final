SELECT name FROM people
WHERE id IN (
    SELECT person_id FROM stars
    WHERE movie_id in (
        SELECT movie_id FROM STARS
        WHERE person_id IN (
            SELECT id IN PEOPLE
            WHERE name = 'Kevin Bacon' AND birth = '1958'
        )
    )
);
