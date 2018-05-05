
def taxCalc(stat='', Income=100):
    taxDir={'SA':5, 'NJ':6, 'FF':9}
    FdTax=10
    stateTax=taxDir[stat]
    totalTaxParcent=FdTax+stateTax
    IncomeAfterTax=Income - (Income*(totalTaxParcent/100))
    print("Income after tax deduction = " + str(IncomeAfterTax))

taxCalc('SA', 100000)

