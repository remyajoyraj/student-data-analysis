import matplotlib
matplotlib.use('TkAgg')   # 👈 add this line

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("students.csv")

df["Average"] = df[["Maths", "Science", "English"]].mean(axis=1)

def grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    else:
        return "C"

df["Grade"] = df["Average"].apply(grade)

top_student = df.loc[df["Average"].idxmax()]
low_attendance = df[df["Attendance"] < 75]

print(df)
print("\nTop Student:\n", top_student)
print("\nLow Attendance:\n", low_attendance)

# Save result
df.to_csv("output.csv", index=False)

plt.figure(figsize=(6,4))
plt.bar(df["Name"], df["Average"])

plt.title("Student Average Marks")
plt.xlabel("Students")
plt.ylabel("Average Marks")

plt.savefig("graph.png")
plt.close()