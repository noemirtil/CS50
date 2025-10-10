-- Deletes prior tables if they exist
DROP TABLE IF EXISTS "ingredients";
DROP TABLE IF EXISTS "donuts";
DROP TABLE IF EXISTS "orders";
DROP TABLE IF EXISTS "customers";
DROP TABLE IF EXISTS "ingredients_list";
DROP TABLE IF EXISTS "orders_history";
DROP TABLE IF EXISTS "sub_orders";

-- Creates tables
CREATE TABLE "ingredients" (
    "id" INTEGER,
    "name" TEXT UNIQUE NOT NULL,
    "unit_price" INTEGER NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "donuts" (
    "id" INTEGER,
    "name" TEXT UNIQUE NOT NULL,
    "gluten_free" INTEGER NOT NULL CHECK("gluten-free" = 0 OR 1),
    "unit_price" INTEGER NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "orders" (
    "id" INTEGER,
    "customer_id" INTEGER NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY("customer_id") REFERENCES "customers"("id")
);

CREATE TABLE "customers" (
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    PRIMARY KEY("id")
);

-- Junction tables:
CREATE TABLE "ingredients_list" (
    "ingredient_id" INTEGER,
    "donut_id" INTEGER,
    FOREIGN KEY("ingredient_id") REFERENCES "ingredients"("id"),
    FOREIGN KEY("donut_id") REFERENCES "donuts"("id")
);

CREATE TABLE "orders_history" (
    "user_id" INTEGER,
    "order_id" INTEGER,
    FOREIGN KEY("order_id") REFERENCES "orders"("id"),
    FOREIGN KEY("user_id") REFERENCES "users"("id")
);

CREATE TABLE "sub_orders" (
    "order_id" INTEGER,
    "donut_id" INTEGER,
    "quantity" INTEGER NOT NULL CHECK("quantity" > 0),
    FOREIGN KEY("order_id") REFERENCES "orders"("id"),
    FOREIGN KEY("donut_id") REFERENCES "donuts"("id")
);