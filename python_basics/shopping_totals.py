# Food items (prices in US dollars):

apples = 2.69
coffee = 8.99
bread = 2.99
lettuce = 3.19
cheese = 6.89

nontaxable = apples + coffee + bread + lettuce + cheese
total_nontaxable = sum([nontaxable])
print("Total non-taxable: $" + str(total_nontaxable))

# Non-food items

pencils = 3.49
toothpaste = 3.89
shoelaces = 4.99
flowers = 7.99
soap = 1.29

taxable = pencils + toothpaste + shoelaces + flowers + soap
taxable_total = sum([taxable])
print("Total Taxable: $" + str(taxable_total))

tax_rate = .08

# Calculate the tax amount for taxable items
total_taxable_taxed = taxable_total * tax_rate

# Total tax and total cost of taxable items with tax.
taxable_with_tax = sum([taxable_total + total_taxable_taxed])
print("Tax: $" + str(round(total_taxable_taxed, 2)))
print("Total cost for taxable items with tax: $" +
      str(round(taxable_with_tax, 2)))

# Taxable items, tax, non taxable items total
total_cost = taxable_with_tax + total_nontaxable
print("Total cost of all items (including tax): $" + str(round(total_cost, 2)))

# Declare new tax rate
new_tax_rate = .09

# New tax rate with taxable items
new_total_cost = taxable_total * new_tax_rate
print("New tax rate total: $" + str(round(new_total_cost, 2)))
new_total_cost = new_total_cost + taxable_total + total_nontaxable
print("Total cost of all items with new tax rate: $" +
      str(round(new_total_cost, 2)))
