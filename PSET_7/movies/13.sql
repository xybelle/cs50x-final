SELECT name FROM people
WHERE name = 'Kevin Bacon' AND birth = '1958'
AND WHERE id IN (
    SELECT person_id FROM stars
    WHERE movie_id 
)
