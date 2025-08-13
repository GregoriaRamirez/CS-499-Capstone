# Algorithms & Data Structures — Original Artifact

## Description

This original artifact contains the first version of the Animal Shelter Dashboard’s filtering and data processing logic, developed during CS 340: Client-Server Development. In this version, filtering for breed, color, and outcome type was implemented using repetitive loops and conditional checks. The logic was embedded directly into the same function that updated charts and maps, making it harder to maintain and extend.

The approach was functional but inefficient, as repetitive code increased the risk of errors and made performance slower on larger datasets. There was no input validation, meaning that incorrect or unsupported filter selections could lead to errors or unintended results.

This version serves as the baseline for comparing later enhancements that introduced vectorized operations, modular functions, and validation for more reliable performance.


## Limitations
- Repeated code for each filter (breed, color, outcome type).
- Inefficient row-by-row filtering instead of optimized operations.
- Filtering logic and UI callbacks tightly coupled.

## Technologies Used
- Python
- Dash
- Pandas

