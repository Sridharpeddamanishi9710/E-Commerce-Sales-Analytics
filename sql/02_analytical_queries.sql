-- =========================================================================
-- E-Commerce Sales & Customer Insights Analytics - Analytical Queries
-- =========================================================================

-- 1. Monthly Sales & Revenue Trend
SELECT 
    STRFTIME('%Y-%m', o.OrderDate) AS SalesMonth,
    COUNT(DISTINCT o.OrderID) AS TotalOrders,
    ROUND(SUM(oi.LineTotal), 2) AS TotalRevenue,
    ROUND(SUM(oi.LineProfit), 2) AS TotalProfit
FROM orders o
JOIN order_items oi ON o.OrderID = oi.OrderID
GROUP BY SalesMonth
ORDER BY SalesMonth;

-- 2. Revenue & Profit by Product Category
SELECT 
    p.Category,
    SUM(oi.Quantity) AS UnitsSold,
    ROUND(SUM(oi.LineTotal), 2) AS CategoryRevenue,
    ROUND(SUM(oi.LineProfit), 2) AS CategoryProfit
FROM order_items oi
JOIN products p ON oi.ProductID = p.ProductID
GROUP BY p.Category
ORDER BY CategoryRevenue DESC;

-- 3. Top 5 Best-Selling Products
SELECT 
    p.ProductName,
    p.Category,
    SUM(oi.Quantity) AS TotalQuantitySold,
    ROUND(SUM(oi.LineTotal), 2) AS TotalRevenue
FROM order_items oi
JOIN products p ON oi.ProductID = p.ProductID
GROUP BY p.ProductID, p.ProductName, p.Category
ORDER BY TotalQuantitySold DESC
LIMIT 5;

-- 4. Top 5 High-Value Customers
SELECT 
    c.CustomerID,
    c.CustomerName,
    r.RegionName,
    COUNT(DISTINCT o.OrderID) AS OrderCount,
    ROUND(SUM(oi.LineTotal), 2) AS TotalSpent
FROM customers c
JOIN regions r ON c.RegionID = r.RegionID
JOIN orders o ON c.CustomerID = o.CustomerID
JOIN order_items oi ON o.OrderID = oi.OrderID
GROUP BY c.CustomerID, c.CustomerName, r.RegionName
ORDER BY TotalSpent DESC
LIMIT 5;

-- 5. Regional Performance Analysis
SELECT 
    r.RegionName,
    COUNT(DISTINCT o.OrderID) AS TotalOrders,
    ROUND(SUM(oi.LineTotal), 2) AS RegionalRevenue,
    ROUND(AVG(oi.LineTotal), 2) AS AverageOrderValue
FROM regions r
JOIN customers c ON r.RegionID = c.RegionID
JOIN orders o ON c.CustomerID = o.CustomerID
JOIN order_items oi ON o.OrderID = oi.OrderID
GROUP BY r.RegionName
ORDER BY RegionalRevenue DESC;


-- 6. Order Status Analysis
SELECT
    o.OrderStatus,
    COUNT(DISTINCT o.OrderID) AS TotalOrders
FROM orders o
GROUP BY o.OrderStatus
ORDER BY TotalOrders DESC;


-- 7. Payment Method Analysis
SELECT
    o.PaymentMethod,
    COUNT(DISTINCT o.OrderID) AS TotalOrders,
    ROUND(SUM(oi.LineTotal), 2) AS TotalRevenue
FROM orders o
JOIN order_items oi ON o.OrderID = oi.OrderID
GROUP BY o.PaymentMethod
ORDER BY TotalOrders DESC;


-- 8. Delivery Time Analysis
SELECT
    o.OrderStatus,
    ROUND(AVG(o.DeliveryDays), 2) AS AverageDeliveryDays,
    COUNT(DISTINCT o.OrderID) AS TotalOrders
FROM orders o
GROUP BY o.OrderStatus
ORDER BY o.OrderStatus;


-- 9. Discount and Profitability Analysis
SELECT
    oi.Discount,
    COUNT(*) AS OrderItemCount,
    ROUND(SUM(oi.LineTotal), 2) AS TotalRevenue,
    ROUND(SUM(oi.LineProfit), 2) AS TotalProfit,
    ROUND(
        100.0 * SUM(oi.LineProfit) / NULLIF(SUM(oi.LineTotal), 0),
        2
    ) AS ProfitMarginPercent
FROM order_items oi
GROUP BY oi.Discount
ORDER BY oi.Discount;
