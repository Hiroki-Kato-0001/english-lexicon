import matplotlib.pyplot as plt

def plot_region_bar(counts: dict, output_path="images/region_counts.png"):
    keys_to_labels = {
        "brit_count": "Great Britain",
        "name_count": "North America (General)",
        "us_count": "United States",
        "can_count": "Canada",
        "austral_count": "Australia",
        "nz_count": "New Zealand",
        "scot_count": "Scotland",
        "irish_count": "Ireland",
        "ind_count": "India",
        "eafr_count": "East African",
        "wafr_count": "West Africa",
        "safr_count": "South Africa",
        "nafr_count": "North Africa",
        "neng_count": "New England",
        "easi_count": "East Asia",
        "wasi_count": "West Asia",
        "sasi_count": "South Asia",
        "nasi_count": "North Asia"
    }
    labels = []
    sizes = []

    for k, v in counts.items():
        if v > 0 and k != "total":
            labels.append(keys_to_labels[k])
            sizes.append(v)

    plt.figure(figsize=(8, 8))
    plt.bar(labels, sizes, color='skyblue')
    plt.xlabel('Regions')
    plt.ylabel('Counts')
    plt.title('Region Counts from Text Analysis')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    plt.savefig(output_path)
    plt.close()

    return output_path
