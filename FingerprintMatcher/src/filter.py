import math

class MinutiaeFilter:
    """
    - Odfiltrowuje minutie blisko krawędzi (margin)
    - Usuwa duplikaty w odległości < distance_thresh
    """
    @staticmethod
    def remove_false_minutiae(min_list, image_shape,
                              margin=10, distance_thresh=8):
        rows, cols = image_shape
        filtered = [
            m for m in min_list
            if margin < m['pt'][0] < cols - margin
            and margin < m['pt'][1] < rows - margin
        ]
        final = []
        for m in filtered:
            dup = False
            for f in final:
                if m['type'] == f['type']:
                    dx = m['pt'][0] - f['pt'][0]
                    dy = m['pt'][1] - f['pt'][1]
                    if math.hypot(dx, dy) < distance_thresh:
                        dup = True
                        break
            if not dup:
                final.append(m)
        return final
