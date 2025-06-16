import requests

BASE_URL = "https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena"

def _extrair_dezenas(dados_json):
    """Tenta extrair as dezenas sorteadas de diferentes campos possíveis."""
    for campo in ("listaDezenas", "dezenas", "dezenasSorteadasOrdemSorteio"):
        dezenas = dados_json.get(campo)
        if dezenas:
            return sorted(int(d) for d in dezenas)
    raise ValueError("Não foi possível extrair as dezenas do JSON")

def obter_concurso(numero: int = None):
    """Obtém o número do concurso e as dezenas sorteadas."""
    url = f"{BASE_URL}/{numero}" if numero else BASE_URL
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    dados = resp.json()

    numero_concurso = (
        dados.get("numero") or
        dados.get("numeroDoConcurso") or
        dados.get("concurso") or
        dados.get("idConcurso") or
        numero
    )

    dezenas = _extrair_dezenas(dados)
    return int(numero_concurso), dezenas

def ler_dezenas_usuario(qtd: int = 6):
    """Lê 'qtd' dezenas únicas entre 1 e 60 digitadas pelo usuário."""
    escolhidas = set()
    while len(escolhidas) < qtd:
        try:
            falta = qtd - len(escolhidas)
            n = int(input(f"Digite um número entre 1 e 60 ({falta} restante): ").strip())
            if not 1 <= n <= 60:
                print("Número fora do intervalo.")
            elif n in escolhidas:
                print("Número repetido.")
            else:
                escolhidas.add(n)
        except ValueError:
            print("Entrada inválida.")
    return sorted(escolhidas)

def formatar_lista(lst):
    return ", ".join(f"{n:02d}" for n in sorted(lst))

def main():
    # 1. Lê os números do usuário
    numeros_usuario = ler_dezenas_usuario()

    # 2. Concurso mais recente
    try:
        concurso_atual, dezenas_atual = obter_concurso()
    except Exception as e:
        print(f"Erro ao acessar o concurso atual: {e}")
        return

    # 3. Lista de concursos a pesquisar: atual + 20 anteriores
    concursos = []
    for i in range(0, 31):  # inclui o atual
        numero = concurso_atual - i
        try:
            num, dezenas = obter_concurso(numero)
            acertos = set(numeros_usuario) & set(dezenas)
            concursos.append({
                "numero": num,
                "dezenas": dezenas,
                "acertos": sorted(acertos)
            })
        except Exception as e:
            print(f"Erro ao acessar o concurso {numero}: {e}")

    # 4. Exibe resultados detalhados
    print("\n=== RESULTADOS ===")
    for c in sorted(concursos, key=lambda x: x["numero"], reverse=True):
        dezenas_str = formatar_lista(c["dezenas"])
        acertos_str = formatar_lista(c["acertos"])
        print(f"Concurso {c['numero']}: {dezenas_str} → Acertos: {len(c['acertos'])}", end='')
        if c["acertos"]:
            print(f" ({acertos_str})")
        else:
            print("")

if __name__ == "__main__":
    main()
