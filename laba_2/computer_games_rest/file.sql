BEGIN;
--
-- Create model ComputerGame
--
CREATE TABLE "catalog_computergame" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "genre" varchar(50) NOT NULL, "setting" varchar(50) NOT NULL, "date" date NOT NULL);
--
-- Create model Platform
--
CREATE TABLE "catalog_platform" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "date" date NOT NULL);
CREATE TABLE "catalog_platform_game" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "platform_id" integer NOT NULL REFERENCES "catalog_platform" ("id") DEFERRABLE INITIALLY DEFERRED, "computergame_id" integer NOT NULL REFERENCES "catalog_computergame" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Engine
--
CREATE TABLE "catalog_engine" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "language" varchar(50) NOT NULL, "date" date NOT NULL, "game_id" integer NULL REFERENCES "catalog_computergame" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Company
--
CREATE TABLE "catalog_company" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "place" varchar(50) NOT NULL, "date" date NOT NULL, "engine_id" integer NULL REFERENCES "catalog_engine" ("id") DEFERRABLE INITIALLY DEFERRED, "game_id" integer NULL REFERENCES "catalog_computergame" ("id") DEFERRABLE INITIALLY DEFERRED, "platform_id" integer NULL REFERENCES "catalog_platform" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "catalog_platform_game_platform_id_computergame_id_3bc988e8_uniq" ON "catalog_platform_game" ("platform_id", "computergame_id");
CREATE INDEX "catalog_platform_game_platform_id_74a03eac" ON "catalog_platform_game" ("platform_id");
CREATE INDEX "catalog_platform_game_computergame_id_a46686f9" ON "catalog_platform_game" ("computergame_id");
CREATE INDEX "catalog_engine_game_id_135ea498" ON "catalog_engine" ("game_id");
CREATE INDEX "catalog_company_engine_id_034fc991" ON "catalog_company" ("engine_id");
CREATE INDEX "catalog_company_game_id_c6d500b1" ON "catalog_company" ("game_id");
CREATE INDEX "catalog_company_platform_id_c65349f7" ON "catalog_company" ("platform_id");
COMMIT;
