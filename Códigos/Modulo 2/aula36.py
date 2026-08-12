# Exercício - sistema de perguntas e respostas


perguntas = {
    "Pergunta 1": {
        "pergunta": "Quanto é 2 + 2?",
        "respostas": {"a": "1", "b": "4", "c": "5", "d": "3"},
        "resposta_certa": "b",
    },
    "Pergunta 2": {
        "pergunta": "Quanto é 5 * 5?",
        "respostas": {"a": "10", "b": "15", "c": "25", "d": "20"},
        "resposta_certa": "c",
    },
    "Pergunta 3": {
        "pergunta": "Quanto é 10 / 2?",
        "respostas": {"a": "2", "b": "5", "c": "10", "d": "20"},
        "resposta_certa": "b",
    },
}

contador_acertos = 0

for chave, info in perguntas.items():
    print(f"{chave}: {info['pergunta']}")
    for opcao, texto in info["respostas"].items():
        print(f"[{opcao}] {texto}")
    escolha = input("Escolha uma alternativa: ").strip().lower()
    if escolha == info["resposta_certa"]:
        print("Resposta correta!")
        contador_acertos += 1
    else:
        print("Resposta incorreta!")

print(f"Você acertou {contador_acertos} de {len(perguntas)} perguntas.")
