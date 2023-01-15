"""calculations with Python interpreter"""

from __future__ import division, print_function

def sphere_vol(radius):
    """computes volume of sphere"""
    vol_sphere = (4 / 3) * 3.14 * (radius ** 3)
    print("sphere volume:", f"{vol_sphere:.2f}", "units")

def whole_cost():
    """whole cost for book with
    cover price, discount percentage
    first, subsequent shipping and extra copies"""
    copies = 60
    cov_price = 24.95
    discount_pct = 40
    first_copy = 3
    extra_copy = 0.75
    all_discount = (cov_price * ((100 - discount_pct) / 100)) * copies
    all_ship = first_copy + (extra_copy * (copies - 1))
    cost = all_discount + all_ship
    print("wholesale cost:", f"${cost:.2f}")

def current_time():
    """current time if someone starts at 6:52 a.m.
    runs 2 miles at 8:15, 3 miles at 7:12"""
    start_hr, start_min = 6, 52
    start_time_sec = ((start_hr * 60) * 60) + (start_min * 60)
    min_ran = 8 + (7 * 3) + 8
    sec_ran = 15 + (12 * 3) + 15
    total_ran_sec = (min_ran * 60) + sec_ran
    end_time_sec = start_time_sec + total_ran_sec
    end_time = str((end_time_sec // 60) // 60) + ":" + str((end_time_sec // 60) % 60)
    print("end time:", end_time)

sphere_vol(5)
whole_cost()
current_time()
