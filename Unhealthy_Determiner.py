import csv
import math
'''
restaurant,item,calories,cal_fat,total_fat,sat_fat,trans_fat,cholesterol,sodium,total_carb,fiber,sugar,protein,vit_a,vit_c,calcium,salad
'''
# Input files
UNHEALTHY_FOODS = "unhealthy_foods.csv"
IDEAL_MEAL = "Ideal_Meal.csv"

# Output file
OUTPUT_FILE = "unhealthy_index_scores.csv"

def percent_error(experimental, theoretical):
    """Calculate percent error. Handles divide-by-zero safely."""
    if theoretical == 0:
        return float('nan')
    return abs((experimental - theoretical) / theoretical) * 100

def main():
    # Load ideal meal values (only one row)
    with open(IDEAL_MEAL, "r", encoding="utf-8") as ideal_file:
        reader = csv.DictReader(ideal_file)
        ideal_row = next(reader)  # assume only one ideal meal row

        # Convert metrics to floats
        ideal_values = {col: float(ideal_row[col]) for col in range(2, 16)}

    # Prepare output file
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["restaurant", "item", "Healthy Index Score"])

        # Process each food item
        with open(UNHEALTHY_FOODS, "r", encoding="utf-8") as foods_file:
            reader = csv.DictReader(foods_file)

            for row in reader:
                errors = [] # Creates a list to contain the percent errors for each food item

                for col in range(2, 16):
                    experimental_val = float(row[col])
                    theoretical_val = ideal_values[col]
                    error = percent_error(experimental_val, theoretical_val)

                    if not math.isnan(error):
                        errors.append(error)

                unhealthy_index_score = sum(errors) / 14

                writer.writerow([row["restaurant"], row["item"], round(unhealthy_index_score, 2)]) # Creates a row with the data