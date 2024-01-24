SELECT title FROM movies
JOIN ratings ON movies.id = ratings.movie_id
WHERE movies.id IN (
    SELECT id FROM stars
    WHERE person_id = (
        SELECT id FROM people
        WHERE name = 'Chadwick Boseman'
    )
) ORDER BY rating ASC LIMIT 5;
