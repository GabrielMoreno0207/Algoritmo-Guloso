def selecao_atividades_guloso(atividades):

    atividades.sort(key=lambda x: x[1])
    
    atividades_selecionadas = [atividades[0]]  
    atividade_anterior = atividades[0]
    
    for atividade in atividades[1:]:
        if atividade[0] >= atividade_anterior[1]:
            atividades_selecionadas.append(atividade)
            atividade_anterior = atividade
    
    return atividades_selecionadas

atividades = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]

atividades_selecionadas = selecao_atividades_guloso(atividades)
print("Atividades selecionadas:")
for atividade in atividades_selecionadas:
    print(f"Atividade: Inicio {atividade[0]}, Termino {atividade[1]}")
