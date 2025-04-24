import math

class Verifier:
    """
    - Paruje minutie tego samego typu w promieniu match_threshold
    - similarity = (#par) / max(#min1,#min2) * 100%
    - decyzja TAK/NIE wg similarity_threshold
    """
    def __init__(self, match_threshold=15, similarity_threshold=50):
        self.match_thresh = match_threshold
        self.sim_thresh = similarity_threshold

    def match_minutiae(self, l1, l2):
        matched, used = [], set()
        for m1 in l1:
            for idx, m2 in enumerate(l2):
                if idx in used: continue
                if m1['type'] == m2['type']:
                    dx = m1['pt'][0] - m2['pt'][0]
                    dy = m1['pt'][1] - m2['pt'][1]
                    if math.hypot(dx, dy) < self.match_thresh:
                        matched.append((m1, m2))
                        used.add(idx)
                        break
        return matched

    def verify(self, l1, l2):
        matched = self.match_minutiae(l1, l2)
        m_count = len(matched)
        denom = max(len(l1), len(l2)) if l1 and l2 else 1
        similarity = m_count / denom * 100
        decision = "TAK" if similarity >= self.sim_thresh else "NIE"
        return similarity, decision
