CREATE TABLE IF NOT EXISTS COMPUTERS(
    PRO_ID TEXT PRIMARY KEY,
    PRO_NAME TEXT,
    PRO_PRICE INTEGER,
    PRO_COM TEXT
);

INSERT INTO COMPUTERS(PRO_ID, PRO_NAME, PRO_PRICE, PRO_COM) VALUES
    ("101","Levono",2700,"15"),
    ("102","Dell",350,"16"),
    ("103","Hp",500,"14"),
    ("104","asus",750,"16"),
    ("105", "apple", 5000, "11"),
    ("106", "acer",4500, "12"),
    ("107","Microsoft",700,"12"),
    ("108","samsung",2500,"13");

-- displaying data with minimum price
SELECT PRO_NAME, PRO_PRICE FROM COMPUTERS WHERE PRO_PRICE = (SELECT MIN(PRO_PRICE) FROM PRODUCT);

-- displaying data with maximum price
select PRO_NAME, PRO_PRICE FROM COMPUTERS WHERE PRO_PRICE = (SELECT MAX(PRO_PRICE) FROM PRODUCT);