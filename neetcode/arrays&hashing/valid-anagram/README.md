# Valid Anagram

Este exercício consiste em verificar se duas strings são **anagramas**, isto é, se possuem exatamente os mesmos caracteres com as mesmas quantidades, ainda que estejam em ordens diferentes.

## Primeira solução: ordenação

Inicialmente, pensei em ordenar as duas strings e comparar os resultados:

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```

### Raciocínio

Se duas palavras são anagramas, seus caracteres ficam na mesma sequência depois de ordenados.

Por exemplo:

```text
s = "anagram"  ->  sorted(s) = ['a', 'a', 'a', 'g', 'm', 'n', 'r']
t = "nagaram"  ->  sorted(t) = ['a', 'a', 'a', 'g', 'm', 'n', 'r']
```

Como as listas ordenadas são iguais, as strings são anagramas.

### Complexidade

- Tempo: `O(n log n)`, devido à ordenação dos caracteres.
- Espaço: `O(n)`, pois `sorted()` cria novas listas.

## Segunda solução: `Counter`

Depois, percebi que não era necessário ordenar as strings. Bastava contar quantas vezes cada caractere aparecia e comparar essas frequências:

```python
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
```

### Raciocínio

O `Counter` cria uma estrutura semelhante a um dicionário, na qual cada caractere é associado ao seu número de ocorrências.

Para `"anagram"` e `"nagaram"`, as duas contagens são equivalentes:

```python
Counter({'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1})
```

Assim, se os dois objetos `Counter` forem iguais, as strings possuem os mesmos caracteres nas mesmas quantidades e, portanto, são anagramas.

### Complexidade

- Tempo: `O(n)`, pois os caracteres das duas strings são percorridos para construir as contagens.
- Espaço: `O(k)`, sendo `k` a quantidade de caracteres distintos.

## Conclusão

A primeira solução é simples e intuitiva, mas depende da ordenação. A solução com `Counter` representa melhor o objetivo do problema: comparar diretamente a frequência dos caracteres. Além de deixar a intenção do código clara, ela reduz a complexidade de tempo de `O(n log n)` para `O(n)`.
