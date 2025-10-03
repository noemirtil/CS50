-- SELECT "title" FROM "episodes" WHERE "air_date" LIKE '20__-12-__';
SELECT "title" FROM "episodes" WHERE SUBSTRING("air_date", 6, 2) = '12';