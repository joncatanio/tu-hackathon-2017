INSERT INTO Cards
   (user_id, balance, credit_limit, `type`, name, benefit_type, multiplier, quarter_mult, quarter_type)
VALUES
   (1, '123.41', '8500.00', 'credit', 'Chase Freedom', 'quarterly', '0.01', '0.05', 'department'),
   (1, '2450.12', '8500.00', 'credit', 'Chase Freedom Unlimited', 'flat', '0.015', NULL, NULL),
   (1, '0.00', '7500.00', 'credit', 'United MileagePlus', 'miles', '0.01', '0.02', 'air')
;

INSERT INTO Transactions
   (user_id, card_id, amount, merchant, timestamp)
VALUES
   (1, 1, '15.12', 'SLO Barbeque', NOW()),
   (1, 1, '56.98', 'BEST BUY', NOW()),
   (1, 1, '51.31', 'Nordstrom Online', NOW()),
   (1, 2, '1023.12', 'Big O Tires', NOW()),
   (1, 2, '89.15', 'KIA SERVICE CENTER', NOW()),
   (1, 2, '122.31', 'Fancy Steakhouse', NOW()),
   (1, 2, '1215.54', 'Newegg.com', NOW())
;

INSERT INTO Inquiries
   (user_id, text, inq_type, date)
VALUES
   (1, 'ABC COMPANY CO', 'hard', NOW()),
   (1, 'AUTO SHOP INC', 'hard', NOW()),
   (1, 'GOV INC', 'soft', NOW())
;

INSERT INTO Marks
   (received, expires, description)
VALUES
   (NOW(), DATE_ADD(NOW(), INTERVAL 7 YEAR), 'Missed Payment')
;

INSERT INTO Merchants
   (name, base_url, merchant_type)
VALUES
   ('Nordstrom', 'https://secure.nordstrom.com/', 'department'),
   ('Macy\'s', 'https://www.macys.com/chkout/', 'department'),
   ('Amazon', 'https://www.amazon.com/gp/buy/payselect/handlers/', 'department'),
   ('Lululemon', 'https://shop.lululemon.com/checkout/spk/', 'department'),
   ('Walmart', 'https://www.walmart.com/checkout/#/', 'department'),
   ('Barnes and Noble', 'https://www.barnesandnoble.com/checkout/', 'misc'),
   ('Home Depot', 'https://secure2.homedepot.com/mycheckout/checkout#/', 'misc')
;
