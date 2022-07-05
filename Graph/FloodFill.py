'''
Title: 733. Flood Fill
Level: Easy
Link: https://leetcode.com/problems/flood-fill/
Author: Yuan
Date: 2022/07/05
'''

# dfs
class Solution1:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if image == None or image[sr][sc] == color:
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

class Solution2:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if image == None or image[sr][sc] == color:
            return image
        
        self.fill(sr, sc, image, image[sr][sc], color)
        
        return image
        
    def fill (self, sr, sc, image, current_color, color):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != current_color:
            return

        image[sr][sc] = color
        self.fill(sr+1, sc, image, current_color, color)
        self.fill(sr-1, sc, image, current_color, color)
        self.fill(sr, sc+1, image, current_color, color)
        self.fill(sr, sc-1, image, current_color, color)              