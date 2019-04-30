.. toctree::
   :maxdepth: 3


Using algo_deduplicate - Entry points
**********************************


Dependencies
============

    + python (3.6)
    + tensorflow (1.12)
    + keras (2.2.4)
    
    
Run
===
 
1. Go to the project directory:
PRJ_PATH=/path/to/items_deduplication/
cd PRJ_PATH

2. run algo_deduplicate using the command:

bash>> python run_deduplication.py path/2/image_1 path/2/image_2
  
  This piece of code get image_1 & image_2 as inputs and 
  return a score between 0 and 100 indicating whether they are duplicates (close to 100) or not (close to 0)
  

Testing
=======

Run unittests

bash>> iduplicate_tests.py

- Feel free to add more unittest cases for more checking



