-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2015-08-16 05:17:20.113




-- tables
-- Table: CLIENT
CREATE TABLE CLIENT (
    id_cl int  NOT NULL,
    full_name varchar(255)  NOT NULL,
    email varchar(255)  NOT NULL,
    CONSTRAINT CLIENT_pk PRIMARY KEY  (id_cl)
)
;





-- Table: "TRANSACTION"
CREATE TABLE "TRANSACTION" (
    id_tr int  NOT NULL,
    CLIENT_id_cl int  NOT NULL,
    profit_loss decimal(38,17)  NOT NULL,
    date datetime  NOT NULL,
    time int  NOT NULL,
    amount decimal(38,17)  NOT NULL,
    changed decimal(38,17)  NOT NULL,
    currency_pair varchar(7)  NOT NULL,
    CONSTRAINT TRANSACTION_pk PRIMARY KEY  (id_tr)
)
;









-- foreign keys
-- Reference:  TRANSACTION_CLIENT (table: "TRANSACTION")


ALTER TABLE "TRANSACTION" ADD CONSTRAINT TRANSACTION_CLIENT 
    FOREIGN KEY (CLIENT_id_cl)
    REFERENCES CLIENT (id_cl)
;





-- End of file.

