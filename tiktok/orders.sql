#Company X has a record of its customers and their orders in a database.
Find the customers with the highest order price for orders places
within 10 years of the first order (earliest order_date)
Print customer name and order price
If multiple customers have the same order price, print all of them

There are two tables, customers and orders

customers
id 
name
order_id

orders
id
price
order_date


```sql
SELECT c.name, o.price
FROM customers c
JOIN orders o
ON c.order_id = o.id
WHERE o.order_date >= (SELECT MIN(order_date) FROM orders) - INTERVAL 10 year
AND o.price = (SELECT MAX(price) FROM orders);
```