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
