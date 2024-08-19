sql_query = """```sql
SELECT p.product_id, p.product_name, SUM(st.quantity * p.product_price) AS total_revenue
FROM products p
JOIN sales_transaction st ON p.product_id = st.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_revenue DESC
LIMIT 1;
```"""
sql_query.strip("` \n")



