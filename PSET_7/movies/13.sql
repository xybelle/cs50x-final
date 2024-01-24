SELECT name
FROM people
WHERE id IN (
    SELECT person_id
    FROM stars
    WHERE movie_id in (
        SELECT movie_id
        FROM stars
        WHERE person_id IN (
            SELECT id
            FROM PEOPLE
            WHERE name = 'Kevin Bacon' AND birth = '1958'
        )
    )
);
