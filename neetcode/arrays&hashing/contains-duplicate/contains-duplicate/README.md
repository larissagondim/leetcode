# Contains Duplicate

Este exercício consiste em verificar se uma lista de números inteiros possui algum valor repetido.

## Primeira solução: dicionário de frequências

Minha primeira ideia foi utilizar um dicionário para armazenar a frequência de cada número da lista.

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isDouble = False
        frequencia = {}

        for num in nums:
            frequencia[num] = frequencia.get(num, 0) + 1

            if frequencia[num] > 1:
                isDouble = True
                break

        return isDouble
```

O raciocínio foi percorrer a lista e, para cada número, aumentar sua contagem no dicionário. O método `get(num, 0)` retorna a frequência atual do número ou `0` caso ele ainda não tenha sido inserido.

Assim que a frequência de algum número se torna maior que `1`, sabemos que existe uma duplicata. Nesse momento, o laço é interrompido e a função retorna `True`.

Essa solução funciona corretamente, mas armazena uma informação além do necessário: a quantidade de vezes que cada número apareceu. Para resolver o problema, precisamos saber apenas se o número já apareceu ou não.

## Segunda solução: conjunto de valores únicos

Depois, percebi que poderia utilizar um `set`. Em Python, um conjunto não permite elementos duplicados. Portanto, ao transformar a lista em um conjunto, todas as repetições são removidas.

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set(nums)
        return len(unique) != len(nums)
```

Se a quantidade de elementos do conjunto for diferente da quantidade de elementos da lista original, significa que pelo menos um valor foi removido por estar repetido. Nesse caso, a função retorna `True`.

Exemplo:

```python
nums = [1, 2, 3, 1]
unique = {1, 2, 3}

len(nums)    # 4
len(unique)  # 3
```

Como os tamanhos são diferentes, a lista possui uma duplicata.

## Comparação

| Solução | Tempo médio | Espaço adicional | Característica |
| --- | --- | --- | --- |
| Dicionário de frequências | `O(n)` | `O(n)` | Pode parar assim que encontra uma duplicata |
| Conjunto criado com `set(nums)` | `O(n)` | `O(n)` | Mais curta e expressa diretamente a ideia de valores únicos |

## Conclusão

As duas soluções possuem a mesma complexidade assintótica e resolvem corretamente o problema. No entanto, a solução com `set` é mais simples e legível, pois utiliza diretamente a propriedade de que conjuntos não armazenam elementos repetidos.

Por isso, depois de analisar a primeira abordagem, escolhi a segunda como solução final.
