-- # 1st Normal Form (Singularity, Atomicity)
-- 1. Each cell must contain one value, not a list (Singularity) -> create a new table 
-- 2. All row must be unique (no duplicate rows) -> adding ID number 
-- 3. Each value must not be divisible (Atomicity) -> adding column to divide


-- # 2nd Normal Form (No partial dependencies)
-- 1. Non partial dependencies - all non-prime attributes should be FULLY functionally dependant on the candidate key(ex. composite key) -> create seperate table 


-- # 3rd normal Form (No transitive dependencies)
-- 1. All fields must ONLY be determined by the primary/composite key, not by other keys -> create sperate table 




