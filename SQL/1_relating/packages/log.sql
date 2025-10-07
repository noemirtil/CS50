
-- *** The Lost Letter ***
SELECT * FROM "packages" WHERE "contents" LIKE "%congrat%";
SELECT * FROM "addresses" WHERE "id" = "854";
SELECT * FROM "scans" WHERE "address_id" = '854';
-- *** The Devious Delivery ***
SELECT * FROM "packages" WHERE "from_address_id" IS NULL;
SELECT * FROM "scans" WHERE "package_id" = '5098';
-- *** The Forgotten Gift ***
SELECT * FROM "addresses" WHERE "address" LIKE '%728 Maple Place%';
-- id = 4983
SELECT * FROM "scans" WHERE "address_id" = '4983';
-- picked, package_id = 6269
SELECT * FROM "packages" WHERE "id" = '6269';
-- contents Chalk, to_address_id = 4425;
SELECT * FROM "scans" WHERE "package_id" = '6269';
-- confirms that after three errors, landed to_address_id = 4425;
SELECT * FROM "addresses" WHERE "id" = "4425";
-- 8681 Beacon Street