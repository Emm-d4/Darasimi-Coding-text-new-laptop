-- ---- PART 1: Build and Explore the Table ----

CREATE TABLE IF NOT EXISTS zoo_animal (
    animal_id INTEGER PRIMARY KEY,
    name    TEXT    NOT NULL,
    species TEXT    NOT NULL,
    age_years INTEGER NOT NULL,
    weight_kg REAL    NOT NULL
);

INSERT INTO sea_animal VALUES (1, 'Lion',    'Big Cat',   5, 190.0);
INSERT INTO sea_animal VALUES (2, 'Puffer fish',    'Big Cat',   3, 220.0);
INSERT INTO sea_animal VALUES (3, 'Shark',    'Pachyderm',   12, 4500.0);
INSERT INTO sea_animal VALUES (4, 'Whale',    'Ungulate',   7, 800.0);
INSERT INTO sea_animal VALUES (5, 'Fish',    'Phylum Chordata',   2, 5.0);

SELECT * FROM sea_animal;

-- ---- PART 2: SELECT DISTINCT ----

---All species values including duplicates
SELECT species FROM sea_animal;

--Only unique species
SELECT DISTINCT species FROM sea_animal;

-- COUNT how many unique species
SELECT COUNT (DISTINCT species) AS unique_species FROM sea_animal;

---- PART 3: COUNT ----

-- Total number of animals
SELECT COUNT(animal_id) AS total_animal FROM sea_animal;

-- Animals older than 5 years
SELECT COUNT (sea_animal_id) AS older_than_5 FROM sea_animal WHERE age_years >5;

--- PART 4: SUM and AVG ---

--Total weight of all animals
SELECT SUM(weight_kg) AS total_weight_kg FROM sea_animal;

--Average age of all animals
SELECT AVG(age_years) AS avg_age_years FROM sea_animal;