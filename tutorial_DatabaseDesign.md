Principles of Relational Database Design
----------------------------------------

1. No redundancy - a single column goes into only one table!

    - except for foreign keys, they are the only exception - because they're used to join tables

2. No bad dependancies
  - What are dependencies?
  - determinants?
  - candidate key? (self explanatory?)
  - partial dependancy?
  - transitive dependancy?

Normalization:

  - Eliminating 'bad' dependencies, by splitting up data into tables and linking via foreign keys

Normal forms:

  - First Normal Form (1NF)

When all attributes are atomic, i.e., not nested.
I think I kind of get this, but yeah. When you have nested categories
(like say, sub-genres, inside of genres?, or albums, nested into artists?)

- I suppose they're should be a way to use foreign keys to link song titles to artists, and albums from other tables.
- So I shou

Not nested?

  - Second Normal Form (2NF)
  - Third Normal Form (3NF) 
  - *Boyce-Codd Normal Form (BCNF)* - what's this? why is it in the middle?
  - Fourth Normal Form (4NF) 
  - Fifth Normal Form (5NF)

Mistakes to Avoid
-----------------

1. Poor design/planning

Just like building a house, a database needs to be well designed.

So what constitutes a 'well-designed' database?

2. Ignoring normalization
3. Poor naming standards
4. Lack of documentation
5. One table to hold all domain values
6. Using identity/guid columns as your only key
7. Not using SQL facilities to protect data integrity
8. Not using stored procedures to access data
9. Trying to build generic objects
10. Lack of testing
