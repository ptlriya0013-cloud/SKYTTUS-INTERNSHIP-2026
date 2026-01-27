-- ASSESSMENT-5 Constraints and Schema design 
/* Create users table with
  
  primary key
  uniuq email
  not null password
  add foreihn key between users and orders
  create index on email column
  create view to display user order summary

  */

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100) UNIQUE,   -- unique email
    password VARCHAR(50) NOT NULL  -- password cannot be NULL
);

INSERT INTO users VALUES
(1, 'Riya', 'riya@gmail.com', 'riya@123'),
(2, 'Amit', 'amit@gmail.com', 'amit@123'),
(3, 'Cheriti', 'chery@gmail.com', 'cheri@123'),
(4, 'Tirth', 'tirth@gmail.com', 'tirth@123');


-- Add foreign key constraint
ALTER TABLE orders
ADD CONSTRAINT fk_user
FOREIGN KEY (user_id)
REFERENCES users(user_id);


-- Create orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    order_amount INT,
    order_date DATE
);

 -- Insert orders data
INSERT INTO orders  VALUES
(101, 1, 5000, '2025-01-10'),
(102, 1, 3000, '2025-01-15'),
(103, 2, 7000, '2025-01-20'),
(104, 3, 4000, '2025-01-25'),
(105, 4, 6000, '2025-01-28');

select * from users;
select * from orders;

 -- Create index on email column
CREATE INDEX idx_users_email
ON users(email);


-- Create view for user order summary
CREATE VIEW user_order_summary AS
SELECT 
    u.user_id,
    u.name,
    u.email,
    COUNT(o.order_id) AS total_orders,
    SUM(o.order_amount) AS total_amount
FROM users u
LEFT JOIN orders o
ON u.user_id = o.user_id
GROUP BY u.user_id, u.name, u.email;

SELECT * FROM user_order_summary;
