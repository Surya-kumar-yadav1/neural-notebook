import pandas as pd

df = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR", "Finance"],
    "Salary": [50000, 60000, 40000, 45000, 55000],
    "Age": [50, 60, 40, 4, 50]
})
grp=df.groupby("Department").agg(
    avg_sal=("Salary","mean"),
    max_age=("Age","max")
)
print(grp)