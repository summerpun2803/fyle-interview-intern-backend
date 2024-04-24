-- Write query to get number of graded assignments for each student:
SELECT
    student_id,
    state,
    COUNT(*) AS count
FROM
    assignments
WHERE
    state IN ('DRAFT', 'GRADED', 'SUBMITTED')
GROUP BY
    student_id,
    state;
