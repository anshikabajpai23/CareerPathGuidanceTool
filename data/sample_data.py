import pandas as pd
import random

# Define skills
skills = ["Python", "SQL", "ML", "Statistics", "Deep Learning", "Communication", "Java", "C++", "Algorithms", "Databases", "TensorFlow", "PyTorch"]

# Generate synthetic skill vectors
data = []
num_instances = 10  # total placeholder rows
for _ in range(num_instances):
    row = [random.randint(0, 1) for _ in skills]
    data.append(row)

# Create DataFrame
df = pd.DataFrame(data, columns=skills)

print(df)


df.to_csv("sample_skills_data.csv", index=False)