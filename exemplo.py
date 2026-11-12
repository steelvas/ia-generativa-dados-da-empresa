"""Simulação didática. Não transmite documentos a ferramentas de IA."""

def decidir_envio(ferramenta_aprovada, fluxo_autorizado):
    if not ferramenta_aprovada or not fluxo_autorizado:
        return "NÃO ENVIAR: verificar ferramenta, dados e finalidade"
    return "PENDENTE: aplicar controles específicos e registrar o uso"


if __name__ == "__main__":
    print(decidir_envio(False, False))
    assert decidir_envio(False, True).startswith("NÃO ENVIAR")
    assert decidir_envio(True, True).startswith("PENDENTE")
