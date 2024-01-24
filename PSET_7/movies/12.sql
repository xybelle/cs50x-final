SELECT title FROM movies
WHERE id in (
    SELECT movie_id FROM stars
    WHERE person_id in (
        SELECT id FROM people
        WHERE name in ('Bradley Cooper', 'Jennifer Lawrence')
    )
);
