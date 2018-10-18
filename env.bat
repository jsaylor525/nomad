REM These settings are required for create.py to work, the PG variables
REM are needed in windows. If they don't exist we can't create the db via python
SET DATABASE_URL=postgres://localhost/lecture4
SET PGUSER=jsaylor
SET PGPASSWORD=password
SET FLASK_APP=application.py