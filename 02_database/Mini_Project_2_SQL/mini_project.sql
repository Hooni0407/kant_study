DROP DATABASE IF EXISTS shop;

CREATE DATABASE shop;
\c shop

CREATE TABLE category
(
    category_id     SERIAL          PRIMARY KEY,
    category_name   VARCHAR(50)     NOT NULL UNIQUE,
    description     TEXT
);

CREATE TABLE product
(
    product_id      SERIAL          PRIMARY KEY,
    product_name    VARCHAR(100)    NOT NULL,
    price           INT             NOT NULL CHECK (price >= 0),
    stock           INT             NOT NULL DEFAULT 0 CHECK (stock >= 0),
    category_id     INT             REFERENCES category(category_id),
    description     TEXT
);

CREATE TABLE cart
(
    cart_id         SERIAL          PRIMARY KEY,
    user_id         INT             NOT NULL REFERENCES users(user_id),
    product_id      INT             NOT NULL REFERENCES product(product_id),
    quantity        INT             NOT NULL DEFAULT 1 CHECK (quantity >= 1)
);

CREATE TABLE users
(
    user_id         INT             PRIMARY KEY,
    email           VARCHAR(50)     NOT NULL UNIQUE,
    password        VARCHAR(12)     NOT NULL,
    user_name       VARCHAR(10)     NOT NULL,
    phone           VARCHAR(11)     NOT NULL
);

INSERT INTO users(user_id, email, password, user_name, phone)
VALUES
(1, 'x@email.com', 'a12345678', '홍길동', '01012341234'),
(2, 'y@email.com', 'a12345678', '홍길덩', '01012341235');

SELECT * FROM instructors;


INSERT INTO category(category_id, category_name, description)
VALUES
(1, '바지', '가성비 좋은 와이드 팬츠'),
(2, '아우터', '가성비 좋은 코트');

SELECT * FROM category;


INSERT INTO product(product_id, product_name, price, stock, category_id, description)
VALUES
(1, '그레이 와이드팬츠', 60000, 3, 1, '가성비 좋은 와이드 팬츠'),
(2, '검은색 슬랙스', 60000, 1, 1, '가성비 좋은 슬랙스');
(3, '패딩', 100000, 1, 2, '오리털 검은색 패딩');

SELECT * FROM product;

SELECT COUNT(*) FROM product;