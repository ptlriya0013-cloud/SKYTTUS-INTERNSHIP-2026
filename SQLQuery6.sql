--ASSESSMENT 6  Transactions and Safety
CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    account_name VARCHAR(50),
    balance INT
);


INSERT INTO accounts(account_id, account_name, balance) VALUES
(001, 'Riya Patel', 25000),
(002, 'Cheriti Patel', 27000),
(003, 'Ayaan Patel', 20000);

SELECT * FROM accounts;



--Start a Transaction 
BEGIN Transaction;

--Insert records into accounts 
INSERT INTO accounts (account_id, account_name, balance)
VALUES (004, 'Riddhi Jogani', 15000);



--Rollback changes
ROLLBACK;


--Demonstrate transfer of money using transactions
--Commit valid transactions
BEGIN TRANSACTION;

UPDATE accounts
SET balance = balance - 2000
WHERE account_id = 1;

UPDATE accounts
SET balance = balance + 2000
WHERE account_id = 2;

COMMIT;

select * from accounts;

