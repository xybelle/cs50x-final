SELECT title FROM movies
WHERE id in (
    SELECT movie_id FROM stars
    WHERE person_id in (
        SELECT id FROM people
        WHERE name = 'Bradley Cooper', 'Jennifer Lawrence'
    )
);
