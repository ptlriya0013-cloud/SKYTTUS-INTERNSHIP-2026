--Real world case study

--Customers Table
CREATE TABLE customers (
   customers_id int PRIMARY KEY,
   name varchar(50),
   city varchar(30)
);
 
 INSERT INTO customers (customers_id,name, city) VALUES
 (1, 'Riya', 'Navsari'),
 (2, 'Cheriti', 'Valsad'),
 (3, 'Ayaan', 'Navsari'),
 (4, 'Krish', 'Surat'),
 (5, 'Riya', 'Chikhali');
  
  SELECT * FROM customers;

  -- Products Table
  CREATE TABLE products (
     product_id int PRIMARY KEY,
     product_name varchar(50),
     price int
);

INSERT INTO products (product_id, product_name, price) VALUES
(001, 'laptop', 55000),
(002, 'Mobile', 25000),
(003, 'Tablet', 65000),
(004, 'Headphones', 5000);

SELECT * FROM products;

--ORDER TABLE
CREATE TABLE orderss (
   order_id int PRIMARY KEY,
   customer_id int,
   order_date DATE,
   amount int,
   FOREIGN KEY (customer_id) REFERENCES customers(customers_id)
);

INSERT INTO orderss (order_id, customer_id, order_date, amount) VALUES
(1001, 1, '2025-01-05', 80000),
(1002, 2, '2025-01-10', 25000),
(1003, 1, '2025-02-12', 3000),
(1004, 3, '2025-02-15', 55000),
(1005, 4, '2025-03-01', 1500);
 
 SELECT * FROM orderss;

 --Oredr items table
CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orderss(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO order_items (order_id, product_id, quantity) VALUES 
(1001, 1, 1),
(1001, 2, 1),
(1002, 2, 1),
(1003, 3, 1),
(1004, 1, 1),
(1005, 4, 1);

SELECT * FROM order_items;

--Total oredr per customers
SELECT c.customers_id, c.name, COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orderss o
ON c.customers_id = o.customer_id
GROUP BY c.customers_id, c.name;


--Customer who never placed an order
SELECT c.customers_id, c.name
FROM customers c
LEFT JOIN orderss o
ON c.customers_id = o.customer_id
WHERE o.order_id IS NULL;


--Highest sellling product
SELECT TOP 1 p.product_name, SUM(oi.quantity) AS total_quantity
FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY total_quantity DESC;


--Monthly sales report
SELECT 
    FORMAT(order_date, 'yyyy-MM') AS month,
    SUM(amount) AS total_sales
FROM orderss
GROUP BY FORMAT(order_date, 'yyyy-MM')
ORDER BY month;



--Customers with total purchase > 50000
SELECT 
    c.customers_id,
    c.name,
    SUM(o.amount) AS total_purchase
FROM customers c
JOIN orderss o
ON c.customers_id = o.customer_id
GROUP BY c.customers_id, c.name
HAVING SUM(o.amount) > 50000;


--Top 3 cities with revenue 
SELECT TOP 3
    c.city,
    SUM(o.amount) AS total_revenue
FROM customers c
JOIN orderss o
ON c.customers_id = o.customer_id
GROUP BY c.city
ORDER BY total_revenue DESC;




