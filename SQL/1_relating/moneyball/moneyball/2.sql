SELECT "year", "salary" FROM "salaries"
WHERE "player_id" = (
    SELECT "id" FROM "players"
    WHERE "first_name" = 'Cal' AND "last_name" = 'Ripken'
)
ORDER BY "year" DESC;



-- SELECT "year", "salary" FROM "salaries"
-- JOIN "players" ON "players"."id" = "salaries"."player_id"
-- WHERE "first_name" = 'Cal' AND "last_name" = 'Ripken'
-- ORDER BY "year" DESC;