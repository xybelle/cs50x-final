SELECT id FROM movies
JOIN stars ON movies.id = stars.movie_id
WHERE stars.person_id IN (
    SELECT name FROM people
    ORDER BY birth
);
