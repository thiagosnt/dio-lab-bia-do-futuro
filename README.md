# 💼 SócIA: Sua Parceira Financeira Inteligente

> Projeto desenvolvido como parte do laboratório "BIA do Futuro" da Digital Innovation One (DIO). 

A **SócIA** é uma assistente virtual de Inteligência Artificial focada em gestão financeira para micro e pequenos empreendedores. Diferente de chatbots genéricos, ela foi projetada com engenharia de prompt avançada para ler planilhas de vendas reais, calcular custos de rateio e ajudar na precificação de produtos de forma segura e contextualizada.

---

## 🚀 O Problema que Resolvido

Muitos pequenos empreendedores não possuem um analista financeiro e lutam para precificar produtos corretamente. Um erro no cálculo do frete ou na taxa da maquininha de cartão pode comprometer todo o lucro. A **SócIA** democratiza o acesso à análise de dados, oferecendo inteligência financeira através de uma interface de chat simples, operando de forma local e segura.

---

## ✨ Principais Funcionalidades

*   **Análise de Dados em CSV:** Capacidade de varrer dados tabulares para identificar histórico de vendas e receitas.
*   **Cálculo Estruturado (Chain of Thought):** A IA processa contas matemáticas, rateio de lotes e taxas de forma sequencial, garantindo alta precisão e evitando alucinações matemáticas.
*   **Memória de Contexto:** A aplicação retém o histórico das mensagens da sessão, permitindo conversas fluidas e cálculos contínuos sem que o usuário precise repetir valores.
*   **Guardrails Estritos (Blindagem de Escopo):** A SócIA possui travas de segurança rígidas. Ela é programada para recusar educadamente solicitações sobre impostos governamentais (IRPF, etc.) ou conselhos legais, orientando o usuário a buscar um contador.

---

## 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando uma arquitetura Full-Stack voltada para IA local:

*   **Python:** Linguagem base para a lógica de programação.
*   **Streamlit:** Framework utilizado para construir a interface web e gerenciar o estado da sessão (memória do chat).
*   **Ollama (Llama 3):** Motor do modelo de linguagem (LLM) rodando localmente, garantindo privacidade dos dados do usuário.
*   **Pandas:** Biblioteca para manipulação e estruturação da leitura dos arquivos CSV.

---

## 📂 Estrutura do Projeto

O repositório segue a estrutura padrão do laboratório[cite: 1]:

```text
├── assets/                 # Imagens e mídias do projeto
├── data/                   # Arquivos CSV de exemplo e regras de negócio
├── docs/                   # Documentação, avaliação de métricas e pitch
├── examples/               # Exemplos de uso
├── src/                    # Código-fonte principal (Python/Streamlit)
└── README.md               # Este arquivo
