-- DROP TABLE IF EXISTS Entries;
-- DROP TABLE IF EXISTS Habits;
-- DROP TABLE IF EXISTS Dificulty;
-- DROP TABLE IF EXISTS Weigth;

-- CREATE TABLE Habits (
    -- HAB_ID INTEGER PRIMARY KEY AUTOINCREMENT,
	-- HAB_fk_dificulty INTEGER NOT NULL,	 
    -- HAB_fk_weight	INTEGER NOT NULL,
    -- HAB_name  TEXT,
    -- HAB_active	BOOLEAN ,
    -- HAB_daysPerWeek INTEGER 
-- );

-- CREATE TABLE Dificulty (
	-- DIF_ID INTEGER PRIMARY KEY AUTOINCREMENT,
	-- DIF_name TEXT,
	-- DIF_value FLOAT
-- );
	
-- create table Weigth(
	-- WEI_ID INTEGER PRIMARY KEY AUTOINCREMENT,
	-- WEI_name TEXT,
	-- WEI_value FLOAT
-- );

-- CREATE TABLE Entries (
    -- ENTRY_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    -- ENTRY_fk_habits INTEGER NOT NULL,
	-- ENTRY_fk_grade INTEGER NOT NULL,
    -- ENTRY_date DATE NOT NULL
-- );