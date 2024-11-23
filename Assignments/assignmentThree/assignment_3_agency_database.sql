-- Creating the database for a film technicians agency

CREATE DATABASE film_agency;

USE film_agency;

/* Creating tables
I created a client table to include basic personal information such as name, job role 
and whether they are available for work. All the information is crucial for the agency to run, so all
data is marked as 'Not Null', i.e., each client must provide us with the information for each column. */

CREATE TABLE clients (
client_id INTEGER NOT NULL AUTO_INCREMENT,
first_name VARCHAR(255) NOT NULL,
last_name VARCHAR(255) NOT NULL,
job_role ENUM("Costume Designer", "Director of Photography", "Editor", 
"Hair and Make-up Designer", "Line Producer", "Production Designer", "Sound Mixer") NOT NULL,
available ENUM("Yes", "No") NOT NULL,
PRIMARY KEY (client_id)
);

/* Next I created a projects table, containing information about each project that is currently being worked on 
or that has previously been worked on by a client. Client ID was the foreign key for this table to link
the data to a specific client (without unnecessary repetition of the 'Name' columns). Again, I have 
utilised the 'Not Null' restraint for all required data. */

CREATE TABLE projects (
project_id INTEGER NOT NULL, 
project_name VARCHAR(255),
client_id INTEGER,
start_date DATE NOT NULL,
end_date DATE NOT NULL,
PRIMARY KEY (project_id),
FOREIGN KEY (client_id) REFERENCES clients(client_id)
);

/* Finally, I created a table for keeping track of invoices that have been issued for each project. Again, this can
can be linked by a foreign key to the project ID in the projects table to get more information about the project
(such as its name), and in turn the client/s working on the project. The invoice batch code must be unique, as this
is what will help us to identify each payment that is received. */

CREATE TABLE invoices (
invoice_batch_code VARCHAR(255) NOT NULL UNIQUE,
project_id INTEGER,
invoices_sent ENUM("Yes", "No") NOT NULL,
PRIMARY KEY (invoice_batch_code),
FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

/* Inserting data
I used the insert command to populate each of my tables with sample data. */

INSERT INTO clients
(first_name, last_name, job_role, available)
VALUES
("Rachel", "Green", "Costume Designer", "Yes"),
("Monica", "Geller", "Production Designer", "No"),
("Ross", "Geller", "Sound Mixer", "No"),
("Joey", "Tribbiani", "Production Designer", "Yes"),
("Chandler", "Bing", "Editor", "Yes"),
("Phoebe", "Buffay", "Hair and Make-up Designer", "No"),
("Mike", "Hannigan", "Sound Mixer", "No"),
("Central", "Perk", "Director of Photography", "Yes");

INSERT INTO projects
(project_id, project_name, client_id, start_date, end_date)
VALUES
(101, "Holiday Armadillo", 3, "2024-04-04", "2024-07-30"),
(102, "Smelly Cat", 6, "2024-09-01", "2024-12-20"),
(103, "Transponster", 5, "2023-12-30", "2024-09-15"),
(104, "Days of Our Lives", 4, "2024-01-12", "2024-06-15"),
(105, "In London", 2, "2024-08-20", "2024-11-22"),
(106, "Banana Hammock", 7, "2024-07-01", "2024-11-30"),
(107, "Leather Pants", 3, "2024-08-01", "2024-10-16"),
(108, "Bloomies", 1, "2024-01-06", "2024-09-05");

INSERT INTO invoices
(invoice_batch_code, project_id, invoices_sent)
VALUES
("FRIENDS1", 103, "Yes"),
("FRIENDS2", 108, "Yes"),
("FRIENDS3", 104, "Yes"),
("FRIENDS4", 101, "Yes"),
("FRIENDS5", 106, "Yes"),
("FRIENDS6", 107, "Yes"),
("FRIENDS7", 105, "Yes"),
("FRIENDS8", 102, "No");

/* Queries
Please note: all code below has been commented out to avoid it being auto-run, so should be un-commented for testing.
The main purpose of an agency is to provide a list of clients in a specific role, that are currently 
available for work. I created a procedure that would present this information for a given role when called; 
in my example, I have selected all available Production Designers. */

-- DELIMITER //
-- CREATE PROCEDURE get_role_availability(IN client_role VARCHAR(255))
-- BEGIN
-- 	SELECT c.first_name, c.last_name, c.job_role
--     FROM clients c
--     WHERE c.job_role = client_role AND c.available = "Yes"
--     ORDER BY c.last_name ASC;
-- END //

-- DELIMITER ;

-- CALL get_role_availability("Production Designer");

/* It may also be useful when keeping track of company data to find out how many clients within each job role
the company represents. You can do so by using the below function (again, I have used the Production Designer
role for my example): */

-- DELIMITER //
-- CREATE FUNCTION get_role_count(client_role VARCHAR(255))
-- RETURNS INT
-- DETERMINISTIC
-- BEGIN
-- 	DECLARE role_count INT;
-- 	SELECT COUNT(client_role) INTO role_count FROM clients 
--     WHERE job_role = client_role;
--     RETURN role_count;
-- END //

-- DELIMITER ;

-- SELECT get_role_count("production designer") AS Role_Count;

/* In order to get an overview of which clients are on which project, including the clients who are not on a project, 
we can use a Left Join of the client and project tables: */

-- SELECT 
-- c.first_name, c.last_name, p.project_name
-- FROM
-- clients c
-- LEFT JOIN 
-- projects p
-- ON
-- c.client_id = p.client_id
-- ORDER BY
-- c.last_name ASC;

/* It could also be useful to get a full idea of which client is on which project, as well as whether or not their
invoices have been submitted. This can be achieved with a join of all three tables; I concatenated the strings
first three pieces of information to make the main point - whether the invoices have been sent - stand out more. */

-- SELECT
-- CONCAT(c.first_name, " ", c.last_name, " - ", p.project_name) AS Client_and_Project, inv.invoices_sent
-- FROM
-- clients c
-- JOIN
-- projects p 
-- JOIN
-- invoices inv
-- WHERE
-- c.client_id = p.client_id AND p.project_id = inv.project_id
-- ORDER BY inv.invoices_sent ASC;

/* For ease, I created a procedure to insert a new client.*/

-- DELIMITER //
-- CREATE PROCEDURE add_client(
--     IN new_first_name VARCHAR(255),
--     IN new_last_name VARCHAR(255),
--     IN new_job_role ENUM("Costume Designer", "Director of Photography", "Editor", "Hair and Make-up Designer", "Line Producer", "Production Designer", "Sound Mixer"),
-- 	IN new_available ENUM("Yes", "No")
-- )
-- BEGIN
--     INSERT INTO clients (first_name, last_name, job_role, available)
--     VALUES (new_first_name, new_last_name, new_job_role, new_available);
-- END //

-- DELIMITER ;

-- CALL add_client ("Test", "Tester", "Director of Photography", "Yes");

/* And also a procedure to delete a client, if they decide to leave the agency. */

-- DELIMITER //
-- CREATE PROCEDURE delete_client(
--     IN deleted_client_id INT
-- )
-- BEGIN
--     DELETE 
--     FROM clients
--     WHERE client_id = deleted_client_id;
-- END //

-- DELIMITER ;

-- CALL delete_client(9);

/* Uncomment code below to re-set for purpose of the example. */

-- ALTER TABLE clients
-- AUTO_INCREMENT = 9;

/* It is quite common for end dates on projects to change, this can be updated in our Projects table
using the following procedure (here I've changed the end date of Project 103 - "Transponster" as an example): */

-- DELIMITER //
-- CREATE PROCEDURE change_end_date(IN interval_change INT, IN changing_project_id INT)
-- BEGIN
-- 	UPDATE projects
--     SET end_date = ADDDATE(end_date, INTERVAL interval_change DAY)
--     WHERE project_id = changing_project_id;
-- END //

-- DELIMITER ;

-- CALL change_end_date(10, 103);

/* Sometimes it can be useful to determine which project started first, or ends last. This can be
calculated using the following data retrieval methods: */
 
-- SELECT
-- project_name, end_date 
-- AS project_ending_latest
-- FROM
-- projects 
-- WHERE end_date = (SELECT MAX(end_date) FROM projects);

-- SELECT
-- project_name, end_date 
-- AS project_ending_earliest
-- FROM
-- projects 
-- WHERE end_date = (SELECT MIN(end_date) FROM projects);
