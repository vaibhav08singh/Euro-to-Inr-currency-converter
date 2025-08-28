def converter(euro_val):
    inr_val = euro_val * 102.34 
    print(euro_val, "euro =", inr_val,"inr")

print("Enter the amount in euro to convert to inr:")
euro_amount = float(input())
converter(euro_amount)