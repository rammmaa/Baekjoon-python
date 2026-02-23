SELECT ID,
       CASE
           WHEN rn <= cnt * 0.25 THEN 'CRITICAL'
           WHEN rn <= cnt * 0.50 THEN 'HIGH'
           WHEN rn <= cnt * 0.75 THEN 'MEDIUM'
           ELSE 'LOW'
       END AS COLONY_NAME
FROM (
    SELECT ID,
           ROW_NUMBER() OVER (ORDER BY SIZE_OF_COLONY DESC) AS rn,
           COUNT(*) OVER () AS cnt
    FROM ECOLI_DATA
) t
ORDER BY ID;