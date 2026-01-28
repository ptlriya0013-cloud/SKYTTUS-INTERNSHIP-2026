--ASSESMENT 8 - Query Optimization 

--Add index to improve search on orders.customer_id
CREATE INDEX idx_orderss_customer_id
ON orderss(customer_id);


-- Use EXPLAIN to analyze query
SET STATISTICS PROFILE ON;

SELECT c.customers_id, c.name, COUNT(o.order_id)
FROM customers c
LEFT JOIN orderss o
ON c.customers_id = o.customer_id
GROUP BY c.customers_id, c.name;

SET STATISTICS PROFILE OFF;


--Optimize a slow join query

--Slow query
SELECT *
FROM customers c
JOIN orderss o
ON c.customers_id = o.customer_id
WHERE o.customer_id = 1;

--Optimized Query
-- Use index + select required columns only
SELECT c.name, o.order_id, o.amount
FROM orderss o
JOIN customers c
ON o.customer_id = c.customers_id
WHERE o.customer_id = 1;



--Explain when index should not be used 

-- Explain when index should not be used
-- Index should not be used when:
-- 1. A large percentage of rows are returned
-- 2. Column has very low cardinality
-- 3. Full table scan is faster than index lookup
-- Example:
-- WHERE order_date BETWEEN '2025-01-01' AND '2025-12-31'

-- Example query where index may not be useful
SELECT *
FROM orderss
WHERE order_date BETWEEN '2025-01-01' AND '2025-12-31';



