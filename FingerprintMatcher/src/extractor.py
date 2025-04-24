class MinutiaeExtractor:
    """
    Ekstrakcja minutii metodą Crossing Number:
    CN = (# zmian między sąsiadami) / 2
    CN=1 → zakończenie; CN=3 → rozwidlenie
    """
    @staticmethod
    def extract_minutiae(skel_image):
        minutiae = []
        rows, cols = skel_image.shape
        neighbors = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

        for i in range(1, rows-1):
            for j in range(1, cols-1):
                if skel_image[i, j] == 255:
                    vals = [
                        1 if skel_image[i+dx, j+dy] == 255 else 0
                        for dx, dy in neighbors
                    ]
                    vals_cycle = vals + [vals[0]]
                    transitions = sum(
                        abs(vals_cycle[k] - vals_cycle[k+1]) for k in range(8)
                    )
                    cn = transitions / 2
                    if cn == 1:
                        minutiae.append({'type': 'ending', 'pt': (j, i)})
                    elif cn == 3:
                        minutiae.append({'type': 'bifurcation', 'pt': (j, i)})
        return minutiae
