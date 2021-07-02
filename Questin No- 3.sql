#database creation
create DATABASE iffat;

#table creation
CREATE TABLE STUDENTS (
    ID INT,
    Nmae varchar(11),
    Marks int,
);

#insert values into STUDENTS
 INSERT INTO STUDENTS (
    ID,
    Name,
    Marks
    
)
VALUES
    (
        1,
        'Ashley',
        81
    ),
    (
        2,
        'Samantha',
        75
    ),
    (
        4,
        'Julia',
        76
    ),
    (
        3,
        'Belvet',
        84
    );

# question no. 3
SELECT NAME FROM STUDENTS WHERE Marks > 75 ORDER BY RIGHT(NAME, 3), ID ASC;