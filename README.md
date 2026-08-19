# 💼 SócIA: Sua Parceira Financeira Inteligente

> Projeto desenvolvido como parte do laboratório "BIA do Futuro" da Digital Innovation One (DIO)[cite: 1]. 

A **SócIA** é uma assistente virtual de Inteligência Artificial focada em gestão financeira para micro e pequenos empreendedores. Diferente de chatbots genéricos, ela foi projetada com engenharia de prompt avançada para ler planilhas de vendas reais, calcular custos de rateio e ajudar na precificação de produtos de forma segura e contextualizada.

---

## 🚀 O Problema que Resolvemos

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

    ├── assets/                 # Imagens e mídias do projeto
    ├── data/                   # Arquivos CSV de exemplo e regras de negócio
    ├── docs/                   # Documentação, avaliação de métricas e pitch
    ├── examples/               # Exemplos de uso
    ├── src/                    # Código-fonte principal (Python/Streamlit)
    └── README.md               # Este arquivo

---

## 💻 Como Executar o Projeto

**Pré-requisitos:**
*   Python 3.8+ instalado.
*   Ollama instalado e rodando localmente com o modelo Llama 3 (ou compatível).

**Passo a passo:**

1.  Clone este repositório para a sua máquina.
2.  Instale as dependências necessárias no seu terminal:
    ```bash
    pip install streamlit pandas
    ```
3.  Navegue até a pasta onde está o arquivo principal do código (ex: `app.py`).
4.  Inicie a aplicação do Streamlit:
    ```bash
    streamlit run app.py
    ```
5.  Acesse o chat através do navegador (geralmente em `http://localhost:8501`) e comece a conversar com a SócIA!

---

## 📊 Avaliação e Métricas

O modelo passou por testes rigorosos de *benchmark*, focados em Assertividade, Segurança e Coerência. Os detalhes dos testes práticos e a evolução do prompt podem ser conferidos na pasta `/docs` deste repositório.
