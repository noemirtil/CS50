-- Deletes prior tables if they exist
DROP TABLE IF EXISTS "users";
DROP TABLE IF EXISTS "schools";
DROP TABLE IF EXISTS "companies";
DROP TABLE IF EXISTS "people_connections";
DROP TABLE IF EXISTS "school_connections";
DROP TABLE IF EXISTS "company_connections";

CREATE TABLE "users" (
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "username" TEXT NOT NULL UNIQUE,
    "password" TEXT NOT NULL,
    "people1" INTEGER,
    "school1" INTEGER,
    "company1" INTEGER,
    PRIMARY KEY("id"),
    FOREIGN KEY("people1") REFERENCES "people_connections"("id"),
    FOREIGN KEY("school1") REFERENCES "school_connections"("id"),
    FOREIGN KEY("company1") REFERENCES "company_connections"("id")
);

CREATE TABLE "schools" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "type" TEXT NOT NULL,
    "location" TEXT NOT NULL,
    "year" INT NOT NULL CHECK("year" BETWEEN 1000 AND 3000),
    PRIMARY KEY("id")
);

CREATE TABLE "companies" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "industry" TEXT NOT NULL,
    "location" TEXT NOT NULL,
    PRIMARY KEY("id")
);

-- --------------------------------- Junction tables:
CREATE TABLE "people_connections" (
    "user_a" INTEGER,
    "user_b" INTEGER,
    FOREIGN KEY("user_a") REFERENCES "users"("id"),
    FOREIGN KEY("user_b") REFERENCES "users"("id")
);

CREATE TABLE "school_connections" (
    "school_id" INTEGER,
    "alumni" INTEGER,
    "start" NUMERIC NOT NULL,
    "end" NUMERIC,
    "degree" TEXT NOT NULL,
    FOREIGN KEY("school_id") REFERENCES "schools"("id"),
    FOREIGN KEY("alumni") REFERENCES "users"("id")
);

CREATE TABLE "company_connections" (
    "company_id" INTEGER,
    "employee" INTEGER,
    "start" NUMERIC NOT NULL,
    "end" NUMERIC,
    "title" TEXT NOT NULL,
    FOREIGN KEY("company_id") REFERENCES "companies"("id"),
    FOREIGN KEY("employee") REFERENCES "users"("id")
);