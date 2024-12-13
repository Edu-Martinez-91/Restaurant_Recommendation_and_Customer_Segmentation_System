CREATE DATABASE restaurants;

-- Simply out of curiosity and to see how the values iterate belonging to a single table, 
-- we will perform an INNER JOIN of all the tables in the database, 
-- losing many values along the way, and extract it directly in the Python script. 

SELECT *
FROM user_profile u
JOIN rating r
USING (userID)
JOIN user_pay
USING (userID)
JOIN user_cui
USING (userID)
JOIN location l
USING (placeID)
JOIN rest_pay rp
USING (placeID)
JOIN rest_cui rc
USING (placeID)
JOIN if_parking ip
USING (placeID)
JOIN opening
USING (placeID);

-- Now we will retrieve the data for exploratory analysis. One of the most interesting tables is the users profile, 
-- and it is where we will start from.

SELECT *
FROM user_profile;

-- The other table that have more data, is the location 
-- one:

SELECT * 
FROM location;

SELECT *
FROM rest_cui;

SELECT DISTINCT(parking_lot)
FROM if_parking;

SELECT *
FROM rating;



-- Now we will try to extract the table of locations and users to perform a statistical analysis of both in Python.

SELECT *
FROM user_profile u
JOIN rating r
USING (userID)
JOIN location l
USING (placeID);

 -- Aquí vemos si el rating de satisfacción es mayor entre aquellos que no son abstemios, 
 -- 
    SELECT 
    SUM(CASE WHEN alcohol = 'No_Alcohol_Served' THEN 1 ELSE 0 END) AS count_no_alcohol_served,
    SUM(CASE WHEN alcohol != 'No_Alcohol_Served' THEN 1 ELSE 0 END) AS count_with_alcohol_served
FROM 
    (
        SELECT r.rating, l.alcohol, u.drink_level
        FROM user_profile u
        JOIN rating r USING (userID)
        JOIN location l USING (placeID)
    ) AS combined_data
WHERE 
    combined_data.drink_level != 'abstemious' 
    AND combined_data.rating = 2;
    
