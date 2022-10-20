SELECT SELLER.FIRST_NAME AS 'seller_first_name',
SELLER.LAST_NAME  AS 'seller_last_name', 
BUYER.FIRST_NAME AS 'buyer_first_name', 
BUYER.LAST_NAME  AS 'buyer_last_name',
O.*,
P.*,
PAY.*
FROM ORDERS O JOIN USERS BUYER ON O.CUSTOMER_ID = BUYER.USER_ID AND BUYER.ROLE_TYPE = 'BUYER'
		      JOIN ORDERDETAILS OD ON O.ORDER_ID = OD.ORDER_ID
			  JOIN PRODUCTS P ON P.PRODUCT_ID = OD.PRODUCT_ID
              JOIN PAYMENTS PAY ON O.PAYMENT_ID = PAY.PAYMENT_ID
			  JOIN USERS SELLER ON (SELLER.USER_ID = P.SELLER_ID AND SELLER.ROLE_TYPE = 'SELLER');

SELECT BUYER.FIRST_NAME AS 'buyer_first_name', 
BUYER.LAST_NAME  AS 'buyer_last_name',
O.SUB_TOTAL, O.TAXES, O.SHIPPING, O.GRAND_TOTAL, O.ORDER_DATE,
P.PRODUCT_ID, P.PRODUCT_NAME,P.PRICE_PER_UNIT, P.PRODUCT_DESCRIPTION,
OD.PRODUCT_QUANTITY
FROM ORDERS O JOIN USERS BUYER ON O.CUSTOMER_ID = BUYER.USER_ID AND BUYER.ROLE_TYPE = 'BUYER'
			  JOIN ORDERDETAILS OD ON O.ORDER_ID = OD.ORDER_ID
			  JOIN PRODUCTS P ON P.PRODUCT_ID = OD.PRODUCT_ID
WHERE USER_ID = 1;

SELECT P.PRODUCT_NAME, P.PRICE_PER_UNIT
FROM PRODUCTS P;

SELECT O.CUSTOMER_ID, O.ORDER_ID,
OD.PRODUCT_ID, OD.PRODUCT_QUANTITY,
P.PRODUCT_NAME, P.PRICE_PER_UNIT, P.PRODUCT_DESCRIPTION
FROM ORDERS O JOIN USERS ON O.CUSTOMER_ID = USERS.USER_ID
			  JOIN ORDERDETAILS OD ON O.ORDER_ID = OD.ORDER_ID
              JOIN PRODUCTS P ON P.PRODUCT_ID = OD.PRODUCT_ID
WHERE CUSTOMER_ID = 3 AND OD.ORDER_ID = 202;

SELECT O.CUSTOMER_ID, O.ORDER_ID,
OD.PRODUCT_ID, OD.PRODUCT_QUANTITY,
P.PRODUCT_NAME, P.PRICE_PER_UNIT, P.PRODUCT_DESCRIPTION
FROM ORDERS O JOIN USERS ON O.CUSTOMER_ID = USERS.USER_ID
			  JOIN ORDERDETAILS OD ON O.ORDER_ID = OD.ORDER_ID
              JOIN PRODUCTS P ON P.PRODUCT_ID = OD.PRODUCT_ID
WHERE CUSTOMER_ID = 3 AND OD.ORDER_ID = 202;

SELECT O.SUB_TOTAL, O.TAXES, O.SHIPPING, O.GRAND_TOTAL
FROM ORDERS O
WHERE O.CUSTOMER_ID = 1 AND O.ORDER_ID = 201;

SELECT O.CUSTOMER_ID, O.ORDER_ID,
OD.PRODUCT_ID, OD.PRODUCT_QUANTITY,
P.PRODUCT_NAME, P.PRICE_PER_UNIT, P.PRODUCT_DESCRIPTION
FROM ORDERS O JOIN USERS ON O.CUSTOMER_ID = USERS.USER_ID
			  JOIN ORDERDETAILS OD ON O.ORDER_ID = OD.ORDER_ID
              JOIN PRODUCTS P ON P.PRODUCT_ID = OD.PRODUCT_ID
WHERE CUSTOMER_ID = 3 AND OD.ORDER_ID = 200;
SELECT role_type FROM users WHERE user_id = 1;
SELECT user_id, role_type 
FROM users WHERE user_id = 3;

SELECT SUM(PRODUCT_QUANTITY)
FROM ORDERDETAILS WHERE ORDER_ID = 200;

SELECT SUM(PRODUCT_QUANTITY)
FROM ORDERDETAILS WHERE ORDER_ID = 204;

SELECT *
FROM USERS;

SELECT *
FROM ORDERS;

SELECT *
FROM PRODUCTS;

SELECT *
FROM ORDERDETAILS;


SELECT *
FROM PAYMENTS;

-- INSERT INTO products(product_name,product_description,product_instructions,product_qauntity,price_per_unit,product_img) VALUES("Airpods", "for listening to music", "charge, hookup with bluetooth, use", "5", "200","wdgrewdwdwefrergefde");

-- INSERT INTO `group6project`.`USERS` (`first_name`, `last_name`, `email`, `password`, `role_type`, `created_at`) VALUES ('Elle', 'Woods', 'elle@yahoo.com', 'ilikebruce', 'seller', NOW());
-- INSERT INTO `group6project`.`USERS` (`first_name`, `last_name`, `email`, `password`, `role_type`, `created_at`) VALUES ('Billy', 'Brooks', 'billy@yahoo.com', 'ilikechicago', 'buyer', NOW());

-- INSERT INTO `group6project`.`PRODUCTS` (`product_name`, `price_per_unit`, `product_description`, `product_instructions`, `product_quantity`, `product_img`, `created_at`, `seller_id`) VALUES ('computer', '900.00', 'to help you with your work', 'charge computer for 2 hrs and then it\'s good to go for 18 hrs', '10', 'https://cdn.britannica.com/77/170477-050-1C747EE3/Laptop-computer.jpg?w=400&h=300&c=crop', NOW(), '1');
-- INSERT INTO `group6project`.`PRODUCTS` (`product_name`, `price_per_unit`, `product_description`, `product_instructions`, `product_quantity`, `product_img`, `created_at`, `seller_id`) VALUES ('keyboard', '150.00', 'to help you with typing', 'charge for 2 hours lasts for 20hrs', '15', 'https://cdn.britannica.com/80/27080-004-3D09DDD7/Compaq-Computer-Corporation-portable-computer-IBM-weight-November-1982.jpg?w=315', NOW(), '1');
-- INSERT INTO `group6project`.`PRODUCTS` (`product_name`, `price_per_unit`, `product_description`, `product_instructions`, `product_quantity`, `product_img`, `created_at`, `seller_id`) VALUES ('mouse', '25.00', 'help use a computer', 'sadfasfdasfasdf', '20', 'https://cdn.britannica.com/64/74064-004-1192BCB2/mouse-personal-computer.jpg?w=315', NOW(), '1');



ALTER TABLE PRODUCTS
RENAME COLUMN product_qauntity TO product_quantity;



-- INSERT INTO `group6project`.`ORDERS` (`order_id`, `address`, `order_date`, `customer_id`, `payment_id`) VALUES (202, 'adsfasdfa', NOW(), 3, 1);
-- INSERT INTO `group6project`.`ORDERS` (`order_id`, `address`, `order_date`, `customer_id`, `payment_id`) VALUES (203, 'adsfasdfa', NOW(), 1, 2);

-- INSERT INTO ORDERDETAILS (`order_id`,  `product_id`, `product_quantity`) VALUES (202, 502, 2);
-- INSERT INTO ORDERDETAILS (`order_id`, `product_id`,`product_quantity`) VALUES (202, 500, 1);
-- INSERT INTO ORDERDETAILS (`order_id`,`product_id`,`product_quantity`) VALUES (202, 501, 2);
-- INSERT INTO ORDERDETAILS (`order_id`, `product_id`,`product_quantity`) VALUES (203,501, 2);
-- INSERT INTO ORDERDETAILS (`order_id`,`product_id`,`product_quantity`) VALUES (203, 502,1);

