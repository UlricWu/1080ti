import csv

# define your input dataset
#output would be added _tab
input_file_name = "cust_complains_all_through_3_31.csv"
output_file_name = "cust_complains_all_through_3_31_tab.csv"

#replace special strings
def remove_n_r(column):
    column = column.replace('\n','')
    column = column.replace('\r','')
    column = column.replace('\t','')
    return column

in_txt = csv.reader(open(input_file_name, encoding="utf8"), delimiter = ',')

out_csv = open(output_file_name, 'w', newline='\n', encoding="utf8")
csv_writer = csv.writer(out_csv, delimiter = '\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
line_count = 0

# statistics about the how many columns are been precessed
for row in in_txt:
    if line_count == 0:
        print('Column names are:', row)
        line_count += 1
    else:
        new_row = []
        for col in row:
            new_row.append(remove_n_r(col))
        csv_writer.writerow(new_row)
        line_count += 1

out_csv.close()
print('Processed',line_count,' lines.')
