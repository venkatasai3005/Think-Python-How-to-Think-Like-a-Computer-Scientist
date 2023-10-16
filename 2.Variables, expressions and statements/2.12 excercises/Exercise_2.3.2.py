cover_price=24.95
discount=0.4
shipping_cost_first_copy=3
shipping_cost_additional_copy=0.75
total_copies=60

books_cost=total_copies*cover_price*(1-discount)
shipping_cost=shipping_cost_first_copy+(total_copies-1)*shipping_cost_additional_copy
total=books_cost+shipping_cost
print(total)


#output 945.4499999999999
