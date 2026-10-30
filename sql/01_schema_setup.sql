-- =========================================================================
-- E-Commerce Sales & Customer Insights Analytics - Schema Setup Script
-- Database: ECommerceAnalytics
-- =========================================================================

-- Drop tables if they already exist (to allow clean re-runs)
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS regions;

-- 1. Regions Table
CREATE TABLE regions (
    RegionID VARCHAR(10) PRIMARY KEY,
    RegionName VARCHAR(50) NOT NULL,
    Country VARCHAR(50) NOT NULL
);

-- 2. Customers Table
CREATE TABLE customers (
    CustomerID VARCHAR(20) PRIMARY KEY,
    CustomerName VARCHAR(100) NOT NULL,
    Email VARCHAR(100),
    JoinDate DATE,
    RegionID VARCHAR(10),
    Age INT,
    Gender VARCHAR(20),
    AgeGroup VARCHAR(20),
    FOREIGN KEY (RegionID) REFERENCES regions(RegionID)
);

-- 3. Products Table
CREATE TABLE products (
    ProductID VARCHAR(20) PRIMARY KEY,
    ProductName VARCHAR(100) NOT NULL,
    Category VARCHAR(50) NOT NULL,
    SubCategory VARCHAR(50) NOT NULL,
    UnitPrice DECIMAL(10, 2) NOT NULL,
    CostPrice DECIMAL(10, 2) NOT NULL
);

-- 4. Orders Table
CREATE TABLE orders (
    OrderID VARCHAR(30) PRIMARY KEY,
    CustomerID VARCHAR(20),
    OrderDate DATE NOT NULL,
    ShipDate DATE,
    OrderStatus VARCHAR(30),
    PaymentMethod VARCHAR(30),
    DeliveryDays INT,
    FOREIGN KEY (CustomerID) REFERENCES customers(CustomerID)
);

-- 5. Order Items Table
CREATE TABLE order_items (
    OrderItemID VARCHAR(30) PRIMARY KEY,
    OrderID VARCHAR(30),
    ProductID VARCHAR(20),
    Quantity INT NOT NULL,
    Discount DECIMAL(5, 2) DEFAULT 0.00,
    LineTotal DECIMAL(10, 2) NOT NULL,
    LineProfit DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (OrderID) REFERENCES orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES products(ProductID)
);

-- Verification: Display structure status
-- (Run these after data import to verify row counts)
-- SELECT COUNT(*) FROM regions;
-- SELECT COUNT(*) FROM customers;
-- SELECT COUNT(*) FROM products;
-- SELECT COUNT(*) FROM orders;
-- SELECT COUNT(*) FROM order_items;