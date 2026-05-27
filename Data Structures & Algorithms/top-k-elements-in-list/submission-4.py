class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        res = []
        # Cree un mapa para meterlos y ver sus incidencias
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
        # Sorted los valores basados en la tupla item[1], siendo key 0 y el valor 1 de la tupla
        # luego los reversee para obtener de mayor a menor
        map = {k: v for k, v in sorted(map.items(), key=lambda item: item[1], reverse=True)}

        # Así usar "k" en un ciclo, así solo darme los valores necesarios, 
        # Ejemplo "2" me da los mayores 2      
        
        for i,key in enumerate(map):
            if i >= k: break
            res.append(key)
            
        return res
        
        