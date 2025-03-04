## Assignment Three
### Introduction
This is the directory for my third assignment.  

### My Chosen Database :blue_book:

I chose to make a database inspired by my current role as an Assistant within a Film Technicians agency. We need to keep track of a lot of data, such as client information (full name, 
job role, availability), project information (project name, start date, end date) and invoices (invoice number, whether the invoices have been sent). A lot of this data also needs to be 
interlinked, i.e., we often need to be able to find the corresponding client for each invoice when a payment has been made. This can be based on the project ID for the invoice, 
and in turn the client ID for the project. In setting up three separate, normalised tables for each of these areas of information, I have demonstrated how to use joins and stored procedures 
to retrieve necessary data corresponding to production enquiries (e.g., we may get enquiries about availability for a specific role). I have also shown how stored procedures can be utilised 
to more easily add and delete clients when they join/leave the agency. Finally, I implemented aggregate functions to calculate the number of clients the agency has on their books in each specific role, 
and to analyse which projects are due to finish first and last.
