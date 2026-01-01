def convert_lbs_to_kg(lbs):
    kgs = lbs * 0.453592
    return f"{lbs} {'pound' if lbs == 1 else 'pounds'} equals {kgs:.2f} {'kilogram' if round(kgs,2) == 1.00 else 'kilograms'}."