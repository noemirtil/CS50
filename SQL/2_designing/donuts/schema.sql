-- Deletes prior tables if they exist
DROP TABLE IF EXISTS "ingredients";

-- Creates tables
CREATE TABLE "ingredients" (
    "id" INTEGER,
    "name" TEXT UNIQUE NOT NULL,
    "unit_price" INTEGER NOT NULL,
    PRIMARY KEY("id")
)

CREATE TABLE "donuts" (
    "id" INTEGER,
    "name" TEXT UNIQUE NOT NULL,
    "gluten_free" INTEGER NOT NULL CHECK("gluten-free" = 0 OR 1),
    "unit_price" INTEGER NOT NULL,
    PRIMARY KEY("id")
)

CREATE TABLE "orders" (
    "id" INTEGER,
    "donut_id" INTEGER NOT NULL,
    "quantity" INTEGER NOT NULL CHECK("quantity" > 0),
    "customer_id" INTEGER NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY("donut_id") REFERENCES "donuts"("id")
    FOREIGN KEY("customer_id") REFERENCES "customers"("id")
)

CREATE TABLE "customers" (
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    -- "order_id" INTEGER NOT NULL,
    PRIMARY KEY("id"),
    -- FOREIGN KEY("order_id") REFERENCES "orders"("id")
)

-- Junction tables:
CREATE TABLE "ingredients_list" (
    "ingredient_id" INTEGER,
    "donut_id" INTEGER
    FOREIGN KEY("ingredient_id") REFERENCES "ingredients"("id")
    FOREIGN KEY("donut_id") REFERENCES "donuts"("id")
)

CREATE TABLE "orders_history" (
    "user_id" INTEGER,
    "order_id" INTEGER,
    FOREIGN KEY("order_id") REFERENCES "orders"("id")
    FOREIGN KEY("us er_id") REFERENCES "users"("id")
);