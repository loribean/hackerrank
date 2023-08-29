```The given table students contains the total marks of a student in a class
The teach of the class wasnt to assign grades based on the total marks and the table is as follows
Greater than 90 A+
Greater than 70 and less than equal to 90 A
Greater than 50 and less than equal to 70 B
Greater than or equal 40 to C
Less than 40 F


```sql

select id, name, marks,
case
when marks > 90 then 'A+'
when marks > 70 and marks <= 90 then 'A'
when marks > 50 and marks <= 70 then 'B'
when marks >= 40 and marks <= 50 then 'C'
else 'Fail'
end as grade


```

