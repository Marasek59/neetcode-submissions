class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Spočítáme výskyty každého čísla -> O(n)
        pocty = {}
        for cislo in nums:
            pocty[cislo] = pocty.get(cislo, 0) + 1

    # 2. Vytvoříme přihrádky (index = počet opakování) -> O(n)
    # Délka je len(nums) + 1, protože indexujeme od 0 a max počet je len(nums)
        prihradky = [[] for _ in range(len(nums) + 1)]
    
        for cislo, pocet in pocty.items():
            prihradky[pocet].append(cislo)

        # 3. Projdeme přihrádky odzadu (od nejčastějších) -> O(n)
        vysledek = []
        # range(start, stop, krok) -> jdeme od posledního indexu až k 1
        for i in range(len(prihradky) - 1, 0, -1):
            for cislo in prihradky[i]:
                vysledek.append(cislo)
                if len(vysledek) == k:
                    return vysledek
