--
-- File generated with SQLiteStudio v3.2.1 on Ïí Ñåð 10 16:46:40 2020
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: subscriptions
CREATE TABLE subscriptions (
    id        INTEGER PRIMARY KEY,
    user_name STRING,
    status    BOOLEAN NOT NULL
                      DEFAULT (0) 
);

INSERT INTO subscriptions (
                              id,
                              user_name,
                              status
                          )
                          VALUES (
                              1,
                              'sasha_reshetar',
                              1
                          );


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
