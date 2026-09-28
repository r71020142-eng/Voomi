import os

html_content = """<!doctype html>
<html lang="pt-BR" class="dark notranslate" translate="no">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
    <meta http-equiv="Content-Language" content="pt-BR" />
    <meta name="format-detection" content="telephone=no" />
    <meta name="google" content="notranslate" />

    <!-- Icons & PWA -->
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png" />
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png" />
    <link rel="shortcut icon" href="/favicon.svg" />
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
    <link rel="manifest" href="/site.webmanifest" />
    <meta name="theme-color" media="(prefers-color-scheme: dark)" content="#0A0E0C" />
    <meta name="theme-color" media="(prefers-color-scheme: light)" content="#F1F6F2" />

    <!-- Primary SEO -->
    <title>Voomi — Vídeos que vendem. Sem você aparecer.</title>
    <meta name="description" content="Ache produtos vencedores e crie vídeos com avatar por IA, prontos para postar — sem gravar, sem aparecer e sem editor." />
    <meta name="keywords" content="vídeos com IA, avatar por IA, vender sem aparecer, UGC com IA, TikTok Shop, produtos em alta, radar de produtos, afiliados, criação de vídeos, Voomi" />
    <meta name="author" content="Voomi" />
    <meta name="robots" content="index, follow, max-image-preview:large" />
    <link rel="canonical" href="https://voomi.app.br/" />

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="Voomi" />
    <meta property="og:locale" content="pt_BR" />
    <meta property="og:title" content="Voomi — Vídeos que vendem. Sem você aparecer." />
    <meta property="og:description" content="Ache o produto vencedor e a IA cria o vídeo com um avatar no seu lugar — pronto pra postar, sem você aparecer." />
    <meta property="og:url" content="https://voomi.app.br/" />
    <meta property="og:image" content="/lp/proof-tiktok-shop-results.webp" />

    <!-- Stylesheet -->
    <link rel="stylesheet" href="styles.css" />
  </head>

  <body>
    <div id="inicio" class="voomi-lp">
      <!-- Skip Link for Accessibility -->
      <a class="skip-link" href="#conteudo">Pular para o conteúdo</a>

      <!-- Ambient Glowing Orbs -->
      <div class="ambient" aria-hidden="true">
        <i></i><i></i><i></i>
      </div>

      <!-- Header Navigation -->
      <header class="nav-wrap">
        <nav class="nav container" aria-label="Navegação principal">
          <a class="brand" href="#inicio" aria-label="Voomi — início">
            <img src="/favicon.svg" width="31" height="31" alt="Voomi Logo" />
            <span>voomi</span>
          </a>

          <!-- Desktop & Mobile Navigation Links -->
          <div class="nav__links">
            <a class="nav-item" href="#plataforma">Como funciona</a>
            <a class="nav-item" href="#para-quem">Pra quem é</a>
            <a class="nav-item" href="#provas">Provas</a>
            <a class="nav-item" href="#planos">Planos</a>
            <a class="nav-item" href="#faq">Dúvidas</a>

            <!-- Mobile Language Switcher -->
            <div class="nav__lang nav__lang--stacked" role="group" aria-label="Idioma">
              <button type="button" class="is-active" data-lang="pt" aria-label="Português" aria-pressed="true">
                <svg viewBox="0 0 640 480" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                  <g stroke-width="1pt">
                    <rect fill="#229e45" width="640" height="480"></rect>
                    <path fill="#f8e509" d="M323.4 42.1L588 240.7 323.4 438.3 58.9 240.7z"></path>
                    <circle fill="#2b49a3" cx="323.4" cy="240.7" r="112"></circle>
                    <path d="M216.9 283.5c0 0 41.2-31.4 106.5-31.4s106.5 31.4 106.5 31.4" stroke="#fff" stroke-width="12" fill="none"></path>
                  </g>
                </svg>
              </button>
              <button type="button" data-lang="en" aria-label="English" aria-pressed="false">
                <svg viewBox="0 0 640 480" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                  <g fill-rule="evenodd">
                    <g stroke-width="1pt">
                      <path fill="#bd3d44" d="M0 0h640v37h-640zm0 73.9h640v37h-640zm0 147.8h640v37h-640zm0 73.9h640v37h-640zm0-295.6h640v37h-640zm0 221.7h640v37h-640zm0 73.9h640v37h-640z"></path>
                      <path fill="#fff" d="M0 37h640v36.9h-640zm0 73.9h640v36.9h-640zm0 73.9h640v36.9h-640zm0 73.9h640v36.9h-640zm0 73.9h640v36.9h-640zm0 73.9h640v36.9h-640z"></path>
                    </g>
                    <path fill="#192f5d" d="M0 0h364.8v258.5H0z"></path>
                  </g>
                </svg>
              </button>
            </div>
          </div>

          <!-- Nav Action Buttons -->
          <div class="nav__actions">
            <div class="nav__lang" role="group" aria-label="Idioma">
              <button type="button" class="is-active" data-lang="pt" aria-label="Português" aria-pressed="true">
                <svg viewBox="0 0 640 480" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                  <g stroke-width="1pt">
                    <rect fill="#229e45" width="640" height="480"></rect>
                    <path fill="#f8e509" d="M323.4 42.1L588 240.7 323.4 438.3 58.9 240.7z"></path>
                    <circle fill="#2b49a3" cx="323.4" cy="240.7" r="112"></circle>
                    <path d="M216.9 283.5c0 0 41.2-31.4 106.5-31.4s106.5 31.4 106.5 31.4" stroke="#fff" stroke-width="12" fill="none"></path>
                  </g>
                </svg>
              </button>
              <button type="button" data-lang="en" aria-label="English" aria-pressed="false">
                <svg viewBox="0 0 640 480" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                  <g fill-rule="evenodd">
                    <g stroke-width="1pt">
                      <path fill="#bd3d44" d="M0 0h640v37h-640zm0 73.9h640v37h-640zm0 147.8h640v37h-640zm0 73.9h640v37h-640zm0-295.6h640v37h-640zm0 221.7h640v37h-640zm0 73.9h640v37h-640z"></path>
                      <path fill="#fff" d="M0 37h640v36.9h-640zm0 73.9h640v36.9h-640zm0 73.9h640v36.9h-640zm0 73.9h640v36.9h-640zm0 73.9h640v36.9h-640zm0 73.9h640v36.9h-640z"></path>
                    </g>
                    <path fill="#192f5d" d="M0 0h364.8v258.5H0z"></path>
                  </g>
                </svg>
              </button>
            </div>
            <a class="nav__login" href="#planos">Entrar</a>
            <a class="cta cta--compact" href="#planos">
              <span>Começar agora</span>
              <b aria-hidden="true">↗</b>
            </a>
            <button class="menu" aria-label="Abrir menu" aria-expanded="false">
              <i></i><i></i>
            </button>
          </div>
        </nav>
      </header>

      <!-- Main Content Container -->
      <main id="conteudo">
        <!-- 1. Hero Section -->
        <section class="hero hero--no-vsl container section">
          <div class="hero__brand-field" aria-hidden="true">
            <i><img src="/favicon.svg" alt="" /></i><i><img src="/favicon.svg" alt="" /></i>
            <i><img src="/favicon.svg" alt="" /></i><i><img src="/favicon.svg" alt="" /></i>
            <i><img src="/favicon.svg" alt="" /></i><i><img src="/favicon.svg" alt="" /></i>
            <i><img src="/favicon.svg" alt="" /></i><i><img src="/favicon.svg" alt="" /></i>
            <i><img src="/favicon.svg" alt="" /></i><i><img src="/favicon.svg" alt="" /></i>
            <i><img src="/favicon.svg" alt="" /></i><i><img src="/favicon.svg" alt="" /></i>
            <i><img src="/favicon.svg" alt="" /></i><i><img src="/favicon.svg" alt="" /></i>
            <i><img src="/favicon.svg" alt="" /></i><i><img src="/favicon.svg" alt="" /></i>
            <i><img src="/favicon.svg" alt="" /></i><i><img src="/favicon.svg" alt="" /></i>
          </div>

          <div class="hero__eyebrow">
            <span>SEM APARECER</span>
            <i></i>
            <span>SEM GRAVAR</span>
            <i></i>
            <span>SEM EDITOR</span>
          </div>

          <div class="hero__copy">
            <p class="kicker">A operação completa para vender com vídeo</p>
            <h1>Ache o produto vencedor.<br><em>A IA cria o vídeo por você.</em></h1>
            <p class="hero__sub">Com um avatar no seu lugar — pronto pra postar em minutos.</p>

            <div class="social-line">
              <div class="avatars" role="img" aria-label="Criadores da comunidade">
                <span></span><span></span><span></span><span></span><span></span>
              </div>
              <div>
                <b>★★★★★</b>
                <small>+4.000 criadores ativos</small>
              </div>
            </div>

            <div class="hero__action">
              <a class="cta" href="#planos">
                <span>Quero criar sem aparecer</span>
                <b aria-hidden="true">↗</b>
              </a>
              <p class="micro">Um ano de acesso <i></i> Preço travado</p>
            </div>
          </div>
        </section>

        <!-- 2. Marketplaces Marquee -->
        <section class="market">
          <p>Um vídeo. Vários lugares para vender.</p>
          <div class="marquee" aria-label="Marketplaces compatíveis">
            <div>
              <span class="market-logo market-logo--tiktok" role="img" aria-label="TikTok Shop">
                <i>
                  <svg role="img" viewBox="0 0 24 24"><path fill="currentColor" d="M12.525.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.15 1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.01 2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z"/></svg>
                </i>
                <b>TikTok Shop</b>
              </span>

              <span class="market-logo market-logo--shopee" role="img" aria-label="Shopee">
                <i>
                  <svg role="img" viewBox="0 0 24 24"><path fill="currentColor" d="M15.9414 17.9633c.229-1.879-.981-3.077-4.1758-4.0969-1.548-.528-2.277-1.22-2.26-2.1719.065-1.056 1.048-1.825 2.352-1.85a5.2898 5.2898 0 0 1 2.8838.89c.116.072.197.06.263-.039.09-.145.315-.494.39-.62.051-.081.061-.187-.068-.281-.185-.1369-.704-.4149-.983-.5319a6.4697 6.4697 0 0 0-2.5118-.514c-1.909.008-3.4129 1.215-3.5389 2.826-.082 1.1629.494 2.1078 1.73 2.8278.262.152 1.6799.716 2.2438.892 1.774.553 2.5029 1.2589 2.4799 2.235-.03 1.185-1.187 2.052-2.7339 2.052a6.388 6.388 0 0 1-3.3448-1.063c-.112-.079-.199-.063-.266.037-.097.143-.339.499-.434.64-.055.082-.047.185.086.28 1.146.818 2.49 1.254 3.8969 1.254 2.28 0 3.9968-1.393 4.2278-3.468zM19.9892 7.7471H16.892a4.8988 4.8988 0 0 0-9.784 0H4.0108L2 22.046h20L19.9892 7.7471zm-7.992-3.766a3.784 3.784 0 0 1 3.774 3.766H8.2232a3.784 3.784 0 0 1 3.774-3.766zm-8.23 16.945L5.438 8.8671h1.666v1.942a.56.56 0 0 0 .56.56.56.56 0 0 0 .56-.56V8.8671h7.552v1.942a.56.56 0 0 0 .56.56.56.56 0 0 0 .56-.56V8.8671h1.666l1.671 12.059H3.7672z"/></svg>
                </i>
                <b>Shopee</b>
              </span>

              <span class="market-logo market-logo--mercado" role="img" aria-label="Mercado Livre">
                <i>
                  <svg role="img" viewBox="0 0 24 24"><path fill="currentColor" d="M11.115 16.479a.93.927 0 0 1-.939-.886c-.002-.042-.006-.155-.103-.155-.04 0-.074.023-.113.059-.112.103-.254.206-.46.206a.816.814 0 0 1-.305-.066c-.535-.214-.542-.578-.521-.725.006-.038.007-.08-.02-.11l-.032-.03h-.034c-.027 0-.055.012-.093.039a.788.786 0 0 1-.454.16.7.699 0 0 1-.253-.05c-.708-.27-.65-.928-.617-1.126.005-.041-.005-.072-.03-.092l-.05-.04-.047.043a.728.726 0 0 1-.505.203.73.728 0 0 1-.497-.197.838.835 0 0 1-.264-.537c-.073-.628.324-.969.458-1.076.037-.029.055-.074.048-.12a.154.154 0 0 0-.05-.1l-.048-.035-.054.025c-.173.08-.48.203-.836.203-.497 0-.829-.267-.988-.795a1.86 1.854 0 0 1-.09-.597c0-.986.744-1.854 1.776-2.1a3.61 3.6 0 0 1 .902-.11c.758 0 1.493.208 2.186.619.068.04.153.03.209-.026l.46-.46a.14.14 0 0 0 .01-.19 4.6 4.588 0 0 0-2.865-.943 4.8 4.786 0 0 0-1.196.147C4.693 7.82 3.5 9.24 3.5 10.966c0 .324.053.648.156.963.295.91 1.004 1.488 1.954 1.597.027.003.048.016.06.037.01.02.008.046-.008.065-.054.062-.27.33-.23.75.035.372.229.684.545.88.026.016.04.044.038.074a.108.108 0 0 1-.03.073c-.076.082-.236.27-.23.635.008.487.37.896.865.98.025.004.045.018.055.04.01.02.007.046-.007.065-.08.106-.215.344-.191.733.036.568.513.987 1.135 1.001.03 0 .055.015.068.038.012.022.012.049-.001.07a.64.638 0 0 0-.083.315c0 .548.516.924 1.256.924.908 0 1.53-.564 1.576-1.428l.001-.035-.034-.012a2.02 2.014 0 0 1-.41-.219c-.31-.223-.5-.568-.523-.974-.017-.305.086-.59.29-.8a1.05 1.047 0 0 1 .74-.308c.032 0 .06.01.085.025l.38.253a.85.848 0 0 0 .47.142c.484 0 .878-.396.878-.883z"/></svg>
                </i>
                <b>mercado livre</b>
              </span>

              <span class="market-logo market-logo--instagram" role="img" aria-label="Instagram Shop">
                <i>
                  <svg role="img" viewBox="0 0 24 24"><path fill="currentColor" d="M7.0301.084c-1.2768.0602-2.1487.264-2.911.5634-.7888.3075-1.4575.72-2.1228 1.3877-.6652.6677-1.075 1.3368-1.3802 2.127-.2954.7638-.4956 1.6365-.552 2.914-.0564 1.2775-.0689 1.6882-.0626 4.947.0062 3.2586.0206 3.6671.0825 4.9473.061 1.2765.264 2.1482.5635 2.9107.308.7889.72 1.4573 1.388 2.1228.6679.6655 1.3365 1.0743 2.1285 1.38.7632.295 1.6361.4961 2.9134.552 1.2773.056 1.6884.069 4.9462.0627 3.2578-.0062 3.668-.0206 4.9478-.0825 1.2767-.061 2.1484-.264 2.911-.5635.7887-.308 1.4571-.72 2.1227-1.388.6678-.6679 1.0743-1.3365 1.3801-2.1285.295-.7632.4961-1.6361.552-2.9134.056-1.2773.069-1.6884.0627-4.9462-.0062-3.2578-.0206-3.668-.0825-4.9478-.061-1.2767-.264-2.1484-.5635-2.911-.308-.7887-.72-1.4571-1.388-2.1227C21.3197 1.348 20.651.9415 19.859.6357c-.7632-.295-1.6361-.4961-2.9134-.552-1.2773-.056-1.6884-.069-4.9462-.0627-3.2578.0062-3.668.0206-4.9693.063zm.1065 2.161c1.261-.0574 1.6393-.069 4.8634-.069 3.2241 0 3.6024.0116 4.8634.069 1.1664.0532 1.8001.2479 2.2215.4116.558.2168.956.4754 1.3745.894.4186.4185.6772.8165.894 1.3745.1637.4214.3584 1.0551.4116 2.2215.0574 1.261.069 1.6393.069 4.8634 0 3.2241-.0116 3.6024-.069 4.8634-.0532 1.1664-.2479 1.8001-.4116 2.2215-.2168.558-.4754.956-.894 1.3745-.4185.4186-.8165.6772-1.3745.894-.4214.1637-1.0551.3584-2.2215.4116-1.261.0574-1.6393.069-4.8634.069-3.2241 0-3.6024-.0116-4.8634-.069-1.1664-.0532-1.8001-.2479-2.2215-.4116-.558-.2168-.956-.4754-1.3745-.894-.4186-.4185-.6772-.8165-.894-1.3745-.1637-.4214-.3584-1.0551-.4116-2.2215-.0574-1.261-.069-1.6393-.069-4.8634 0-3.2241.0116-3.6024.069-4.8634.0532-1.1664.2479-1.8001.4116-2.2215.2168-.558.4754-.956.894-1.3745.4185-.4186.8165-.6772 1.3745-.894.4214-.1637 1.0551-.3584 2.2215-.4116zM12 5.8378c-3.4033 0-6.1622 2.7589-6.1622 6.1622 0 3.4033 2.7589 6.1622 6.1622 6.1622 3.4033 0 6.1622-2.7589 6.1622-6.1622 0-3.4033-2.7589-6.1622-6.1622-6.1622zm0 10.1622c-2.2091 0-4-1.7909-4-4 0-2.2091 1.7909-4 4-4 2.2091 0 4 1.7909 4 4 0 2.2091-1.7909 4-4 4zm6.4063-10.8453c-.7959 0-1.441.6451-1.441 1.441s.6451 1.441 1.441 1.441c.7959 0 1.441-.6451 1.441-1.441s-.6451-1.441-1.441-1.441z"/></svg>
                </i>
                <b>Instagram Shop</b>
              </span>

              <span class="market-logo market-logo--amazon" role="img" aria-label="Amazon">
                <i>
                  <svg viewBox="0 0 448 512"><path fill="currentColor" d="M257.2 162.7c-48.7 1.8-169.5 15.5-169.5 117.5 0 109.5 138.3 114 183.5 43.2 6.5 10.2 35.4 37.5 45.3 46.8l56.8-56S341 288.9 341 261.4V114.3C341 89 316.5 32 228.7 32 140.7 32 94 87 94 136.3l73.5 6.8c16.3-49.5 54.2-49.5 54.2-49.5 40.7-.1 35.5 29.8 35.5 69.1zm0 86.8c0 80-84.2 68-84.2 17.2 0-47.2 50.5-56.7 84.2-57.8v40.6zm136 163.5c-7.7 10-70 67-174.5 67S34.2 408.5 9.7 379c-6.8-7.7 1-11.3 5.5-8.3C88.5 415.2 203 438.5 281 438.5c55.5 0 100.8-15.3 107.7-22.7 4.5-4.8 8.8 4.2 4.5 10.2z"/></svg>
                </i>
                <b>amazon</b>
              </span>

              <span class="market-logo market-logo--youtube" role="img" aria-label="YouTube Shopping">
                <i>
                  <svg role="img" viewBox="0 0 24 24"><path fill="currentColor" d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
                </i>
                <b>YouTube Shopping</b>
              </span>
            </div>
          </div>
        </section>

        <!-- 3. Metrics & Numbers -->
        <section class="numbers container section-tight">
          <div>
            <strong>+4.000</strong>
            <span>pessoas usam a Voomi</span>
          </div>
          <div>
            <strong>+15.000</strong>
            <span>criativos todo dia</span>
          </div>
          <div>
            <strong>+250</strong>
            <span>produtos no radar</span>
          </div>
          <div>
            <strong>+120</strong>
            <span>novos criadores por dia</span>
          </div>
          <p>8 meses no mercado. Todo dia mais gente vendendo sem aparecer.</p>
        </section>

        <!-- 4. Dobra 01 — DESTRAVE -->
        <section class="section pains" data-reveal>
          <div class="unlock-shell container">
            <header class="unlock-intro section-head left">
              <span>01 — DESTRAVE</span>
              <h2>Você não trava por falta de vontade.<br class="unlock-intro__desktop-break"> <em>Trava sempre nos mesmos lugares.</em></h2>
            </header>

            <div class="pain-carousel">
              <div class="pain-grid">
                <!-- Pain Card 1 -->
                <article class="pain-card">
                  <div class="pain-card__number">01</div>
                  <div class="pain-card__content">
                    <div class="pain-card__problem">
                      <small>O BLOQUEIO</small>
                      <h3>“Não tenho produto pra vender.”</h3>
                    </div>
                    <div class="card-solution">
                      <small>A SAÍDA</small>
                      <p>Você se afilia. Vende o produto dos outros e fica com a comissão — sem estoque, sem risco.</p>
                    </div>
                  </div>
                </article>

                <!-- Pain Card 2 -->
                <article class="pain-card">
                  <div class="pain-card__number">02</div>
                  <div class="pain-card__content">
                    <div class="pain-card__problem">
                      <small>O BLOQUEIO</small>
                      <h3>“Achei o produto. E agora, quem faz o vídeo?”</h3>
                    </div>
                    <div class="card-solution">
                      <small>A SAÍDA</small>
                      <p>A Voomi cria o vídeo por você. Avatar, cenário, enquadramento — pronto pra postar. Seu rosto nunca aparece.</p>
                    </div>
                  </div>
                </article>

                <!-- Pain Card 3 -->
                <article class="pain-card">
                  <div class="pain-card__number">03</div>
                  <div class="pain-card__content">
                    <div class="pain-card__problem">
                      <small>O BLOQUEIO</small>
                      <h3>“Nem consigo abrir minha loja no TikTok Shop.”</h3>
                    </div>
                    <div class="card-solution">
                      <small>A SAÍDA</small>
                      <p>O Viral Boost cria historinhas que fazem sua conta crescer e ajudam a destravar a loja.</p>
                    </div>
                  </div>
                </article>

                <!-- Pain Card 4 -->
                <article class="pain-card">
                  <div class="pain-card__number">04</div>
                  <div class="pain-card__content">
                    <div class="pain-card__problem">
                      <small>O BLOQUEIO</small>
                      <h3>“Tô preso só no TikTok.”</h3>
                    </div>
                    <div class="card-solution">
                      <small>A SAÍDA</small>
                      <p>O mesmo vídeo trabalha em TikTok Shop, Shopee, Mercado Livre, Instagram Shop e mais.</p>
                    </div>
                  </div>
                </article>

                <!-- Pain Card 5 -->
                <article class="pain-card">
                  <div class="pain-card__number">05</div>
                  <div class="pain-card__content">
                    <div class="pain-card__problem">
                      <small>O BLOQUEIO</small>
                      <h3>“As ferramentas só mostram o que vende. E daí?”</h3>
                    </div>
                    <div class="card-solution">
                      <small>A SAÍDA</small>
                      <p>A Voomi não para na informação. Entrega o vídeo pronto — não mais uma análise.</p>
                    </div>
                  </div>
                </article>

                <!-- Pain Card 6 -->
                <article class="pain-card">
                  <div class="pain-card__number">06</div>
                  <div class="pain-card__content">
                    <div class="pain-card__problem">
                      <small>O BLOQUEIO</small>
                      <h3>“Já gastei dinheiro e não deu em nada.”</h3>
                    </div>
                    <div class="card-solution">
                      <small>A SAÍDA</small>
                      <p>Aqui você paga uma vez e opera o ano inteiro. Você só investe quando resolve criar.</p>
                    </div>
                  </div>
                </article>
              </div>
            </div>

            <!-- Controls -->
            <div class="pain-controls">
              <div></div>
              <span>
                <button type="button" aria-label="Bloqueio anterior">←</button>
                <button type="button" aria-label="Próximo bloqueio">→</button>
              </span>
            </div>

            <div class="unlock-manifesto">
              <p>Não é ferramenta pra uma etapa. <strong>É a operação inteira, do produto ao vídeo postado.</strong></p>
            </div>
          </div>
        </section>

        <!-- 5. Outcome Bridge -->
        <section class="outcome-bridge" data-reveal>
          <div class="outcome-bridge__dots" aria-hidden="true"></div>
          <div class="container outcome-bridge__inner">
            <div class="outcome-bridge__copy">
              <span>O PONTO DE VIRADA</span>
              <h2>Enquanto você tenta<br>fazer tudo sozinho…</h2>
              <p>Tem gente encontrando um produto, transformando uma ideia em vídeo e colocando o criativo no ar no mesmo dia.</p>
              <strong>A boa notícia: você não precisa mais começar da câmera.</strong>
            </div>

            <div class="outcome-bridge__visual" role="img" aria-label="Espaços reservados para criativos e provas de venda">
              <div class="floating-video floating-video--one">
                <img src="/lp/voomi-outcome-product.webp" alt="Massageador portátil em criativo vertical" />
                <small>PRODUTO REAL</small>
              </div>

              <div class="outcome-bridge__arrow" aria-hidden="true">→</div>

              <div class="floating-video floating-video--two">
                <img src="/lp/voomi-outcome-avatar.webp" alt="Criador demonstrando o massageador portátil" />
                <small>CRIATIVO COM AVATAR</small>
              </div>

              <div class="proof-stack proof-stack--screenshot">
                <img src="/lp/proof-tiktok-shop-results.webp" alt="Resultados do TikTok Shop com GMV atribuído de R$ 5,3 mil, 93 itens vendidos e comissão estimada de R$ 538,80" />
              </div>
            </div>
          </div>
        </section>

        <!-- 6. Dobra 02 — SEM CÂMERA -->
        <section class="section compare-wrap" data-reveal>
          <div class="container compare">
            <div class="section-head left compare-title">
              <span>02 — SEM CÂMERA</span>
              <h2>O que te trava não é a ferramenta.<br><em>É a câmera apontada pra você.</em></h2>
              <p>Você já pensou em vender online. Mas na hora de gravar, travou. A Voomi existe para você vender sem passar por isso.</p>
            </div>

            <div class="comparison">
              <div class="comparison__side muted-side">
                <small>AS OUTRAS</small>
                <p><i>×</i>Mostram vídeos — você grava</p>
                <p><i>×</i>Você ainda precisa aparecer</p>
                <p><i>×</i>O vídeo nunca sai</p>
                <p><i>×</i>Cobrança todo mês</p>
              </div>
              <div class="comparison__side voomi-side">
                <small>COM A VOOMI</small>
                <p><i>✓</i>O avatar grava por você</p>
                <p><i>✓</i>Seu rosto nunca aparece</p>
                <p><i>✓</i>Vídeo pronto em minutos</p>
                <p><i>✓</i>Pague uma vez. É seu.</p>
              </div>
            </div>

            <blockquote>
              “Ninguém vai te reconhecer. Ninguém vai te julgar.<br><em>E mesmo assim, você vende.”</em>
            </blockquote>
          </div>
        </section>

        <!-- 7. Dobra 03 — A PLATAFORMA -->
        <section id="plataforma" class="container section platform" data-reveal>
          <div class="section-head">
            <span>03 — A PLATAFORMA</span>
            <h2>Não é uma ferramenta.<br><em>É a operação inteira na sua mão.</em></h2>
            <p>Do produto vencedor ao vídeo pronto. Sem aparecer, sem editor, sem sair daqui.</p>
          </div>

          <!-- Creator Lab Pipeline -->
          <article class="creator creator--pipeline">
            <div class="creator__copy creator__copy--pipeline">
              <div>
                <span class="chip">MÓDULO PRINCIPAL</span>
                <small>CREATOR LAB</small>
                <h3>Onde tudo<br><em>vira vídeo.</em></h3>
              </div>
              <div class="creator__copy-details">
                <p>Escolha o cenário, o produto e o avatar. A Voomi combina tudo e entrega o vídeo pronto pra postar.</p>
                <ul>
                  <li>Cenário definido por você</li>
                  <li>Avatar no seu lugar</li>
                  <li>Vídeo final pronto para vender</li>
                </ul>
              </div>
            </div>

            <div class="creator__visual creator-pipeline" role="group" aria-label="Cenário, produto e avatar transformados em um vídeo pronto">
              <figure class="creator-pipeline__card creator-pipeline__card--scenario">
                <img src="/lp/creator-lab-scenario.webp" alt="Cenário de uma garagem com motocicletas" />
                <figcaption>
                  <small>01</small>
                  <strong>CENÁRIO</strong>
                </figcaption>
              </figure>

              <span aria-hidden="true">→</span>

              <figure class="creator-pipeline__card creator-pipeline__card--product">
                <img src="/lp/creator-lab-product.webp" alt="Jaqueta preta escolhida como produto" />
                <figcaption>
                  <small>02</small>
                  <strong>PRODUTO</strong>
                </figcaption>
              </figure>

              <span aria-hidden="true">→</span>

              <figure class="creator-pipeline__card creator-pipeline__card--avatar">
                <img src="/lp/creator-lab-avatar.webp" alt="Avatar masculino escolhido para apresentar o produto" />
                <figcaption>
                  <small>03</small>
                  <strong>AVATAR</strong>
                </figcaption>
              </figure>

              <span aria-hidden="true">→</span>

              <figure class="creator-pipeline__card creator-pipeline__card--result">
                <video poster="/lp/creator-lab-result-poster.jpg" src="/lp/videos/creator-lab-result.mp4" aria-label="Vídeo final criado com o cenário, o produto e o avatar" autoplay muted loop playsinline></video>
                <button type="button" class="creator-pipeline__sound" aria-label="Ativar som do vídeo final">
                  <span aria-hidden="true">♪</span>
                  ATIVAR SOM
                </button>
                <figcaption>
                  <small>04</small>
                  <strong>VÍDEO PRONTO</strong>
                </figcaption>
              </figure>
            </div>
          </article>

          <!-- Creation Gallery -->
          <div class="creation-gallery">
            <header class="creation-gallery__head">
              <span>GALERIA DE CRIAÇÕES</span>
              <h3>Ideias que viraram<br><em>vídeos prontos.</em></h3>
              <p>Criações feitas dentro da Voomi, passando automaticamente para você ver o resultado.</p>
            </header>

            <div class="story-rail story-rail--creations" role="group" aria-label="Galeria em carrossel de vídeos criados na Voomi">
              <div class="story-rail__track" style="--copies: 2;">
                <!-- Videos looping -->
                <div class="story-video story-video--passive">
                  <video src="/lp/videos/creation-gallery-cookware.mp4" poster="/lp/videos/creation-gallery-cookware-poster.webp" autoplay muted loop playsinline></video>
                </div>
                <div class="story-video story-video--passive">
                  <video src="/lp/videos/creation-gallery-01.mp4" poster="/lp/videos/creation-gallery-01-poster.webp" autoplay muted loop playsinline></video>
                </div>
                <div class="story-video story-video--passive">
                  <video src="/lp/videos/creation-gallery-02.mp4" poster="/lp/videos/creation-gallery-02-poster.webp" autoplay muted loop playsinline></video>
                </div>
                <div class="story-video story-video--passive">
                  <video src="/lp/videos/creation-gallery-03.mp4" poster="/lp/videos/creation-gallery-03-poster.webp" autoplay muted loop playsinline></video>
                </div>
                <div class="story-video story-video--passive">
                  <video src="/lp/videos/creation-gallery-04.mp4" poster="/lp/videos/creation-gallery-04-poster.webp" autoplay muted loop playsinline></video>
                </div>
                <div class="story-video story-video--passive">
                  <video src="/lp/videos/creation-gallery-05.mp4" poster="/lp/videos/creation-gallery-05-poster.webp" autoplay muted loop playsinline></video>
                </div>
                <div class="story-video story-video--passive">
                  <video src="/lp/videos/creation-gallery-06.mp4" poster="/lp/videos/creation-gallery-06-poster.webp" autoplay muted loop playsinline></video>
                </div>
                <!-- Duplicate for loop -->
                <div class="story-video story-video--passive" aria-hidden="true">
                  <video src="/lp/videos/creation-gallery-cookware.mp4" poster="/lp/videos/creation-gallery-cookware-poster.webp" autoplay muted loop playsinline></video>
                </div>
                <div class="story-video story-video--passive" aria-hidden="true">
                  <video src="/lp/videos/creation-gallery-01.mp4" poster="/lp/videos/creation-gallery-01-poster.webp" autoplay muted loop playsinline></video>
                </div>
                <div class="story-video story-video--passive" aria-hidden="true">
                  <video src="/lp/videos/creation-gallery-02.mp4" poster="/lp/videos/creation-gallery-02-poster.webp" autoplay muted loop playsinline></video>
                </div>
              </div>
            </div>
          </div>

          <!-- Product Tour -->
          <header class="product-tour-heading">
            <span>TELAS DA PLATAFORMA</span>
            <h3>Conheça por <em>dentro.</em></h3>
          </header>

          <div class="product-tour">
            <div class="product-tour__topline">
              <div>
                <strong>Veja como cada etapa funciona na prática.</strong>
              </div>
              <p>Navegue pelas telas reais e conheça o papel de cada módulo.</p>
            </div>

            <div class="product-tour__tabs" role="tablist" aria-label="Módulos da plataforma">
              <button type="button" role="tab" class="is-active" aria-selected="true">
                <span>01</span>
                <b>MOTION</b>
                <small>Motion Lab</small>
              </button>
              <button type="button" role="tab" aria-selected="false">
                <span>02</span>
                <b>RADAR</b>
                <small>Radar de produtos</small>
              </button>
              <button type="button" role="tab" aria-selected="false">
                <span>03</span>
                <b>BOOST</b>
                <small>Viral Boost</small>
              </button>
              <button type="button" role="tab" aria-selected="false">
                <span>04</span>
                <b>AVATAR</b>
                <small>Personalize IA</small>
              </button>
              <button type="button" role="tab" aria-selected="false">
                <span>05</span>
                <b>STUDIO</b>
                <small>Lab Studio</small>
              </button>
            </div>

            <div class="product-tour__panel" id="product-tour-panel" role="tabpanel" aria-live="polite">
              <div class="product-tour__screen">
                <div class="product-tour__image product-tour__image--screenshot">
                  <img src="/lp/module-motion-full.webp" alt="Tela do Motion Lab da Voomi com o catálogo de movimentos em vídeo" />
                  <button type="button" class="product-tour__arrow product-tour__arrow--previous" aria-label="Ver tela anterior">←</button>
                  <button type="button" class="product-tour__arrow product-tour__arrow--next" aria-label="Ver próxima tela">→</button>
                </div>
                <div class="product-tour__screen-nav" role="group" aria-label="Navegação entre as telas">
                  <button type="button">
                    <span>←</span> Anterior
                  </button>
                  <p>
                    <b>01</b> <span>/</span> 05
                  </p>
                  <button type="button">
                    Próxima <span>→</span>
                  </button>
                </div>
              </div>

              <aside class="product-tour__guide">
                <header>
                  <span>01 / 05 · MOTION</span>
                  <h3>Motion Lab</h3>
                  <p>Escolha um movimento do catálogo e veja seu influencer executando ele em vídeo, com o produto na cena.</p>
                </header>

                <div class="product-tour__capabilities">
                  <small>O QUE ESTE MÓDULO RESOLVE</small>
                  <ul>
                    <li><i>01</i><span>Escolha o movimento num catálogo pronto</span></li>
                    <li><i>02</i><span>Coloque o produto vestido ou na mão</span></li>
                    <li><i>03</i><span>Ajuste a cena conversando com a IA</span></li>
                  </ul>
                </div>

                <div class="product-tour__outcome">
                  <span>RESULTADO</span>
                  <p>O vídeo sai com movimento de gente de verdade, não com um avatar parado falando.</p>
                </div>

                <footer class="product-tour__progress">
                  <a class="cta cta--compact" href="#planos">
                    <span>Quero usar a Voomi</span>
                    <b aria-hidden="true">↗</b>
                  </a>
                </footer>
              </aside>
            </div>
          </div>
        </section>

        <!-- 8. Dobra 04 — PRA QUEM É -->
        <section id="para-quem" class="container section for-you" data-reveal>
          <div class="section-head">
            <span>04 — PRA QUEM É</span>
            <h2>A Voomi é para você se...</h2>
          </div>

          <div class="audience-clean__grid">
            <article class="audience-card">
              <small>01</small>
              <h3>Quer uma renda a mais, mas não quer aparecer</h3>
              <div class="card-solution">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><polyline points="17 11 19 13 23 9"/></svg>
                <p>O avatar aparece por você. Você vende no anonimato.</p>
              </div>
            </article>

            <article class="audience-card">
              <small>02</small>
              <h3>Não tem produto, estoque ou dinheiro pra investir</h3>
              <div class="card-solution">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><polyline points="17 11 19 13 23 9"/></svg>
                <p>Você se afilia, promove e fica com a comissão.</p>
              </div>
            </article>

            <article class="audience-card">
              <small>03</small>
              <h3>Já tentou gravar e travou</h3>
              <div class="card-solution">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><polyline points="17 11 19 13 23 9"/></svg>
                <p>Aqui você não grava nada — nem precisa perder a vergonha.</p>
              </div>
            </article>

            <article class="audience-card">
              <small>04</small>
              <h3>Não sabe editar e não quer aprender</h3>
              <div class="card-solution">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><polyline points="17 11 19 13 23 9"/></svg>
                <p>A Voomi monta o vídeo e ensina você do zero.</p>
              </div>
            </article>

            <article class="audience-card">
              <small>05</small>
              <h3>Já vende e quer escalar sem virar refém do conteúdo</h3>
              <div class="card-solution">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><polyline points="17 11 19 13 23 9"/></svg>
                <p>Multiplique criativos em minutos, sem gravar.</p>
              </div>
            </article>

            <article class="audience-card">
              <small>06</small>
              <h3>Cansou de ferramenta que só mostra o que vende</h3>
              <div class="card-solution">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><polyline points="17 11 19 13 23 9"/></svg>
                <p>A Voomi entrega o vídeo pronto na sua mão.</p>
              </div>
            </article>
          </div>

          <footer class="audience-clean__footer">
            <strong>Você não precisa aparecer, ter produto ou saber editar.</strong>
            <a class="cta" href="#planos">
              <span>Quero começar agora</span>
              <b aria-hidden="true">↗</b>
            </a>
          </footer>
        </section>

        <!-- 9. Dobra 05 — GENTE REAL -->
        <section id="provas" class="section proof-wrap" data-reveal>
          <div class="container">
            <div class="section-head">
              <span>05 — GENTE REAL</span>
              <h2>Todo dia chega mensagem<br><em>assim no nosso suporte.</em></h2>
              <p class="proof-summary">Nenhum apareceu na câmera. Nenhum tinha experiência.<strong>A diferença é que eles começaram.</strong></p>
            </div>

            <!-- Video Story Rail -->
            <div class="story-rail story-rail--videos" role="group" aria-label="Carrossel de vídeos de criadores">
              <div class="story-rail__track" style="--copies: 2;">
                <button type="button" class="story-video" aria-label="Abrir resultado com áudio">
                  <video src="/lp/videos/voomi-video-01.mp4" poster="/lp/voomi-video-01-poster.webp" autoplay muted loop playsinline></video>
                  <span>
                    <i>▶</i>
                    <b>CLIQUE PARA OUVIR</b>
                  </span>
                </button>
                <button type="button" class="story-video" aria-label="Abrir resultado com áudio">
                  <video src="/lp/videos/voomi-video-02.mp4" poster="/lp/voomi-video-02-poster.webp" autoplay muted loop playsinline></video>
                  <span>
                    <i>▶</i>
                    <b>CLIQUE PARA OUVIR</b>
                  </span>
                </button>
                <button type="button" class="story-video" aria-label="Abrir resultado com áudio">
                  <video src="/lp/videos/voomi-video-04.mp4" poster="/lp/voomi-video-04-poster.jpg" autoplay muted loop playsinline></video>
                  <span>
                    <i>▶</i>
                    <b>CLIQUE PARA OUVIR</b>
                  </span>
                </button>
                <button type="button" class="story-video" aria-label="Abrir resultado com áudio">
                  <video src="/lp/videos/voomi-video-05.mp4" poster="/lp/voomi-video-05-poster.jpg" autoplay muted loop playsinline></video>
                  <span>
                    <i>▶</i>
                    <b>CLIQUE PARA OUVIR</b>
                  </span>
                </button>
                <button type="button" class="story-video" aria-label="Abrir depoimento com áudio">
                  <video src="/lp/videos/voomi-testimonial-07.mp4" poster="/lp/videos/voomi-testimonial-07-poster.webp" autoplay muted loop playsinline></video>
                  <span>
                    <i>▶</i>
                    <b>CLIQUE PARA OUVIR</b>
                  </span>
                </button>
                <button type="button" class="story-video" aria-label="Abrir depoimento com áudio">
                  <video src="/lp/videos/voomi-testimonial-08.mp4" poster="/lp/videos/voomi-testimonial-08-poster.webp" autoplay muted loop playsinline></video>
                  <span>
                    <i>▶</i>
                    <b>CLIQUE PARA OUVIR</b>
                  </span>
                </button>
                <!-- Duplication for infinite flow -->
                <button type="button" class="story-video" aria-hidden="true" tabindex="-1">
                  <video src="/lp/videos/voomi-video-01.mp4" poster="/lp/voomi-video-01-poster.webp" autoplay muted loop playsinline></video>
                  <span><i>▶</i><b>CLIQUE PARA OUVIR</b></span>
                </button>
                <button type="button" class="story-video" aria-hidden="true" tabindex="-1">
                  <video src="/lp/videos/voomi-video-02.mp4" poster="/lp/voomi-video-02-poster.webp" autoplay muted loop playsinline></video>
                  <span><i>▶</i><b>CLIQUE PARA OUVIR</b></span>
                </button>
              </div>
            </div>

            <!-- Proof Orbit Screenshots -->
            <div class="proof-orbit">
              <div class="proof-orbit__hud">
                <span>RESULTADOS REAIS</span>
              </div>
              <div class="proof-orbit__viewport">
                <button type="button" class="proof-orbit__shot is-active" style="--offset: 0" aria-label="Ver prova: Começou a postar e a primeira venda saiu" aria-current="true">
                  <img src="/lp/proofs/proof-primeira-venda.webp" alt="Começou a postar e a primeira venda saiu" />
                </button>
                <button type="button" class="proof-orbit__shot" style="--offset: 1" aria-label="Ver prova: 20 produtos vendidos em 7 dias">
                  <img src="/lp/proofs/proof-512-vinte-vendas.webp" alt="20 produtos vendidos em 7 dias" />
                </button>
                <button type="button" class="proof-orbit__shot" style="--offset: 2" aria-label="Ver prova: Duas vendas e evolução com as orientações">
                  <img src="/lp/proofs/proof-feedback-tenis.webp" alt="Duas vendas e evolução com as orientações" />
                </button>
                <button type="button" class="proof-orbit__shot" style="--offset: 3" aria-label="Ver prova: 6 vendas e comissão gerada">
                  <img src="/lp/proofs/proof-374-seis-vendas.webp" alt="6 vendas e comissão gerada" />
                </button>
                <button type="button" class="proof-orbit__shot" style="--offset: 4" aria-label="Ver prova: 24 produtos vendidos">
                  <img src="/lp/proofs/proof-mil-24-vendas.webp" alt="24 produtos vendidos" />
                </button>
                <button type="button" class="proof-orbit__shot" style="--offset: 5" aria-label="Ver prova: Resultado internacional em poucos dias">
                  <img src="/lp/proofs/proof-primeira-venda-euro.webp" alt="Resultado internacional em poucos dias" />
                </button>
              </div>

              <div class="proof-orbit__readout">
                <div>
                  <strong>Primeira venda</strong>
                  <p>Começou a postar e a primeira venda saiu</p>
                </div>
                <span>
                  <button type="button" aria-label="Prova anterior">←</button>
                  <button type="button" aria-label="Próxima prova">→</button>
                </span>
              </div>

              <div class="proof-orbit__dots">
                <button type="button" class="is-active" aria-label="Ir para prova 1"></button>
                <button type="button" aria-label="Ir para prova 2"></button>
                <button type="button" aria-label="Ir para prova 3"></button>
                <button type="button" aria-label="Ir para prova 4"></button>
                <button type="button" aria-label="Ir para prova 5"></button>
                <button type="button" aria-label="Ir para prova 6"></button>
              </div>
            </div>
          </div>
        </section>

        <!-- 10. Faça as Contas -->
        <section class="tool-cost section" data-reveal>
          <div class="container">
            <div class="tool-cost__head">
              <span>FAÇA AS CONTAS</span>
              <h2>Quanto custa montar essa operação<br><em>com ferramentas separadas?</em></h2>
              <p>Produto, roteiro, avatar, edição e design em cinco plataformas, cinco cobranças e cinco fluxos diferentes.</p>
            </div>

            <div class="tool-cost__layout">
              <div class="tool-cost__list">
                <article>
                  <i aria-hidden="true"><span style="background-image: url('/lp/tools/minea.png');"></span></i>
                  <div>
                    <strong>Minea Starter</strong>
                    <span>Pesquisa de produtos</span>
                  </div>
                  <b>R$ 255,01<small>/mês</small></b>
                </article>

                <article>
                  <i aria-hidden="true"><span style="background-image: url('/lp/tools/heygen.ico');"></span></i>
                  <div>
                    <strong>HeyGen Creator</strong>
                    <span>Avatares e vídeos</span>
                  </div>
                  <b>R$ 150,92<small>/mês</small></b>
                </article>

                <article>
                  <i aria-hidden="true"><span style="background-image: url('/lp/tools/chatgpt.svg');"></span></i>
                  <div>
                    <strong>ChatGPT Plus</strong>
                    <span>Ideias e roteiros</span>
                  </div>
                  <b>R$ 104,09<small>/mês</small></b>
                </article>

                <article>
                  <i aria-hidden="true"><span style="background-image: url('/lp/tools/capcut.ico');"></span></i>
                  <div>
                    <strong>CapCut Pro</strong>
                    <span>Edição de vídeo</span>
                  </div>
                  <b>R$ 104,03<small>/mês</small></b>
                </article>

                <article>
                  <i aria-hidden="true"><span style="background-image: url('/lp/tools/canva.ico');"></span></i>
                  <div>
                    <strong>Canva Pro</strong>
                    <span>Design e criativos</span>
                  </div>
                  <b>R$ 62,45<small>/mês</small></b>
                </article>

                <footer>
                  <span>TOTAL DE REFERÊNCIA</span>
                  <strong>≈ R$ 676,51<small>/mês</small></strong>
                  <p>Mais de R$ 8.118 por ano em assinaturas separadas.</p>
                </footer>
              </div>

              <aside class="tool-cost__voomi">
                <span>COM A VOOMI</span>
                <h3>Uma operação.<br>Um só fluxo.</h3>
                <ul>
                  <li><i>✓</i> Radar de produtos</li>
                  <li><i>✓</i> Roteiros e Viral Boost</li>
                  <li><i>✓</i> Avatares e cenários com IA</li>
                  <li><i>✓</i> Criação e edição de vídeos</li>
                </ul>

                <div>
                  <small>A PARTIR DE</small>
                  <p>
                    <span>R$</span>
                    <strong>297,00</strong>
                    <b>/mês</b>
                  </p>
                  <em>ou R$ 597,00 no plano anual</em>
                </div>

                <a href="#planos">
                  <span>Ver planos da Voomi</span>
                  <b aria-hidden="true">↗</b>
                </a>
              </aside>
            </div>

            <p class="tool-cost__note">Conversão informativa pela PTAX de venda a R$ 5,2043, publicada pelo Banco Central em 18 de agosto de 2026. Preços, impostos, região e câmbio podem alterar os valores.</p>
          </div>
        </section>

        <!-- 11. Dobra 06 — ESCOLHA SEU PLANO -->
        <section id="planos" class="container section pricing">
          <div class="section-head">
            <span>06 — ESCOLHA SEU PLANO</span>
            <h2>Comece agora. Continue<br><em>do jeito que faz sentido pra você.</em></h2>
            <p>Imagens ilimitadas em qualquer plano. O anual é o ponto certo para quem vai postar todo dia: um ano inteiro de operação, sem voltar a pensar em cobrança.</p>
          </div>

          <!-- Coupon Box -->
          <form class="coupon-box">
            <label for="coupon-code">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg>
              Tem um cupom de creator?
            </label>
            <div class="coupon-box__field">
              <input id="coupon-code" name="coupon" placeholder="Digite seu cupom" autocomplete="off" autocapitalize="characters" spellcheck="false" />
              <button type="submit">Aplicar</button>
            </div>
            <p class="coupon-box__error" role="alert" style="display: none;"></p>
          </form>

          <!-- Pricing Grid -->
          <div class="pricing-grid pricing-grid--three">
            <!-- 1. Plano Mensal -->
            <article class="pricing-card">
              <div class="pricing-card__head">
                <small>PARA EXPERIMENTAR</small>
                <h3>Plano Mensal</h3>
                <p>Para conhecer a operação inteira sem compromisso de prazo. Você renova quando quiser — e pode subir para o anual a qualquer momento.</p>
              </div>
              <div class="pricing-card__price">
                <span>R$</span>
                <strong>297,00</strong>
                <small>/mês</small>
              </div>
              <p class="pricing-card__compare" style="display: none;"></p>
              <div class="pricing-card__divider"></div>
              <ul>
                <li>
                  <i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><polyline points="17 11 19 13 23 9"/></svg></i>
                  <div>
                    <strong>Imagens ilimitadas</strong>
                    <span>Imagens, roteiros, influencers e cenários sem consumir crédito</span>
                  </div>
                </li>
                <li>
                  <i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><polyline points="17 11 19 13 23 9"/></svg></i>
                  <div>
                    <strong>3 vídeos de 8s no 1º mês</strong>
                    <span>Mais 30 clonagens de movimento</span>
                  </div>
                </li>
                <li>
                  <i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><polyline points="17 11 19 13 23 9"/></svg></i>
                  <div>
                    <strong>20 vídeos de 8s por mês</strong>
                    <span>A partir da 1ª renovação, com 30 clonagens — o saldo não acumula</span>
                  </div>
                </li>
              </ul>
              <a class="pricing-card__cta" href="https://checkout.applyfy.com.br/checkout/cmoj54j7f0czv1rqrkgh7lk7y?offer=FYN96AM" target="_blank" rel="noopener noreferrer">
                <span>Quero começar no mensal</span>
                <b aria-hidden="true">↗</b>
              </a>
              <p class="pricing-card__micro">ACESSO À PLATAFORMA VOOMI</p>
            </article>

            <!-- 2. Plano Anual (Featured) -->
            <article class="pricing-card pricing-card--featured">
              <div class="pricing-card__badge">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
                MAIS RECOMENDADO
              </div>
              <div class="pricing-card__head">
                <small>MELHOR CUSTO-BENEFÍCIO</small>
                <h3>Plano Anual</h3>
                <p>O plano de quem já decidiu: um ano inteiro criando, com o preço travado e sem cobrança voltando todo mês. É o que a maior parte das pessoas escolhe.</p>
              </div>
              <div class="pricing-card__price">
                <b>12x de</b>
                <span>R$</span>
                <strong>63,55</strong>
              </div>
              <p class="pricing-card__compare" style="display: none;"></p>
              <p class="pricing-card__cash">ou R$ 597,00 à vista</p>
              <div class="pricing-card__divider"></div>
              <ul>
                <li>
                  <i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><polyline points="17 11 19 13 23 9"/></svg></i>
                  <div>
                    <strong>Imagens ilimitadas</strong>
                    <span>Imagens, roteiros, influencers e cenários sem consumir crédito</span>
                  </div>
                </li>
                <li>
                  <i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><polyline points="17 11 19 13 23 9"/></svg></i>
                  <div>
                    <strong>20 vídeos de 8s por mês</strong>
                    <span>3 no 1º mês e 20 a partir da 1ª renovação, com 30 clonagens — o saldo não acumula</span>
                  </div>
                </li>
                <li>
                  <i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><polyline points="17 11 19 13 23 9"/></svg></i>
                  <div>
                    <strong>Preço travado por 12 meses</strong>
                    <span>Sem reajuste no meio do caminho</span>
                  </div>
                </li>
              </ul>
              <a class="pricing-card__cta" href="https://checkout.applyfy.com.br/checkout/cmok3u6hj0cwh1rqqhzivg0c9?offer=R9VNPCI" target="_blank" rel="noopener noreferrer">
                <span>Quero o plano anual</span>
                <b aria-hidden="true">↗</b>
              </a>
              <p class="pricing-card__micro">ACESSO À PLATAFORMA VOOMI</p>
            </article>

            <!-- 3. Plano Especial / Vitalício -->
            <article class="pricing-card">
              <div class="pricing-card__head">
                <small>MELHOR CUSTO-BENEFÍCIO</small>
                <h3>Plano Anual</h3>
                <p>Paga uma vez e opera o ano inteiro, com o preço travado e sem cobrança voltando todo mês. Faz sentido para quem já decidiu.</p>
              </div>
              <div class="pricing-card__price">
                <b>12x de</b>
                <span>R$</span>
                <strong>74,19</strong>
              </div>
              <p class="pricing-card__compare" style="display: none;"></p>
              <p class="pricing-card__cash">ou R$ 697,00 à vista</p>
              <div class="pricing-card__divider"></div>
              <ul>
                <li>
                  <i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><polyline points="17 11 19 13 23 9"/></svg></i>
                  <div>
                    <strong>Imagens ilimitadas</strong>
                    <span>Imagens, roteiros, influencers e cenários sem consumir crédito</span>
                  </div>
                </li>
                <li>
                  <i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><polyline points="17 11 19 13 23 9"/></svg></i>
                  <div>
                    <strong>3 vídeos de 8s + 30 clonagens</strong>
                    <span>Pacote único, liberado na compra — não renova</span>
                  </div>
                </li>
                <li>
                  <i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><polyline points="17 11 19 13 23 9"/></svg></i>
                  <div>
                    <strong>Créditos em dobro</strong>
                    <span>No primeiro pacote de créditos que comprar</span>
                  </div>
                </li>
              </ul>
              <a class="pricing-card__cta" href="https://checkout.applyfy.com.br/checkout/cmok3u6hj0cwh1rqqhzivg0c9?offer=R9VNPCI" target="_blank" rel="noopener noreferrer">
                <span>Quero o plano anual</span>
                <b aria-hidden="true">↗</b>
              </a>
              <p class="pricing-card__micro">ACESSO À PLATAFORMA VOOMI</p>
            </article>
          </div>

          <!-- Guarantee Note -->
          <div class="pricing-note">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            <p>
              <strong>Escolha com tranquilidade.</strong>
              <span>Os três planos incluem imagens ilimitadas e acesso à experiência completa da Voomi.</span>
            </p>
          </div>
        </section>

        <!-- 12. Dobra 07 — DÚVIDAS -->
        <section id="faq" class="container section faq" data-reveal>
          <div class="faq__intro">
            <span>07 — DÚVIDAS</span>
            <h2>Ficou com alguma dúvida?<br><em>A gente responde.</em></h2>
            <p>Respostas diretas, sem letras miúdas.</p>
          </div>

          <div class="faq__list">
            <!-- FAQ 1 -->
            <article>
              <button type="button" aria-expanded="false">
                <span>01</span>
                <b>Preciso aparecer nos vídeos?</b>
                <i aria-hidden="true">+</i>
              </button>
              <div>
                <p>Não. Você escolhe um avatar — pronto ou criado do seu jeito — e ele aparece no seu lugar. Seu rosto nunca vai para a tela.</p>
              </div>
            </article>

            <!-- FAQ 2 -->
            <article>
              <button type="button" aria-expanded="false">
                <span>02</span>
                <b>Funciona pra quem está começando do zero?</b>
                <i aria-hidden="true">+</i>
              </button>
              <div>
                <p>Sim. Você não precisa de produto, estoque, seguidores ou experiência. A Lab Academy mostra o caminho.</p>
              </div>
            </article>

            <!-- FAQ 3 -->
            <article>
              <button type="button" aria-expanded="false">
                <span>03</span>
                <b>Preciso saber editar vídeo?</b>
                <i aria-hidden="true">+</i>
              </button>
              <div>
                <p>Não. A Voomi entrega o vídeo montado; o Lab Studio permite ajustes simples sem aprender outro programa.</p>
              </div>
            </article>

            <!-- FAQ 4 -->
            <article>
              <button type="button" aria-expanded="false">
                <span>04</span>
                <b>Não tenho produto pra vender. E agora?</b>
                <i aria-hidden="true">+</i>
              </button>
              <div>
                <p>Você se afilia a produtos que já vendem e ganha comissão. O Radar mostra quais merecem sua atenção.</p>
              </div>
            </article>

            <!-- FAQ 5 -->
            <article>
              <button type="button" aria-expanded="false">
                <span>05</span>
                <b>Qual a diferença da Voomi para outras ferramentas?</b>
                <i aria-hidden="true">+</i>
              </button>
              <div>
                <p>A maioria mostra o que vende e deixa você gravar. A Voomi acha o produto, cria o avatar e gera o vídeo pronto.</p>
              </div>
            </article>

            <!-- FAQ 6 -->
            <article>
              <button type="button" aria-expanded="false">
                <span>06</span>
                <b>Só funciona para TikTok Shop?</b>
                <i aria-hidden="true">+</i>
              </button>
              <div>
                <p>Não. O vídeo serve para TikTok Shop, Shopee, Mercado Livre, Instagram Shop e outros canais.</p>
              </div>
            </article>

            <!-- FAQ 7 -->
            <article>
              <button type="button" aria-expanded="false">
                <span>07</span>
                <b>E se eu travar ou tiver dúvida?</b>
                <i aria-hidden="true">+</i>
              </button>
              <div>
                <p>Um assistente inteligente responde 24h e, quando precisar, há suporte humano de verdade.</p>
              </div>
            </article>
          </div>
        </section>

        <!-- 13. Chamada Final -->
        <section id="oferta" class="final section" data-reveal>
          <div class="final__orb" aria-hidden="true"></div>
          <div class="container final__content">
            <span class="chip">A DECISÃO É SUA</span>
            <h2>Você chegou até aqui<br><em>por um motivo.</em></h2>
            <p>Agora existe um jeito de vender sem pôr a cara na internet, sem estoque, sem saber gravar ou editar. A Voomi acha o produto, cria o avatar e entrega o vídeo pronto.</p>
            <h3>A pergunta não é mais “será que eu consigo?”<br><strong>É “por que não começar agora?”</strong></h3>
            <a class="cta" href="#planos">
              <span>Quero criar meu primeiro vídeo sem aparecer</span>
              <b aria-hidden="true">↗</b>
            </a>
            <small>SEM GRAVAR <i></i> SEM APARECER <i></i> SEM MENSALIDADE</small>
          </div>
        </section>
      </main>

      <!-- Footer -->
      <footer class="container footer">
        <a class="brand" href="#inicio" aria-label="Voomi — início">
          <img src="/favicon.svg" width="31" height="31" alt="Voomi Logo" />
          <span>voomi</span>
        </a>
        <p>Vídeos que vendem. Sem você aparecer.</p>
        <span>© 2026 Voomi. Todos os direitos reservados.</span>
      </footer>

      <!-- Video Lightbox Modal -->
      <div class="video-lightbox is-ready" role="dialog" aria-modal="true" style="display: none;">
        <button type="button" aria-label="Fechar vídeo">×</button>
        <div class="video-lightbox__stage">
          <video preload="auto" controls playsinline></video>
          <span class="video-lightbox__loading" aria-live="polite">Carregando vídeo…</span>
        </div>
      </div>
    </div>

    <!-- Interactive Script -->
    <script src="app.js"></script>
  </body>
</html>
"""

with open("/Users/raypires/.gemini/antigravity/scratch/voomi-clone/index.html", "w") as f:
    f.write(html_content)

print("Generated index.html successfully, size:", len(html_content))
