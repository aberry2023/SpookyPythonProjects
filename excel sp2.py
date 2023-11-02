from collections import Counter, defaultdict
import xldr

wb = xl.load_workbook("support files/censuspopdata.xlsx")
sheet = wb.active

#Create a unique list of all state names from the state column (which is 2nd column)
states = {cell.value for cell in list(sheet.columns)[1][2:]}

#Initiate the countie_in_state dict to hold a set for each state key as it would be populated when the Excel is read row-by-row
counties_in_state = defaultdict(set)

# counter counts the number of census tracts(rows) and counter_pop holds the cumulative population
counter = Counter()
counter_pop = Counter()

#Skip the first row as it contains column names
for row in range(2, sheet.max_row+1):
    #Each row represents a census tract
    state  = sheet.cell(row, 2).value
    county = sheet.cell(row, 3).value
    pop = sheet.cell(row, 4).value

    counties_in_state[state].add(county)
    counter[county] += 1
    counter_pop[county] += pop

print("State","County", "Count", "Pop", sep="\t")
for state,county_set in counties_in_state.items():
    # Sort the counties in each state
    for county in sorted(county_set):
        print(state, county, counter[county], counter_pop[county], sep="\t")