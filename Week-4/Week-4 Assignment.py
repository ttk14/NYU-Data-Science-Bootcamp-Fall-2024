# TABLE INFO :
# SALES – Date, Order_id, Item_id, Customer_id, Quantity, Revenue
# ITEMS – Item_id, Item_name, price, department
# CUSTOMERS- customer_id, first_name,last_name,Address


# Question 1
SELECT COUNT (DISTINCT Order_id) AS total_orders
FROM SALES
WHERE Date = '2023-03-18';


# Question 2
SELECT COUNT (DISTINCT S.Order_id) AS total_orders
FROM SALES
JOIN CUSTOMERS C ON S.Customer_id = C.Customer_id
WHERE S.Date = '2023-03-18' AND C.first_name = 'John' AND C.last_name = 'Doe';


# Question 3
SELECT COUNT (DISTINCT Customer_id) AS total_customers, AVG (total_spent) AS avg_customer_amount_spent
FROM (
    SELECT Customer_id, SUM (Revenue) AS total_spent
    FROM SALES
    WHERE Date BETWEEN '2023-01-01' AND '2023-01-31'
    GROUP BY Customer_id
) AS customer_spending;


# Question 4
SELECT I.department, SUM (S.Revenue) AS total_revenue
FROM SALES S
JOIN ITEMS I ON S.Item_id = I.Item_id
WHERE S.Date BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY I.department
HAVING total_revenue < 600;


# Question 5
SELECT MAX (Revenue) AS MAX_Revenue, MIN (Revenue) AS Least_Revenue 
FROM SALES;


# Question 6
WITH MaxOrder AS (
  SELECT Order_id, SUM (Revenue) AS Order_Revenue
  FROM SALES
  GROUP BY Order_id
  ORDER BY Order_Revenue DESC
  LIMIT 1
)
SELECT SALES.Order_id, SALES.Item_id, SALES.Quantity, SALES.Revenue
FROM SALES
JOIN MaxOrder ON SALES.Order_id = MaxOrder.Order_id;
