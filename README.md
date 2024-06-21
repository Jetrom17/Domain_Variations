# Geração de Variações de Domínios com Caracteres Especiais e Conversão para Punycode

![](https://i.imgur.com/HAWUDCx.png)

Este código em Python é uma ferramenta útil para gerar variações de um domínio com caracteres especiais, como acentos. Ele utiliza uma função recursiva chamada substituir_caracteres() para substituir cada caractere do domínio base pelas suas respectivas variações acentuadas. A função gerar_variacoes() utiliza essa função recursiva e retorna um conjunto de variações do domínio. Por fim, o módulo idna é usado para converter essas variações para Punycode, uma representação ASCII de nomes de domínio que podem conter caracteres Unicode.

```py
import idna
# Função para gerar variações com caracteres especiais
def gerar_variacoes(dominio_base):
    variacoes = set()
    substituicoes = {
        'a': ['á', 'à', 'â', 'ä'],
        'e': ['é', 'è', 'ê', 'ë'],
        'u': ['ú', 'ù', 'û', 'ü'],
        'n': ['ñ'],
    }
    
    def substituir_caracteres(dominio, pos):
        if pos >= len(dominio):
            return [dominio]
        
        variacoes_pos = []
        if dominio[pos] in substituicoes:
            for substituicao in substituicoes[dominio[pos]]:
                nova_variacao = dominio[:pos] + substituicao + dominio[pos+1:]
                variacoes_pos.extend(substituir_caracteres(nova_variacao, pos+1))
        variacoes_pos.extend(substituir_caracteres(dominio, pos+1))
        
        return variacoes_pos
    
    variacoes.update(substituir_caracteres(dominio_base, 0))
    return list(variacoes)
# Gerar as variações do domínio
dominio_base = "tabnews.com.br"
variacoes_dominio = gerar_variacoes(dominio_base)
# Converter para Punycode
dominios_punycode = [idna.encode(dominio).decode('ascii') for dominio in variacoes_dominio]
# Print das variações em Punycode
for dominio in dominios_punycode:
    print(dominio)

```
## Instalação
```
git clone https://github.com/Jetrom17/Domain_Variations
```
```
cd Domain_Variations
```
```
python3 dv.py
```
