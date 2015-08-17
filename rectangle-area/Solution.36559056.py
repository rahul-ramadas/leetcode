class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        x_overlap = max(0, min(C, G) - max(A, E))
        y_overlap = max(0, min(D, H) - max(B, F))
        
        overlap_area = x_overlap * y_overlap
        one_area = (C - A) * (D - B)
        two_area = (G - E) * (H - F)
        
        return one_area + two_area - overlap_area
