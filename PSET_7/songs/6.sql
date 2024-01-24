SELECT name FROM songs
WHERE artist_id = (
    SELECT id FROM songs
    WHERE name = 'Post Malone'
);
