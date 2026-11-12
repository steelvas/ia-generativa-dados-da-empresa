# Posso colar um contrato de cliente em uma IA?

Uma equipe quer resumir um contrato contendo dados pessoais e informações comerciais reservadas.

```python
documento = "contrato_de_cliente"
ferramenta_aprovada = False
fluxo_autorizado = False

if not ferramenta_aprovada or not fluxo_autorizado:
    print("Não enviar o documento")
else:
    print("Aplicar as restrições e registrar o uso")
```

1. **Código:** “a ferramenta funciona” não responde se ela pode receber aquele documento.
2. **Resultado:** o envio deve esperar a verificação da finalidade, das permissões, do fornecedor e dos controles disponíveis.
3. **Fundamento:** a LGPD exige finalidade, necessidade e segurança quando há dados pessoais. Sigilo contratual e segredos empresariais também podem estar envolvidos. **Usar IA com dados pessoais não é sempre proibido**; tampouco se deve presumir que todo serviço treina seu modelo com cada entrada.
4. **Decisão do gestor:** aprovar ferramentas e tipos de informação, verificar termos e configurações, definir quem pode usar o serviço e oferecer um caminho seguro para tarefas legítimas.

**Papel do advogado:** fazer a política interna descrever o fluxo real — qual dado é enviado, a quem, para quê e sob quais condições.

Fontes: [LGPD](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709compilado.htm) e [Guia de boas práticas de IA generativa do Governo Digital](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/publicacoes/guia-ia-generativa) — este último é orientação, não proibição geral para empresas privadas.

*Exemplo didático com dados fictícios. Não envia documentos a serviços externos.*
