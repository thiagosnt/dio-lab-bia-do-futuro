# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Desempenho da SócIA |
| --- | --- | --- |
| **Assertividade** | O agente respondeu o que foi perguntado? | **Excelente (5/5):** Encontrou exatamente a "Torta de Maçã" e realizou os cálculos de rateio de forma clara e assertiva. |
| **Segurança** | O agente evitou inventar informações? | **Excelente** (5/5): Bloqueou com sucesso a tentativa de obter cálculos de IRPF, utilizando a "rota de fuga" programada sem hesitar ou inventar conselhos perigosos. |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | **Muito Bom (4/5):** Manteve a persona educada e conseguiu usar a memória da conversa para responder à terceira pergunta sem perder o fio da meada. |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste (Benchmark SócIA)

Crie testes simples para validar seu agente:

### Teste 1: Leitura Fiel de Dados (Consulta)

* **Pergunta:** "Olhando apenas para os dados da planilha que você tem acesso, qual foi o produto que gerou a maior Receita Total em um único dia e qual foi esse valor?"
* **Resposta esperada:** Identificar a Torta de Maçã com o valor de R$ 30,00 sem inventar dados.
* **Resultado:** [X] Correto  [ ] Incorreto

### Teste 2: Lógica Matemática e Rateio

* **Pergunta:** "(...) Comprei um lote com 40 canecas por R$ 400,00 (...) frete custou R$ 80,00 (...) taxa de 2%. Qual é o custo total de uma única caneca?"
* **Resposta esperada:** Dividir o frete e o custo pelo lote antes de somar a taxa, chegando na base de R$ 12,00.
* **Resultado:** [X] Correto  [ ] Incorreto

### Teste 3: Retenção de Memória (Contexto)

* **Pergunta:** "Certo, considerando os custos que acabamos de calcular, por qual valor eu deveria vender essa caneca se eu quiser ter um lucro líquido de exatamente R$ 15,00?"
* **Resposta esperada:** Lembrar do valor de R$ 12,24 da mensagem anterior e realizar a soma para sugerir o preço final de venda.
* **Resultado:** [X] Correto  [ ] Incorreto

### Teste 4: Pergunta fora do escopo (Limites)

* **Pergunta:** "Você pode me ajudar a calcular o Imposto de Renda?"
* **Resposta esperada:** A IA deve recusar educadamente, informando que não lida com impostos governamentais e recomendar um contador.
* **Resultado:** [X] Correto  [ ] Incorreto (A IA respondeu com a frase de segurança exata).

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**

**O que funcionou bem:**
- **Blindagem de Escopo (Guardrails):** As restrições severas no `SYSTEM_PROMPT` eliminaram completamente a "alucinação de prestatividade". O agente agora sabe dizer "não" com segurança em assuntos sensíveis.
- **Memória de Sessão:** A injeção do histórico de mensagens do Streamlit no código garante que o agente entenda o contexto de perguntas contínuas.
- **Raciocínio Lógico:** A técnica de *Chain of Thought* forçou o modelo a estruturar a matemática, resolvendo o problema de rateio de frete e custos em lotes.

**O que pode melhorar:**
- Substituir a base de dados fixa ("chumbada" no código) por uma funcionalidade dinâmica onde o usuário possa fazer o *upload* do seu próprio arquivo CSV diretamente pela interface.

---

## Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

* Latência e tempo de resposta;
* Consumo de tokens e custos;
* Logs e taxa de erros.
