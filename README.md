# Voomi — Clone 100% Fiel & Idêntico (voomi.app.br)

Este projeto é uma reconstrução **100% fiel, idêntica e completa** da plataforma oficial da **Voomi** (`https://voomi.app.br`), incluindo **tanto a Landing Page comercial quanto toda a aplicação SaaS interna autenticada**.

---

## 🌟 O Que Foi Recriado

### 1. Aplicação SaaS Interna Completa (20+ Telas)
- **Dashboard Operacional (`/dashboard`)**:
  - 4 Cards de métricas principais (Faturamento Total, Pedidos, Comissão, Ticket Médio).
  - Gráfico dinâmico de vendas ao longo do tempo.
  - Tabela de pedidos e produtos minerados com status e comissões.
  - **Simulador "Caixa Registradora" ao vivo**: Dispara notificações reais de vendas no canto da tela, com efeitos sonoros originais locais (`money.mp3`, `cash.mp3`, `coin.mp3`) e chuva de confetes (`canvas-confetti`).
  - Saldo de créditos ao vivo: **1.925 créditos** carregados do perfil autenticado.
- **Radar de Produtos 2.0 (`/radar-2.0`)**:
  - Catálogo completo de mais de 50 produtos minerados do TikTok Shop via FastMoss.
  - Filtros por nicho (Beleza, Saúde, Casa, Moda, Eletrônicos), ordenação por vendas, trending score, margem de lucro e rating de fornecedores.
  - Visualização de imagem com fundo removido (`image_no_bg`) e botão **"Criar com este produto"**.
- **Creator Lab (`/videos-ia` e `/videos-ia-v2`)**:
  - Wizard guiado em 4 etapas:
    1. *Cenário*: Escolha do ambiente do vídeo.
    2. *Produto*: Seleção do item minerado do radar ou upload customizado.
    3. *Avatar*: Escolha do influenciador de IA (incluindo o avatar customizado do usuário).
    4. *Movimento & Fala*: Prompt de movimentação, sincronização labial e geração de vídeo.
- **Motion Lab (`/clonagem-movimentos`)**:
  - Catálogo de 63 templates de movimentos, danças virais do TikTok e demonstrações de produtos (`movement_templates`), com vídeos e previews funcionais.
- **Personalize IA (`/personalize-ia`)**:
  - Gerenciador de avatares próprios e mãos em primeira pessoa (POV hands) para segurar produtos.
- **Viral Boost (`/videos-virais`)**:
  - Análise de ganchos virais e criativos de alta retenção.
- **Lab Studio (`/editor-videos`)**:
  - Editor de vídeo integrado com linha do tempo para montagem de criativos e overlays.
- **Lab Academy / Tutoriais (`/tutoriais`)**:
  - Aulas em vídeo com integração oficial do player PandaVideo, divisão por módulos e controle de progresso.
- **Minhas Mídias / Meus Prompts (`/meus-prompts`)**:
  - Histórico de criativos gerados, vídeos renderizados e biblioteca de prompts salvos.
- **Lab Store (`/lab-store`)**:
  - Vitrine de produtos físicos e digitais para afiliação.
- **Comunidade Spy (`/comunidade-spy`)**:
  - Acesso à comunidade exclusiva de afiliados e criadores.
- **Indique & Ganhe (`/indique-ganhe`)**:
  - Programa de afiliados oficial, link exclusivo, saldo de comissões e métricas de cliques.
- **Novidades / Releases (`/novidades`)**:
  - Linha do tempo com as últimas atualizações de modelos e ferramentas da Voomi.
- **Perfil & Configurações (`/perfil`)**:
  - Dados cadastrais do Matheus Moreira (`papan`), alteração de senha, preferências da Caixa Registradora (intervalo de disparo, escolha de som `money`/`cash`/`coin`, seleção de produtos) e histórico de créditos.
- **Painel Administrativo (`/admin/*`)**:
  - Módulos de Visão Geral, Financeiro, Usuários, Produtos, Conteúdo e Sistema.
- **Páginas Institucionais & Legais**:
  - Termos (`/termos`), Privacidade (`/privacidade`), Reembolsos (`/refunds`), Instruções (`/instrucoes`), FAQ (`/faq`) e Sobre (`/sobre`).

---

### 2. Landing Page Comercial Oficial (`/` e `/lp.html`)
- **16 Dobras 100% Idênticas**:
  - Header fixo com vidro fumê, logo oficial, links âncora e seletor bilíngue (Português/Inglês).
  - Hero com orbes animados de fundo (`blur(130px)`), prova social (+4.000 criadores) e CTA com efeito de brilho (*shine*).
  - Marquee infinito com os logos oficiais dos marketplaces (TikTok Shop, Shopee, Mercado Livre, etc.).
  - Carrossel interativo de dores com detecção de cursor (`card-glow`), swipe no mobile e wheel no mouse.
  - Comparativo "AS OUTRAS" vs "COM A VOOMI".
  - Pipeline visual em 4 etapas do Creator Lab com toggle de som.
  - Abas interativas do Product Tour (01 a 05) alternando mockups e descrições.
  - Carrossel de provas e resultados reais com visualizador de vídeo em lightbox full-screen.
  - Calculadora de custos comparando 5 ferramentas (Minea, HeyGen, ChatGPT, CapCut, Canva) vs Voomi.
  - Seletor de planos (Mensal, Anual e Vitalício) com motor de cupom de desconto em tempo real.
  - Accordion de FAQ fluido e rodapé oficial.

---

### 3. Integração com Backend & Sessão Ativa
- **Supabase Oficial**: Conectado a `https://omlwqrtqivqcgrrlrlzf.supabase.co` e `https://api.tikshoplab.com.br`.
- **Sessão Autenticada**:
  - Usuário: `matheusmoreira77@icloud.com` (`papan`)
  - Saldo: **1.925 Créditos**
  - Cargo: **Afiliado** | Acesso: **Premium**
- **Injeção Automática de Credenciais**: O arquivo `index.html` injeta a sessão oficial no `localStorage` sob `sb-omlwqrtqivqcgrrlrlzf-auth-token`, permitindo navegar logado imediatamente.
- **Cache Local de Dados (`/data/`)**: Cópia de segurança em JSON de todas as tabelas (produtos, templates de movimento, tutoriais, notificações e perfil) para funcionamento contínuo mesmo offline.

---

## ⚡ HUD de Navegação Rápida (Dev Navigator)

No canto inferior esquerdo da tela, você encontrará o botão flutuante **⚡ Telas Voomi**, que permite:
1. Alternar instantaneamente entre qualquer uma das **20+ telas** da plataforma com apenas 1 clique.
2. Alternar entre a versão SPA e a Landing Page standalone (`/lp.html`).
3. Restaurar a sessão autenticada do Matheus Moreira ou deslogar para ver a experiência de visitante.

---

## 🚀 Como Executar Localmente

O servidor local já está ativo e rodando! Caso queira reiniciar:

```bash
cd /Users/raypires/.gemini/antigravity/scratch/voomi-clone
python3 server.py 3000
```

Abra no seu navegador:
👉 **`http://localhost:3000`** (ou `http://localhost:3000/dashboard`)

Para acessar a Landing Page pura:
👉 **`http://localhost:3000/lp.html`**
