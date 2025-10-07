SELECT "name", "per_pupil_expenditure", "exemplary", "proficient" FROM "districts"
JOIN "expenditures" ON "districts"."id" = "expenditures"."district_id"
JOIN "staff_evaluations" ON "districts"."id" = "staff_evaluations"."district_id"
WHERE "name" LIKE '%Harvard%';