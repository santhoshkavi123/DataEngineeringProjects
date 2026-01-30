-- Show all the existing database
SHOW DATABASES;

-- Creating the database gizmobox
CREATE DATABASE gizmobox;


-- Creating refunds table
CREATE TABLE IF NOT EXISTS gizmobox.Refunds (
    refund_id INT PRIMARY KEY, 
    payment_id INT NOT NULL, 
    refund_timestamp DATETIME NOT NULL, 
    refund_amount DECIMAL(10, 2) NOT NULL, 
    refund_reason NVARCHAR(255) NOT NULL
);


-- Inserting the documents into the refunds table 
INSERT INTO gizmobox.Refunds (refund_id, payment_id, refund_timestamp, refund_amount, refund_reason)  
VALUES  
(1, 66, '2025-01-10 11:30:00', 85.75, 'Payment Error:Retailer'),  
(2, 69, '2025-01-03 12:40:15', 120.50, 'Order Cancelled:Customer'),  
(3, 72, '2025-01-06 14:45:30', 65.00, 'Product Returned:Customer'),  
(4, 73, '2025-01-07 16:10:45', 210.99, 'Order Cancelled:Customer'),  
(5, 75, '2025-01-09 18:25:00', 45.20, 'Payment Error:Retailer'),  
(6, 80, '2025-01-10 09:35:20', 130.15, 'Order Cancelled:Customer'),  
(7, 83, '2025-01-12 11:20:40', 150.00, 'Product Returned:Customer'),  
(8, 85, '2025-01-14 13:15:30', 89.99, 'Order Cancelled:Customer'),  
(9, 89, '2025-01-15 15:00:00', 78.50, 'Payment Error:Retailer'),  
(10, 91, '2025-01-17 16:45:15', 250.75, 'Product Returned:Customer');


-- Query the records
SELECT * FROM gizmobox.Refunds;