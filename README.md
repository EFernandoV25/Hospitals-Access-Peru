# Hospitals-Access-Peru
## Data Filtering: Hospitals with "Functioning Status"

In this analysis, only hospitals with a "functioning status" were included. The filtering process was performed as follows:

1. **Filter by Condition:**  
    Only rows where the column `Condición` is equal to `"EN FUNCIONAMIENTO"` were selected.  
    Example code:
    ```python
    df = df[df["Condición"] == "EN FUNCIONAMIENTO"]
    ```

2. **Remove Rows Without Coordinates:**  
    Rows missing values in the coordinate columns (`NORTE`, `ESTE`) were dropped to ensure spatial accuracy.

3. **Convert Coordinates to Numeric:**  
    The coordinate columns were converted to numeric types, and any remaining invalid entries were removed.

This ensures that all hospitals analyzed are currently operational and have valid geographic locations.
