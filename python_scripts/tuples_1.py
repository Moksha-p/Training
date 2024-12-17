def sort_add_tuples(tup1, tup2):
    tup = tup1 + tup2
    sorted_tup = sorted(tup)
    return tuple(sorted_tup)

if __name__ == "__main__":
    tup1 = (1, 3, 5)
    tup2 = (2, 4, 6)
    print(f"Sorted and combined tuples: {sort_add_tuples(tup1, tup2)}")