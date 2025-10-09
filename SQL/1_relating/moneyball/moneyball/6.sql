SELECT SUM("H") AS 'total hits', "name"  FROM "performances"
JOIN "teams" ON "teams"."id" = "performances"."team_id"
WHERE "performances"."year" = '2001'
GROUP BY "team_id"
ORDER BY SUM("H") DESC
LIMIT 5;
