import csv
'''
Take the fastfood csv file, look at the titles, and if it contains words like "Grilled", "Wrap", "Veggie",
and place that into a new csv file for healthy foods, and the rest go into unhealthy foods
'''
# Create the input and output files
input_file = "fastfood.csv"
output_file = "healthy_foods.csv"
output_file2 = "unhealthy_foods.csv"

with open(input_file, 'r') as f:
    reader = csv.reader(f)

    with open(output_file, 'w') as f2:

        writer = csv.writer(f2)

        with open(output_file2, 'w') as f3:

            writer2 = csv.writer(f3)

            for row in reader: 
                if "Grilled" in row[1] or "Wrap" in row[1] or "Veggie" in row[1] or "Salad" in row[1] or "Roll" in row[1] or "BLT" in row[0] or "VEGGIE" in row[0]:
                    writer.writerow(row)
                else:
                    writer2.writerow(row)