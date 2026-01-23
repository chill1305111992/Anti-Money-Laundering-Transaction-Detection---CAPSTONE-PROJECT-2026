import pandas as pd

# File paths
input_file = r"..\data\raw\SAML-D_reduced.csv"
output_file = r"..\data\raw\SAML-D_reduced2.csv"

# Read the CSV file
print("Loading CSV file...")
df = pd.read_csv(input_file)

print(f"Original dataset shape: {df.shape}")
print(f"Original number of rows: {len(df)}")

# Keep every 10th row (reduce by 10x)
df_reduced = df.iloc[::2, :].reset_index(drop=True)

print(f"Reduced dataset shape: {df_reduced.shape}")
print(f"Reduced number of rows: {len(df_reduced)}")

# Save to new CSV file
df_reduced.to_csv(output_file, index=False)

print(f"✓ Reduced dataset saved to: {output_file}")
print(f"Reduction ratio: {len(df) / len(df_reduced):.1f}x")