UPDATE fine,
    (
    SELECT name, number_plate, violation
    FROM fine
    GROUP BY name, number_plate, violation
    HAVING COUNT (number_plate) > 1
    ) AS query_in

SET sum_fine = sum_fine * 2

WHERE fine.date_payment IS NULL
  AND
    query_in.name = fine.name
  AND
    query_in.number_plate = fine.number_plate
  AND
    query_in.violation = fine.violation