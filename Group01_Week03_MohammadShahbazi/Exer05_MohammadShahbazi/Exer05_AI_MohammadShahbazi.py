# Budget in million Tomans
budget = 122

# Component list in order: (name, quantity_needed_per_PC, unit_price)
components = [
    ("MotherBoard", 1,25),
    ("CPU", 1, 35),
    ("RAM", 4, 10),
    ("Hard", 2, 12),
    ("Case", 1, 8),
    ("Fan", 1, 18)
]

# Initialize tracking
purchased = {}
total_spent = 0
remaining_budget = budget

# Purchase in order
for name, qty_needed, price in components:
    # Maximum we can afford
    max_affordable = remaining_budget // price
    # We need 'qty_needed' per PC, but here we buy sequentially until we can't complete a full set
    # Actually: we keep buying this component until we can't afford another full set for current PC?
    # The problem says: buy required quantity if possible, else move to next component with leftover money.
    
    # For simplicity: If we can't buy even one piece, stop buying this component.
    if max_affordable < 1:
        continue
    
    # Buy as many as possible, but not more than needed for current PC? 
    # Actually, we keep buying until money runs out for this component.
    # Let's buy the needed quantity if possible, else buy what we can.
    to_buy = min(qty_needed, max_affordable)  # We buy either needed qty or what we can afford
    
    if to_buy > 0:
        cost = to_buy * price
        if cost > remaining_budget:
            break  # shouldn't happen due to max_affordable check
        
        # Record purchase
        purchased[name] = purchased.get(name, 0) + to_buy
        total_spent += cost
        remaining_budget -= cost

# Calculate total items bought
total_items = sum(purchased.values())

# Calculate shortfall for incomplete components
shortfall = 0
for name, qty_needed, price in components:
    bought_qty = purchased.get(name, 0)
    if bought_qty < qty_needed:
        shortfall += (qty_needed - bought_qty) * price

# Print results
print("1. Purchased components list:", purchased)
print("2. Quantity of each purchased component:", purchased)
print("3. Total number of purchased components:", total_items)
print("4. Total amount spent (million Tomans):", total_spent)
print("5. Remaining budget (million Tomans):", remaining_budget)
print("6. Extra budget needed to complete remaining items (million Tomans):", shortfall)