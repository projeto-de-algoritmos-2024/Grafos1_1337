from typing import Optional

class TreeNode
    def __init__(self, val=0, left=None, right=None)
        self.val = val
        self.left = left
        self.right = right

class Solution
    def sumEvenGrandparent(self, raiz Optional[TreeNode]) - int
        def percorrer(no Optional[TreeNode], valor_pai int = -1, valor_avo int = -1) - int
            if not no
                return 0
                
      
            soma_atual = 0
            
            if valor_avo != -1 and valor_avo % 2 == 0
                soma_atual += no.val
                
         
            soma_atual += percorrer(no.left, no.val, valor_pai)
            soma_atual += percorrer(no.right, no.val, valor_pai)
            
            return soma_atual
            
        return percorrer(raiz)
