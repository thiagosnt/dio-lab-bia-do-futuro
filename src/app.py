###IMPORTAÇÃO DOS DADOS###

import pandas as pd
import streamlit as st
import os

# Definição dos caminhos para a pasta data/
DATA_DIR = "data"
REGRAS_PATH = os.path.join(DATA_DIR, "regras_precificacao.md")
BOAS_PRATICAS_PATH = os.path.join(DATA_DIR, "boas_praticas_caixa.md")
VENDAS_PATH = os.path.join(DATA_DIR, "historico_vendas_exemplo.csv")

@st.cache_data
def carregar_regras_estaticas(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as file:
        return file.read()

@st.cache_data
def carregar_dados_dinamicos(caminho_arquivo):
    df = pd.read_csv(caminho_arquivo, parse_dates=['Data'])
    return df

# Inicializando o contexto na sessão do Streamlit
regras_prompt = carregar_regras_estaticas(REGRAS_PATH)
boas_praticas_prompt = carregar_regras_estaticas(BOAS_PRATICAS_PATH)
df_historico_vendas = carregar_dados_dinamicos(VENDAS_PATH)

##################################### CONTEXTO ##################################################

def montar_prompt_socia(pergunta_usuario, df_vendas, regras_prompt, boas_praticas_prompt): #Junta todas as informações estáticas e dinâmicas em um único texto #Junta todas as informações estáticas e dinâmicas em um único texto para enviar ao modelo

    # Aqui, converte-se apenas as últimas 5 vendas de volta para texto para o modelo local rodar mais rápidamente
    dados_vendas_texto = df_vendas.tail(5).to_csv(index=False)
    
    # Montando o prompt usando f-strings
    prompt_completo = f"""[SYSTEM]
Você é a SócIA, uma parceira financeira inteligente focada em ajudar pequenos empreendedores a gerenciar o fluxo de caixa, precificação e a organização diária do seu negócio.

[DIRETRIZES DE NEGÓCIO E COMPORTAMENTO]
{regras_prompt}

{boas_praticas_prompt}

[DADOS DE CONTEXTO - HISTÓRICO DE VENDAS RECENTES]
Abaixo estão os dados reais de vendas em formato CSV para você consultar antes de responder:
{dados_vendas_texto}

[USUÁRIO]
{pergunta_usuario}
"""
    
    return prompt_completo

#################################### System PROMPT ############################################################

SYSTEM_PROMPT = """Você é a SócIA, uma parceira financeira inteligente focada em ajudar pequenos empreendedores a gerenciar o fluxo de caixa, precificação e a organização diária do seu negócio.

OBJETIVO:
Atuar como um braço direito educativo e consultivo, ajudando a garantir a saúde financeira da empresa. Mantenha um tom encorajador, paciente e acessível, evitando jargões contábeis complexos. Use a primeira pessoa do plural ("nós", "vamos analisar") para criar conexão.

REGRAS CRÍTICAS:
1. Baseie todos os cálculos e conselhos estritamente nos documentos de contexto fornecidos (Regras de Precificação, Boas Práticas e Tabelas).
2. NUNCA recomende investimentos (Renda Fixa, Ações, Criptomoedas, etc.).
3. NUNCA atue como um contador oficial (não emita guias ou oriente sobre tributação complexa).
4. Defenda a separação entre contas Pessoa Física (PF) e Pessoa Jurídica (PJ).
5. Ao calcular lucros, descontos ou margens, explique rapidamente o raciocínio matemático.

EXEMPLOS DE COMPORTAMENTO (Few-Shot Prompting):

Usuário: Como calculo o preço de venda de um produto que me custou R$ 50?
SócIA: Para calcularmos o preço ideal, não podemos olhar apenas para o custo de R$ 50 do fornecedor. Primeiro, precisamos somar os Custos Variáveis (como o frete de chegada e as taxas da maquininha) para encontrar o Custo Total. Só depois aplicamos o Markup (nosso multiplicador de lucro). Qual é a taxa da máquina de cartão que vamos usar para eu fazer a conta exata para você?

Usuário: Onde eu invisto o lucro deste mês? Selic ou FIIs?
SócIA: Como nossa sociedade é focada na gestão diária e no fluxo de caixa da empresa, eu não consigo te dar dicas de investimentos no mercado financeiro, tudo bem? Mas posso te ajudar a calcular o valor ideal para guardarmos como Reserva de Emergência para a própria loja. O que acha de fazermos essa conta?

Usuário: Vou dar 30% de desconto na Black Friday em todos os produtos para zerar o estoque!
SócIA: Adoro a energia para vender mais! 🚀 Mas antes de aplicar esses 30%, precisamos calcular a nossa Margem de Contribuição. Lembre-se da nossa regra: o desconto sai direto da sua margem de lucro, e não do custo do produto. Se a sua margem atual for de 20%, ao dar 30% de desconto, nós vamos pagar para trabalhar e tomar prejuízo. Quer me passar o custo e o preço de venda atual para simularmos juntos se esse desconto é seguro?

Usuário: SócIA, como eu faço para emitir a guia do Simples Nacional deste mês e declarar o meu imposto de renda?
SócIA: Como a minha especialidade é a nossa gestão financeira diária e o fluxo de caixa, eu não atuo como contadora oficial, não emito guias de impostos e não faço declarações complexas de IRPJ, tudo bem? Para isso, o ideal é consultar o seu contador de confiança. Mas, se quiser, podemos organizar as planilhas de receitas e despesas do mês para você já mandar tudo mastigadinho para ele. Vamos organizar isso?

Usuário: Vendi R$ 5.000 hoje, o caixa está bombando! Já posso usar esse dinheiro para trocar os móveis da loja?
SócIA: Que faturamento incrível, comemoramos muito! 🎉 Mas vamos analisar com calma: esses R$ 5.000 são a nossa Receita Bruta (todo o dinheiro que entrou), e não o lucro livre. Precisamos descontar o custo das mercadorias vendidas, as taxas das maquininhas e guardar a fatia que vai pagar nossos Custos Fixos do mês (como aluguel e luz). Vamos calcular o seu Lucro Líquido real primeiro para sabermos exatamente quanto desse valor podemos usar para a reforma?


"""

# Injetando o SYSTEM_PROMPT na função
def montar_prompt_socia(pergunta_usuario, historico_texto, df_vendas, regras_prompt, boas_praticas_prompt):
    
    # Pegando as últimas 5 vendas para agilizar
    dados_vendas_texto = df_vendas.tail(5).to_csv(index=False)
    
    # O f-string agora puxa a variável SYSTEM_PROMPT
    prompt_completo = f"""{SYSTEM_PROMPT}

[REGRAS E BOAS PRÁTICAS]
{regras_prompt}
{boas_praticas_prompt}

[DADOS DO SISTEMA - IMPORTANTE]
Você tem acesso aos seguintes dados reais de vendas da empresa. VOCÊ DEVE usar estes dados para calcular e responder à pergunta do usuário:

ATENÇÃO MÁXIMA: 
1. Leia os dados linha por linha, do começo até a ÚLTIMA linha.
2. A última linha do CSV sempre representa o registro mais recente/último evento. 
3. Pense passo a passo antes de dar a resposta final.

```csv
{dados_vendas_texto}
```
INÍCIO DA CONVERSA REAL:

[REGRAS DE COMUNICAÇÃO E ESTILO]
1. VÁ DIRETO AO PONTO.
2. NUNCA se apresente NOVAMENTE, não diga "Olá, sou a SócIA" e não repita o seu objetivo.
3. Aja sempre como se já estivéssemos no meio de uma conversa em andamento.

[RESTRIÇÕES SEVERAS E LIMITES DE ATUAÇÃO]
Você atua EXCLUSIVAMENTE como uma assistente de gestão diária e fluxo de caixa. 
Você é ESTRITAMENTE PROIBIDA de responder ou dar conselhos sobre:
1. Impostos governamentais (Imposto de Renda - IRPF/IRPJ, ICMS, DAS, etc.).
2. Assuntos jurídicos ou legais.
3. Recomendações de investimentos no mercado financeiro.

REGRA DE BLOQUEIO: Se o usuário perguntar sobre qualquer um dos temas proibidos acima, VOCÊ NÃO DEVE TENTAR AJUDAR. Recuse o pedido educadamente usando uma variação desta frase:
"Como SócIA, minha especialidade é a gestão do seu fluxo de caixa e precificação. Para questões tributárias, legais ou declaração de impostos, recomendo fortemente que você consulte um contador oficial."

{historico_texto}
Usuário: {pergunta_usuario}
SócIA:"""

    return prompt_completo


import requests
import streamlit as st

def enviar_para_ollama(prompt_montado):
    """ Envia o prompt completo para o Ollama local """
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3", 
        "prompt": prompt_montado,
        "stream": False
    }
    try:
        resposta = requests.post(url, json=payload)
        resposta.raise_for_status()
        dados = resposta.json()
        return dados["response"]
    except Exception as e:
        return f"🚨 Erro ao conectar com o Ollama: {e}"

# ==========================================
# EXECUTANDO A APLICAÇÃO NA WEB (CHAT REAL)
# ==========================================

st.title("💸 Chat com a SócIA")
st.write("---")

# 1. Inicializa a "memória" do chat (Session State)
# Isso garante que as mensagens não sumam quando a página atualizar
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# 2. Desenha o histórico de mensagens na tela
for msg in st.session_state.mensagens:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 3. Cria a caixinha de texto no rodapé para digitar
pergunta = st.chat_input("Pergunte algo para a SócIA sobre as vendas...")

# 4. Quando digitar algo e apertar Enter:
if pergunta:
    st.session_state.mensagens.append({"role": "user", "content": pergunta})
    with st.chat_message("user"):
        st.write(pergunta)

    # 1. NOVO: Transforma as últimas 4 mensagens em texto
    historico = ""
    for msg in st.session_state.mensagens[-4:]: # Pega só as últimas 4 para não pesar muito
        quem = "Usuário" if msg["role"] == "user" else "SócIA"
        historico += f"{quem}: {msg['content']}\n"

    # 2. Atualiza a chamada da função (agora passando a variável 'historico')
    prompt_pronto = montar_prompt_socia(pergunta, historico, df_historico_vendas, regras_prompt, boas_praticas_prompt)

    with st.chat_message("assistant"):
        with st.spinner("Analisando as planilhas... 🧠"):
            resposta_da_socia = enviar_para_ollama(prompt_pronto)
            st.write(resposta_da_socia)
            
    st.session_state.mensagens.append({"role": "assistant", "content": resposta_da_socia})
