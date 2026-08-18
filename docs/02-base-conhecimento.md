# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Sim, os dados mockados originais foram totalmente substituídos e reestruturados para refletir a realidade da gestão diária de pequenos negócios e garantir a segurança do sistema.

Principais Modificações:

Exclusão de Dados de Investimentos: Arquivos como produtos_financeiros.json e perfil_investidor.json foram removidos intencionalmente da pasta data/. Como a instrução de sistema (System Prompt) proíbe a IA de dar dicas de investimentos, a remoção desses arquivos elimina o risco de alucinações e garante que a assistente não fuja do seu escopo.

Criação de Regras de Negócio (.md): Foram criados documentos de texto (regras_precificacao.md e boas_praticas_caixa.md) que atuam como o cérebro consultivo da SócIA. Eles contêm fórmulas matemáticas para cálculo de markup, margem de contribuição e diretrizes estritas sobre a separação de contas PF e PJ.

Tropicalização de Dados de Vendas (.csv): O arquivo de transações genéricas foi substituído pelo historico_vendas_exemplo.csv. Este dataset foi construído com dados sintéticos simulando o dia a dia de um comércio físico brasileiro. Foi adicionada a coluna crucial Meio_Pagamento (Pix, Cartão de Crédito, Débito) para que a IA consiga cruzar as vendas com tabelas de taxas e calcular o lucro líquido real do empreendedor.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos presentes na pasta `data/` são lidos localmente pelo backend da aplicação (desenvolvido em Python com Streamlit) no momento em que o sistema é inicializado. Para otimizar o processamento e o uso de memória, o conteúdo dos arquivos de texto (`.md`) é carregado e armazenado em variáveis estáticas da sessão. Já o arquivo tabular (`historico_vendas_exemplo.csv`) é processado utilizando a biblioteca Pandas, convertendo os dados sintéticos em um *dataframe* estruturado em memória, pronto para ser filtrado e consultado.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

A integração do conhecimento com o modelo (Ollama) ocorre em duas camadas distintas para evitar alucinações e sobrecarga de tokens:

1. **Injeção Estática (Regras e Diretrizes):** O conteúdo dos arquivos `regras_precificacao.md` e `boas_praticas_caixa.md` é injetado integralmente no *System Prompt* no momento em que a sessão é criada. Isso garante que a SócIA tenha as fórmulas financeiras, a persona e as travas de segurança operando como a base do seu "raciocínio" em todas as interações.
2. **Injeção Dinâmica (Dados de Vendas):** O histórico de transações (`.csv`) **não** é inserido inteiro no prompt. O sistema realiza uma consulta dinâmica: quando o usuário faz uma pergunta sobre faturamento ou vendas de um dia específico, o backend filtra o *dataframe* do Pandas e injeta no prompt apenas o recorte de dados relevante para aquela pergunta específica, fornecendo o contexto exato que a IA precisa para calcular a resposta sem estourar o limite de contexto do LLM local.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

baixo está um exemplo prático de como o backend monta o *prompt* final que é enviado para o modelo (Ollama) quando o usuário faz uma pergunta sobre as vendas do dia 01/10/2023. O sistema concatena as regras fixas com um recorte dinâmico dos dados:

```text
[SYSTEM]
Você é a SócIA, uma parceira financeira inteligente focada em ajudar pequenos empreendedores a gerenciar o fluxo de caixa...
(Regras de comportamento e limitações restritas aplicadas)

[BASE DE CONHECIMENTO - DIRETRIZES]
- Custo Total do Produto: Preço de custo + Frete + Embalagem.
- Margem de Contribuição: Preço de Venda - Custos Variáveis.
- Regra de Ouro: O dinheiro da empresa NÃO é o dinheiro do dono. A empresa deve ter uma conta bancária própria.

[CONTEXTO DE DADOS DINÂMICOS (Filtrado do histórico)]
Data,Produto,Categoria,Preco_Unitario,Quantidade,Receita_Total,Meio_Pagamento
2023-10-01,Café Expresso,Bebidas,6.50,2,13.00,Pix
2023-10-01,Pão de Queijo,Salgados,7.00,3,21.00,Cartao Debito
2023-10-01,Cappuccino,Bebidas,12.00,1,12.00,Cartao Credito a Vista

[USER]
SócIA, qual foi o total da nossa receita de vendas no dia primeiro de outubro e quanto recebemos de pagamentos via Pix?
