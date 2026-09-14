class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        contagem = {}
        operacoes = 0
        
        for x in nums:
            complemento = k - x
            if contagem.get(complemento, 0) > 0:
                operacoes += 1
                contagem[complemento] -= 1
            else:
                contagem[x] = contagem.get(x, 0) + 1
        
        return operacoes