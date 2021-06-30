UPDATE fine f, traffic_violation tv
SET f.sum_fine = IF(f.sum_fine IS NULL, tv.sum_fine, f.sum_fine)
WHERE f.violation = tv.violation;
SELECT *
FROM fine
