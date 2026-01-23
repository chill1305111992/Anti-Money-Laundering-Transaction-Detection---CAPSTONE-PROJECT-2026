import json
import os

path = r'c:\Users\Андрій\FLASK WEB APP\Flask-Web-App-Tutorial\03_statistical_analysis.ipynb'
with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

new_cells = []
for cell in nb['cells']:
    # Replace the first broken cell with a markdown cell
    if cell.get('id') == 'da4e00f9':
        new_cells.append({
            "cell_type": "markdown",
            "id": "da4e00f9",
            "metadata": {},
            "source": [
                "### 7. Customer-level Segmentation\n",
                "We aggregate transactions by sender account to identify high-risk customers."
            ]
        })
        continue
    
    # Fix the second broken cell
    if cell.get('id') == 'aa2ee372':
        new_cells.append({
            "cell_type": "code",
            "execution_count": None,
            "id": "aa2ee372",
            "metadata": {},
            "outputs": [],
            "source": [
                "# 7. Customer-level segmentation\n",
                "customer_stats = transactions.groupby(\"Sender_account\").agg(\n",
                "    total_transactions=(\"Is_laundering\", \"count\"),\n",
                "    suspicious_count=(\"Is_laundering\", \"sum\"),\n",
                "    suspicious_ratio=(\"Is_laundering\", \"mean\")\n",
                ").reset_index()\n",
                "\n",
                "# Using qcut with duplicates='drop' as many customers have 0 ratio\n",
                "customer_stats[\"risk_band\"] = pd.qcut(\n",
                "    customer_stats[\"suspicious_ratio\"], \n",
                "    q=[0, 0.5, 0.9, 1.0], \n",
                "    labels=[\"Low\", \"Medium\", \"High\"],\n",
                "    duplicates='drop'\n",
                ")\n",
                "print(\"Risk Band Distribution:\")\n",
                "print(customer_stats[\"risk_band\"].value_counts())\n",
                "customer_stats.sort_values(\"suspicious_ratio\", ascending=False).head()\n"
            ]
        })
        continue
    
    new_cells.append(cell)

nb['cells'] = new_cells

with open(path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
