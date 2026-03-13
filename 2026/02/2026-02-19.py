def avalanche_risk(snow_depth, slope):
    data = {
       'Gentle': {'Shallow': "Safe", 'Moderate': "Safe", 'Deep': "Safe"},
       'Steep': {'Shallow': "Safe", 'Moderate': "Risky", 'Deep': "Risky"},
       'Very Steep': {'Shallow': "Safe", 'Moderate': "Risky", 'Deep': "Risky"}
    }

    return data[slope][snow_depth]


assert avalanche_risk("Shallow", "Gentle") == "Safe"
assert avalanche_risk("Shallow", "Steep") == "Safe"
assert avalanche_risk("Shallow", "Very Steep") == "Safe"
assert avalanche_risk("Moderate", "Gentle") == "Safe"
assert avalanche_risk("Moderate", "Steep") == "Risky"
assert avalanche_risk("Moderate", "Very Steep") == "Risky"
assert avalanche_risk("Deep", "Gentle") == "Safe"
assert avalanche_risk("Deep", "Steep") == "Risky"
assert avalanche_risk("Deep", "Very Steep") == "Risky"