'''
Title: 733. Flood Fill
Level: Easy
Link: https://leetcode.com/problems/flood-fill/
Author: Yuan
Date: 2022/07/05
'''

# dfs
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if image[sr][sc] == color:
            return image
        
        height = len(image)
        width = len(image[0])
        current_color = image[sr][sc] 
        
        def fill (sr, sc):
            if 0 <= sr < height and 0 <= sc < width and image[sr][sc] == current_color:
                image[sr][sc] = color

                fill(sr+1, sc)
                fill(sr-1, sc)
                fill(sr, sc+1)
                fill(sr, sc-1)      
        
        fill(sr, sc)
        
        return image