CREATE TABLE Cards (
   id           INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
   user_id      INT UNSIGNED,
   balance      DECIMAL(8, 2),
   credit_limit DECIMAL(8, 2),
   type         ENUM("credit", "debit"),
   name         VARCHAR(32),
   benefit_type ENUM("miles", "flat", "quarterly"),
   multiplier   DOUBLE(4, 4),
   quarter_mult DOUBLE(4, 4),
   quarter_type ENUM("department", "gas", "grocery", "restaurant", "air", "misc")
);

CREATE TABLE Transactions (
   id        INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
   user_id   INT UNSIGNED,
   card_id   INT UNSIGNED REFERENCES Cards(id),
   amount    DECIMAL(8, 2),
   merchant  VARCHAR(128),
   timestamp DATETIME
);

CREATE TABLE Inqueries (
   id       INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
   user_id  INT UNSIGNED,
   text     VARCHAR(32),
   inq_type ENUM("hard", "soft"),
   date     DATETIME
);

CREATE TABLE Marks (
   id          INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
   user_id     INT UNSIGNED,
   received    DATETIME,
   expires     DATETIME,
   description VARCHAR(64)
);

CREATE TABLE Merchants (
   id            INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
   name          VARCHAR(32),
   base_url      VARCHAR(64),
   merchant_type ENUM("department", "gas", "grocery", "restaurant", "air", "misc")
);

CREATE TABLE Notifications (
   id INT    UNSIGNED PRIMARY KEY AUTO_INCREMENT,
   user_id   INT UNSIGNED,
   text      VARCHAR(64),
   timestamp DATETIME,
   has_read  BOOLEAN
);
