INSERT INTO Cards
   (user_id, balance, type, name, benefit_type, multiplier, quarter_mult, quarter_type)
VALUES
   (1, '-123.41', '8500.00', 'credit', 'Chase Freedom', 'quarterly', '0.01', '0.05', 'department'),
   (1, '-2450.12', '8500.00', 'credit', 'Chase Freedom Unlimited', 'flat', '0.015', NULL, NULL),
   (1, '0.00', '7500.00', 'credit', 'United MileagePlus', 'miles', 'quarterly', '0.01', '0.02', 'air')
;

INSERT INTO Transactions
   (user_id, card_id, value, info)
VALUES
   (1, 1, '-15.12', 'SLO Barbeque'),
   (1, 1, '-56.98', 'BEST BUY'),
   (1, 1, '-51.31', 'Nordstrom Online')
;

INSERT INTO Inquiries
   (user_id, text, inq_type, date)
VALUES
   (1, 'ABC COMPANY CO', 'hard', NOW()),
   (1, 'AUTO SHOP INC', 'hard', NOW()),
   (1, 'GOV INC', 'soft', NOW())
;

INSERT INTO Marks

;
