import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ── 1. Load & Clean Data ──────────────────────────────────────────────
df = pd.read_csv('All_Diets.csv')

df['Diet_type'] = df['Diet_type'].str.lower().str.strip()

df['Protein(g)'].fillna(df['Protein(g)'].mean(), inplace=True)
df['Carbs(g)'].fillna(df['Carbs(g)'].mean(), inplace=True)
df['Fat(g)'].fillna(df['Fat(g)'].mean(), inplace=True)

print(" Data loaded and cleaned.")
print(f"   Total recipes: {len(df)}")
print(f"   Diet types: {df['Diet_type'].unique()}")

# ── 2. Average Macronutrients per Diet Type ───────────────────────────
avg_macros = df.groupby('Diet_type')[['Protein(g)', 'Carbs(g)', 'Fat(g)']].mean()
print("\n Average Macronutrients per Diet Type:")
print(avg_macros)

# ── 3. Top 5 Protein-Rich Recipes per Diet Type ───────────────────────
top_protein = (df.sort_values('Protein(g)', ascending=False)
                 .groupby('Diet_type')
                .head(5)[['Diet_type', 'Recipe_name', 'Protein(g)', 'Cuisine_type']])
print("\n Top 5 Protein-Rich Recipes per Diet Type:")
print(top_protein)

# ── 4. Diet Type with Highest Average Protein ─────────────────────────
highest_protein_diet = avg_macros['Protein(g)'].idxmax()
print(f"\n Diet with highest average protein: {highest_protein_diet}")

# ── 5. Most Common Cuisine per Diet Type ──────────────────────────────
common_cuisines = (df.groupby(['Diet_type', 'Cuisine_type'])
                     .size()
                     .reset_index(name='count')
                     .sort_values('count', ascending=False)
                     .groupby('Diet_type')
                     .first())
print("\n  Most Common Cuisine per Diet Type:")
print(common_cuisines)

# ── 6. New Metrics ────────────────────────────────────────────────────
df['Protein_to_Carbs_ratio'] = df['Protein(g)'] / df['Carbs(g)'].replace(0, 0.001)
df['Carbs_to_Fat_ratio']     = df['Carbs(g)']   / df['Fat(g)'].replace(0, 0.001)
print("\n New metrics added: Protein_to_Carbs_ratio, Carbs_to_Fat_ratio")

# ── 7. Visualizations ─────────────────────────────────────────────────
os.makedirs('visualizations', exist_ok=True)

# Chart 1: Bar chart
avg_macros.plot(kind='bar', figsize=(10, 6), color=['steelblue', 'coral', 'mediumseagreen'])
plt.title('Average Macronutrient Content per Diet Type')
plt.xlabel('Diet Type')
plt.ylabel('Grams (g)')
plt.xticks(rotation=45)
plt.legend(['Protein', 'Carbs', 'Fat'])
plt.tight_layout()
plt.savefig('visualizations/bar_avg_macros.png')
plt.show()
print(" Bar chart saved.")

# Chart 2: Heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(avg_macros, annot=True, fmt='.1f', cmap='YlOrRd')
plt.title('Macronutrient Heatmap by Diet Type')
plt.tight_layout()
plt.savefig('visualizations/heatmap_macros.png')
plt.show()
print(" Heatmap saved.")

# Chart 3: Scatter plot
top5_all = df.sort_values('Protein(g)', ascending=False).head(50)
plt.figure(figsize=(12, 6))
sns.scatterplot(data=top5_all, x='Cuisine_type', y='Protein(g)',
                hue='Diet_type', s=100)
plt.title('Top Protein-Rich Recipes by Cuisine Type')
plt.xlabel('Cuisine Type')
plt.ylabel('Protein (g)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('visualizations/scatter_top_protein.png')
plt.show()
print(" Scatter plot saved.")

print("\n Task 1 complete! All visualizations saved to /visualizations/")
