CREATE TABLE IF NOT EXISTS paises (
    id SERIAL PRIMARY KEY,
    pais VARCHAR(80),
    capital VARCHAR(80),
    habitantes INTEGER
);

INSERT INTO paises (pais, capital, habitantes) VALUES
('Ecuador', 'Quito', 17643060),
('Perú', 'Lima', 33050325),
('Colombia', 'Bogotá', 50882884),
('Chile', 'Santiago', 19107216),
('Argentina', 'Buenos Aires', 45195777),
('México', 'Ciudad de México', 128932753),
('España', 'Madrid', 47351567);
