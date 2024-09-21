import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    col_n = ["student_id","age"]
    # pd.DataFrame()
    return pd.DataFrame(student_data,columns = col_n)

    