SELECT "first_name", "last_name" FROM "players"
WHERE "players"."id" IN (
    SELECT "players"."id" FROM "players"
    JOIN "salaries" ON "players"."id" = "salaries"."player_id"
    JOIN "performances" ON "players"."id" = "performances"."player_id"
    AND "performances"."year" = "salaries"."year"
    WHERE "salaries"."year" = '2001' AND "performances"."H" != 0
    ORDER BY "salary" / "H"
    LIMIT 10)
INTERSECT
SELECT "first_name", "last_name" FROM "players"
WHERE "players"."id" IN (
    SELECT "players"."id" FROM "players"
    JOIN "salaries" ON "players"."id" = "salaries"."player_id"
    JOIN "performances" ON "players"."id" = "performances"."player_id"
    AND "performances"."year" = "salaries"."year"
    WHERE "salaries"."year" = '2001' AND "performances"."RBI" != 0
    ORDER BY "salary" / "RBI"
    LIMIT 10)
ORDER BY "last_name";
