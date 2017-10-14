CREATE TABLE Cards (
   id           INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
   user_id      INT UNSIGNED,
   balance      DECIMAL(8, 2),
   limit        DECIMAL(8, 2),
   type         ENUM("credit", "debit"),
   name         VARCHAR(32),
   benefit_type ENUM("miles", "flat", "quarterly"),
   multiplier   DOUBLE(4, 4),
   quarter_mult DOUBLE(4, 4),
   quarter_type ENUM("department", "gas", "grocery", "restaurant", "air")
);

CREATE TABLE Transactions (
   id      INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
   user_id INT UNSIGNED,
   card_id INT UNSIGNED REFERENCES Cards(id),
   value   DECIMAL(8, 2),
   info    VARCHAR(128)
);

CREATE TABLE Inquiries (
   id       INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
   user_id  INT UNSIGNED,
   text     VARCHAR(32),
   inq_type ENUM("hard", "soft"),
   date     DATETIME
);

CREATE TABLE Marks (
   id          INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
   received    DATETIME,
   expires     DATETIME,
   description VARCHAR(64)
);

CREATE TABLE Notifications (
   id     INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
   text   VARCHAR(128),
   `date` DATETIME,
   `read` BOOLEAN
);
