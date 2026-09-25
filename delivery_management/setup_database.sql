-- Run this in PostgreSQL to setup the database
-- Connect to PostgreSQL: psql -U postgres

CREATE USER delivery_user WITH PASSWORD 'secure_password';
CREATE DATABASE delivery_db OWNER delivery_user;
GRANT ALL PRIVILEGES ON DATABASE delivery_db TO delivery_user;

-- Enable PostGIS extension
\c delivery_db
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS postgis_topology;

-- Grant permissions
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO delivery_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO delivery_user;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public TO delivery_user;
