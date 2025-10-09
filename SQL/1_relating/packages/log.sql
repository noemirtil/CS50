
-- *** The Lost Letter ***
SELECT * FROM "packages" WHERE "contents" LIKE "%congrat%";
SELECT * FROM "addresses" WHERE "id" = "854";
SELECT * FROM "scans" WHERE "address_id" = '854';
-- *** The Devious Delivery ***
SELECT * FROM "packages" WHERE "from_address_id" IS NULL;
SELECT * FROM "scans" WHERE "package_id" = '5098';
SELECT * FROM "addresses" WHERE "id" IN (50, 348);
-- *** The Forgotten Gift ***
SELECT * FROM "addresses" WHERE "address" LIKE '%109 Tileston Street%';
-- id = 9873
SELECT * FROM "scans" WHERE "address_id" = '9873';
-- Picked 9523, Dropped 9061, 4969, 4568
SELECT * FROM "packages" WHERE "id" = '9523';
-- Flowers to_address_id 4983
SELECT * FROM "addresses" WHERE "id" = '4983';
-- 728 Maple Place
SELECT * FROM "scans" WHERE "package_id" = 9523;
-- picked, dropped at 7432 and picked again by driver_id 17
SELECT * FROM "drivers" WHERE "id" = '17';
-- name Mikel