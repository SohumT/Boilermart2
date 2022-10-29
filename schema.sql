
CREATE TABLE stores(
  store_id integer PRIMARY KEY,
  store_name varchar(50),
  company_id integer,
  address varchar(50),
  zipcode integer,
); 

CREATE TABLE items( 
  item_id integer,
  store_id integer,
  name varchar(50),
  price integer,
  weight decimal(4,1),
  category varchar(50),
  stock integer,
  PRIMARY KEY (item_id)
);

CREATE TABLE discounts(
  store_id integer,
  item_id integer,
  sale_name varchar(50),
  percentage decimal(2,2),
  PRIMARY KEY(store_id, item_id)
); 

CREATE TABLE company(
  company_id integer,
  name text,
  sales integer,
  PRIMARY KEY (company_id)
); 

CREATE TABLE Users(
  User_id integer NOT NULL AUTOINCREMENT,
  Username varchar(50),
  Password text,
  Last_Frequented_Store int, 
  Last_Item int,
  address text,
  zipcode integer,
  PRIMARY Key (User_id)
);

