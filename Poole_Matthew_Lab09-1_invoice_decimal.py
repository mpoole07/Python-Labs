#!/usr/bin/env python3
#
# Matthew Poole, March 27, 2026, CPT127-424, Lab09-1
#
# Program: Invoice Program
# Purpose: Calculate the discount, subtotal, shipping cost, sales tax, and invoice total based on input of the order total
#
# Associated file(s): none

# Insert in the output student's name and exact date/time lab was run.
import datetime
print(f"Student Name: Matthew Poole")
labtime = datetime.datetime.now()
print(f"Lab Time: {labtime}")
print()

# import needed modules for decimal calculations, rounding, and locale
from decimal import Decimal
from decimal import ROUND_HALF_UP
import locale as lc

# display a title
print("The Invoice program")
print()

choice = "y"
while choice == "y":
    
    # get the user entry
    order_total = Decimal(input("Enter order total: "))
    order_total = order_total.quantize(Decimal("1.00"), ROUND_HALF_UP)
    print()               

    # determine the discount percent
    if order_total > 0 and order_total < 100:
        discount_percent = Decimal("0")
    elif order_total >= 100 and order_total < 250:
        discount_percent = Decimal(".1")
    elif order_total >= 250:
        discount_percent = Decimal(".2")

    # calculate the results
    discount = order_total * discount_percent
    discount = discount.quantize(Decimal("1.00"), ROUND_HALF_UP)                                
    subtotal = order_total - discount
    tax_percent = Decimal(".05")
    sales_tax = subtotal * tax_percent
    sales_tax = sales_tax.quantize(Decimal("1.00"), ROUND_HALF_UP)
    # calculate shipping cost
    shipping_rate = Decimal(".085")
    shipping_cost = subtotal * shipping_rate
    shipping_cost = shipping_cost.quantize(Decimal("1.00"), ROUND_HALF_UP)
    # calculate invoice total including the shipping cost
    invoice_total = subtotal + sales_tax + shipping_cost

    lc.setlocale(lc.LC_ALL, "us") # sets the currency locale to US

    # set variables for the formatting specifications
    s1 = ">10"
    s2 = "10"
    # display the results
    print(f"Order total:        {lc.currency(order_total, grouping=True):{s1}}")
    print(f"Discount amount:    {discount:{s2}}")
    print(f"Subtotal:           {subtotal:{s2}}")
    print(f"Shipping cost:      {shipping_cost:{s2}}")
    print(f"Sales tax:          {sales_tax:{s2}}")
    print(f"Invoice total:      {lc.currency(invoice_total, grouping=True):{s1}}")
    print()

    choice = input("Continue? (y/n): ")    
    print()
    
print("Bye!")
