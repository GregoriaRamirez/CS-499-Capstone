# 🧮 Algorithms & Data Structures Artifact

## 📌 Artifact Description
For this category, I selected my Animal Shelter Dashboard project originally built for CS 340: Client-Server Development in February 2025. The artifact was a web dashboard built in Jupyter Notebook using Python framework and Dash that connected to a MongoDB database which pulled data from an uploaded CSV file. It displayed a table of  ten thousand records of animal shelter outcomes through a searchable record list that included filters and charts.The dashboard allows users to explore shelter outcome data using dropdown and radio button filters and visualizes the results in a searchable table and interactive charts.

## 📎 Justification for Inclusion
I included this artifact in my ePortfolio because it demonstrates how I applied structured logic and efficient control flow to solve real-world filtering and visualization problems. In the original version, the `update_dashboard()` function used repetitive if blocks and direct filtering that made it harder to manage. In the enhanced version, I reorganized this function to apply layered filters that only trigger when conditions are met. I also used pandas’ vectorized operations to make filtering more efficient and added input validation so the dashboard would not break when dropdowns were empty or when combinations did not match any records.

## 🔍 Examples Before and After Enhancements
**Original Code (Before Enhancement)**  
```python
# Filtering data directly on original DataFrame multiple times
if filter_type == 'water':
    filtered_df = df[(df['breed'].str.contains('Labrador Retriever')) & 
                     (df['outcome_type'] == 'Euthanasia')]
```
This approach:  
1. Repeatedly filters the full DataFrame  
2. Overwrites previous filter results without preserving the original data  
3. Does not handle empty or missing filter inputs properly  

**Enhanced Code (After Enhancement)**  
```python
def update_dashboard(filter_type, selected_colors, selected_breeds):
    filtered_df = df.copy()
    if filter_type == 'water':
        filtered_df = filtered_df[
            (filtered_df['breed'].str.contains('Labrador Retriever', na=False)) &
            (filtered_df['outcome_type'] == 'Euthanasia') &
            (filtered_df['animal_type'] == 'Dog')
        ]
    elif filter_type == 'mount':
        filtered_df = filtered_df[
            (filtered_df['outcome_type'] == 'Transfer') &
            (filtered_df['animal_type'] == 'Cat') &
            (filtered_df['sex_upon_outcome'].str.contains('Female', na=False)) &
            (filtered_df['age_upon_outcome_in_weeks'].between(52, 260))
        ]
    # Additional filters
    if selected_colors:
        filtered_df = filtered_df[filtered_df['color'].isin(selected_colors)]
    if selected_breeds:
        filtered_df = filtered_df[filtered_df['breed'].isin(selected_breeds)]
    return filtered_df.to_dict('records')
```

## 🔑 Key Enhancements
1. Added layered (chained) filter conditions that apply sequentially and only when relevant, improving clarity and control flow.  
2. Used `df.copy()` to create a separate working dataset, preserving the original data and preventing unintended side effects.  
3. Implemented safer filtering methods such as `.str.contains(..., na=False)` and `.isin()` to avoid runtime errors caused by missing or null data.  
4. Handled multiple filter combinations properly so that filters work together instead of conflicting or overwriting each other.  
5. Returned a clean, consistent data structure with `.to_dict('records')` that the dashboard can reliably use.

These changes improved runtime efficiency, performance, and stability. For example, filtering a 3,000-row DataFrame down to just 150–300 relevant records per interaction significantly improved responsiveness during rapid user input. The dashboard now responds smoothly to user interactions and avoids crashing due to empty fields or unmatched data.

## 🛡️ Additional Reliability Measures
I added input checks to prevent the dashboard from crashing when users leave filters empty or select options with no matching data. This avoids errors that could make the app unstable or stop it from working. By catching missing data or null inputs early, I ensured predictable behavior in the interface, improving stability and reliability. While this is not the same as security features like login or encryption, it keeps the app functional and safe from data-handling issues that could cause failures. In the future, I plan to implement user authentication or role-based access control if the app were to go live.

## 🎯 Alignment to Program Outcomes
This enhancement aligns with **Outcome 3**: Design and evaluate computing solutions that solve a given problem using algorithmic principles and computer science practices and standards appropriate to its solution, while managing the trade-offs involved in design choices. By using layered filtering logic and efficient data-handling methods, I improved both performance and stability while managing complexity in how filters interact.

## 🔄 Reflection on Enhancement Process
Enhancing this artifact helped me better understand the importance of organizing logic for readability and performance. One challenge I faced was making sure multiple filters could work together without interfering with one another’s results. I had to test various combinations and inputs to ensure the application responded as expected in all cases. I was careful with handling missing values or null fields, which required using `na=False` to prevent errors when filtering string fields. Another challenge was maintaining readability while introducing more flexible logic. I used comments and modular blocks to keep the function easy to follow while still expanding its functionality.

This process improved my confidence in using control flow and data structures to solve real problems. It also taught me how clear, well-planned logic can lead to more stable and professional applications.
