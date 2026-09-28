-- Drop existing database if exists
DROP DATABASE IF EXISTS geologix_db;

-- Create new database
CREATE DATABASE geologix_db 
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.UTF-8'
    LC_CTYPE = 'en_US.UTF-8'
    TEMPLATE = template0;

-- Create user if not exists
DO
\\$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_catalog.pg_roles WHERE rolname = 'geologix_user'
   ) THEN
      CREATE USER geologix_user WITH PASSWORD 'geologix123';
   END IF;
END
\\$;

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE geologix_db TO geologix_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO geologix_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO geologix_user;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public TO geologix_user;

-- Create PostGIS extension for spatial data
\c geologix_db
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS postgis_topology;
