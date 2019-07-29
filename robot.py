def robot(n, dl):
    polozenie = (n* (n + 1) // 2 ) % (2 * dl + 2)
    if polozenie < dl + 1:
        return polozenie
    if polozenie == dl + 1:
        return polozenie - 1
    if polozenie < 2 * dl + 2:
        return 2 * dl + 1 - polozenie

    return 0 
