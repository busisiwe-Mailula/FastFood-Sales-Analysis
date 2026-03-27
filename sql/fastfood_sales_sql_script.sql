SELECT * FROM fastfood_db.fastfood_sales;
USE fastfood_db;

-- Analyse data to answer business problem

-- 1. Which menu items generate the most revenue
SELECT
	item_name, sum(revenue) AS total_revenue
FROM fastfood_sales
GROUP BY item_name
ORDER BY total_revenue DESC;

-- 2. Which items sell the most quantity
SELECT
	item_name, sum(quantity) AS total_quantity
FROM fastfood_sales
GROUP BY item_name
ORDER BY total_quantity DESC;

-- 3. Which days generate the most sales
SELECT
	DAYNAME(order_date) AS day_name,
    sum(revenue) AS total_sales
FROM fastfood_sales
GROUP BY order_date
ORDER BY total_sales DESC;

-- 4. which items are underpeforming
SELECT
	item_name,
    SUM(revenue) AS total_revenue,
    SUM(quantity) AS total_quantity
FROM fastfood_sales
GROUP BY item_name
ORDER BY total_revenue;

-- 5. I am just comparing these two items_name since they have the same price to see what led to fanta underperforming, is it demand or the low price?
SELECT
	item_name,
    price,
    SUM(revenue) AS total_revenue,
    SUM(quantity) AS total_quantity
FROM fastfood_sales
WHERE item_name IN('coke','fanta')
GROUP BY item_name, price;
