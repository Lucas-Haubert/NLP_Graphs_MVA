import pandas as pd
import numpy as np

# List of submission paths with their corresponding coefficients
submission_info = [('submissions/submission_gat.csv', 0.747),
                   ('submissions/submission_gcn.csv', 0.751),
                   ('submissions/submission_gin.csv', 0.770),
                   ('submissions/submission_stacked_gat.csv', 0.777),
                   ('csv/gat.csv', 0.697),
                   ('csv/gcn.csv', 0.671),
                   ('csv/gin.csv', 0.720),
                   ('csv/gin2.csv', 0.700)]

# Initialize an empty list to store the scaled matrices
scaled_matrices = []
coefficients_sum = 0

# Read and scale matrices
for path, coefficient in submission_info:
    solution = pd.read_csv(path, index_col='ID').values
    # If normalize
    # solution = np.apply_along_axis(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)), axis=1, arr=solution)
    scaled_matrices.append(solution * coefficient)
    coefficients_sum += coefficient

# Calculate the weighted average
print(coefficients_sum)
result = np.sum(scaled_matrices, axis=0)

# Normalize result if coefficients sum is not equal to 1
if coefficients_sum != 1:
    result /= coefficients_sum

# Create DataFrame
solution = pd.DataFrame(result)
solution['ID'] = solution.index
solution = solution[['ID'] + [col for col in solution.columns if col != 'ID']]

# Save to CSV
solution.to_csv('csv/merged2.csv', index=False)