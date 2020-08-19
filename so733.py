from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        res =[]
        walk(image,(sr,sc),image[sr][sc],res,newColor)
        return image

def walk( image: List[List[int]], pos:tuple,flag:int,res:List[tuple],newColor:int) -> List[tuple] :
    if pos in res :
        return
    if image[pos[0]][pos[1]] == flag :
        res.append(pos)
        image[pos[0]][pos[1]] = newColor
        if pos[0] > 0 :
            walk(image,(pos[0]-1,pos[1]),flag,res,newColor)
        if pos[1] > 0 :
            walk(image,(pos[0],pos[1]-1),flag,res,newColor)
        if pos[0] < len(image) -1 :
            walk(image,(pos[0]+1,pos[1]),flag,res,newColor)
        if pos[1] < len(image[0]) -1 :
            walk(image,(pos[0],pos[1]+1),flag,res,newColor)
