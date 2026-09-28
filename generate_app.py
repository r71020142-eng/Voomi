import os

with open("/Users/raypires/.gemini/antigravity/brain/9fc1d89e-e22c-44e8-823b-a8e1f6e34e59/scratch/aux_dump.js") as f:
    aux = f.read()

idx_pt = aux.find("su={pt:{")
if idx_pt == -1: idx_pt = aux.find("var su={pt:{")
idx_end = aux.find(",cu=e=>e===`pt`")
if idx_end == -1: idx_end = aux.find(";function uu(")

su_js = aux[idx_pt:idx_end]
if su_js.startswith("var "):
    su_js = su_js[4:]

app_content = """/**
 * Voomi.app.br - 100% Faithful Recreated Engine
 * Full Bilingual Support, Interactive Modules, Carousels, Video Lightbox, and Pricing Engine
 */

const """ + su_js + """;

const MODULES = [
  { id: "motion", tag: "MOTION", image: "/lp/module-motion-full.webp" },
  { id: "radar", tag: "RADAR", image: "/lp/module-radar-full.webp" },
  { id: "boost", tag: "BOOST", image: "/lp/module-boost-full.webp" },
  { id: "avatar", tag: "AVATAR", image: "/lp/module-avatar-full.webp" },
  { id: "studio", tag: "STUDIO", image: "/lp/module-studio-full.webp" }
];

const TOOLS = [
  { logo: "/lp/tools/minea.png", name: "Minea Starter", price: "R$ 255,01" },
  { logo: "/lp/tools/heygen.ico", name: "HeyGen Creator", price: "R$ 150,92" },
  { logo: "/lp/tools/chatgpt.svg", name: "ChatGPT Plus", price: "R$ 104,09" },
  { logo: "/lp/tools/capcut.ico", name: "CapCut Pro", price: "R$ 104,03" },
  { logo: "/lp/tools/canva.ico", name: "Canva Pro", price: "R$ 62,45" }
];

const STORY_VIDEOS = [
  { src: "/lp/videos/voomi-video-01.mp4", poster: "/lp/voomi-video-01-poster.webp", testimonial: false },
  { src: "/lp/videos/voomi-video-02.mp4", poster: "/lp/voomi-video-02-poster.webp", testimonial: false },
  { src: "/lp/videos/voomi-video-04.mp4", poster: "/lp/voomi-video-04-poster.jpg", testimonial: false },
  { src: "/lp/videos/voomi-video-05.mp4", poster: "/lp/voomi-video-05-poster.jpg", testimonial: false },
  { src: "/lp/videos/voomi-testimonial-07.mp4", poster: "/lp/videos/voomi-testimonial-07-poster.webp", testimonial: true },
  { src: "/lp/videos/voomi-testimonial-08.mp4", poster: "/lp/videos/voomi-testimonial-08-poster.webp", testimonial: true }
];

const GALLERY_VIDEOS = [
  { src: "/lp/videos/creation-gallery-cookware.mp4", poster: "/lp/videos/creation-gallery-cookware-poster.webp" },
  { src: "/lp/videos/creation-gallery-01.mp4", poster: "/lp/videos/creation-gallery-01-poster.webp" },
  { src: "/lp/videos/creation-gallery-02.mp4", poster: "/lp/videos/creation-gallery-02-poster.webp" },
  { src: "/lp/videos/creation-gallery-03.mp4", poster: "/lp/videos/creation-gallery-03-poster.webp" },
  { src: "/lp/videos/creation-gallery-04.mp4", poster: "/lp/videos/creation-gallery-04-poster.webp" },
  { src: "/lp/videos/creation-gallery-05.mp4", poster: "/lp/videos/creation-gallery-05-poster.webp" },
  { src: "/lp/videos/creation-gallery-06.mp4", poster: "/lp/videos/creation-gallery-06-poster.webp" }
];

const PROOFS = [
  "/lp/proofs/proof-primeira-venda.webp",
  "/lp/proofs/proof-512-vinte-vendas.webp",
  "/lp/proofs/proof-feedback-tenis.webp",
  "/lp/proofs/proof-374-seis-vendas.webp",
  "/lp/proofs/proof-mil-24-vendas.webp",
  "/lp/proofs/proof-primeira-venda-euro.webp"
];

const DEFAULT_LINKS = {
  monthly: "https://checkout.applyfy.com.br/checkout/cmoj54j7f0czv1rqrkgh7lk7y?offer=FYN96AM",
  annual: "https://checkout.applyfy.com.br/checkout/cmok3u6hj0cwh1rqqhzivg0c9?offer=R9VNPCI",
  lifetime: "https://checkout.applyfy.com.br/checkout/cmok3u6hj0cwh1rqqhzivg0c9?offer=R9VNPCI"
};

const PRICING_STANDARD = { monthly: 297, annual: 597, lifetime: 697 };
const PRICING_CREATOR  = { monthly: 147, annual: 347, lifetime: 347 };
const INSTALLMENT_FACTOR = 1.2786;

function formatCurrency(val) {
  return val.toLocaleString("pt-BR", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

function calculateInstallment(total) {
  return (total * INSTALLMENT_FACTOR) / 12;
}

function interpolate(tpl, vars) {
  return tpl.replace(/\\{(\\w+)\\}/g, (_, k) => String(vars[k] ?? `{${k}}`));
}

// App State
let state = {
  lang: "pt",
  menuOpen: false,
  painIndex: 0,
  tourIndex: 0,
  proofIndex: 0,
  activeCoupon: null,
  couponStatus: "idle",
  openFaq: null,
  lightboxVideo: null,
  videoSoundActive: false
};

function getT() {
  return su[state.lang] || su.pt;
}

// Initialize Application
document.addEventListener("DOMContentLoaded", () => {
  initLanguage();
  initMobileMenu();
  initPainCarousel();
  initProductTour();
  initProofOrbit();
  initCreatorLabVideo();
  initStoryRails();
  initCouponSystem();
  initFAQ();
  initLightbox();
  initScrollReveal();
  initMouseGlow();
  renderAll();
});

// Render texts and bindings
function renderAll() {
  const t = getT();
  document.documentElement.lang = state.lang === "pt" ? "pt-BR" : "en";

  // Lang switcher buttons
  document.querySelectorAll(".nav__lang button").forEach(btn => {
    const isPt = btn.getAttribute("data-lang") === "pt";
    btn.classList.toggle("is-active", (state.lang === "pt" && isPt) || (state.lang === "en" && !isPt));
  });

  // Nav Links
  const navLinks = document.querySelectorAll(".nav__links a.nav-item");
  if (navLinks.length >= 5) {
    navLinks[0].textContent = t.nav[0];
    navLinks[1].textContent = t.nav[1];
    navLinks[2].textContent = t.nav[2];
    navLinks[3].textContent = t.nav[3];
    navLinks[4].textContent = t.nav[4];
  }
  const navLogin = document.querySelector(".nav__login");
  if (navLogin) navLogin.textContent = t.login;
  const navCta = document.querySelector(".nav .cta span");
  if (navCta) navCta.textContent = t.ctaCompact;

  // Hero
  const eyebrows = document.querySelectorAll(".hero__eyebrow span");
  if (eyebrows.length >= 3) {
    eyebrows[0].textContent = t.hero.eyebrow[0];
    eyebrows[1].textContent = t.hero.eyebrow[1];
    eyebrows[2].textContent = t.hero.eyebrow[2];
  }
  const heroKicker = document.querySelector(".hero .kicker");
  if (heroKicker) heroKicker.textContent = t.hero.kicker;
  const heroH1 = document.querySelector(".hero h1");
  if (heroH1) heroH1.innerHTML = `${t.hero.title}<br><em>${t.hero.titleEm}</em>`;
  const heroSub = document.querySelector(".hero__sub");
  if (heroSub) heroSub.textContent = t.hero.sub;
  const heroSocial = document.querySelector(".social-line small");
  if (heroSocial) heroSocial.textContent = t.hero.social;
  const heroCta = document.querySelector(".hero__action .cta span");
  if (heroCta) heroCta.textContent = t.hero.cta;
  const heroMicro = document.querySelector(".hero .micro");
  if (heroMicro) heroMicro.innerHTML = `${t.hero.micro[0]} <i></i> ${t.hero.micro[1]}`;

  // Market
  const marketLead = document.querySelector(".market > p");
  if (marketLead) marketLead.textContent = t.market.lead;

  // Numbers
  const numItems = document.querySelectorAll(".numbers div span");
  if (numItems.length >= 4) {
    numItems[0].textContent = t.numbers.labels[0];
    numItems[1].textContent = t.numbers.labels[1];
    numItems[2].textContent = t.numbers.labels[2];
    numItems[3].textContent = t.numbers.labels[3];
  }
  const numNote = document.querySelector(".numbers p");
  if (numNote) numNote.textContent = t.numbers.note;

  // Pains
  const painEyebrow = document.querySelector(".pains .section-head span");
  if (painEyebrow) painEyebrow.textContent = t.pains.eyebrow;
  const painH2 = document.querySelector(".pains .section-head h2");
  if (painH2) painH2.innerHTML = `${t.pains.title}<br class="unlock-intro__desktop-break"> <em>${t.pains.titleEm}</em>`;
  renderPainCards();
  const manifesto = document.querySelector(".unlock-manifesto p");
  if (manifesto) manifesto.innerHTML = `${t.pains.manifesto} <strong>${t.pains.manifestoStrong}</strong>`;

  // Bridge
  const bridgeEyebrow = document.querySelector(".outcome-bridge__copy span");
  if (bridgeEyebrow) bridgeEyebrow.textContent = t.bridge.eyebrow;
  const bridgeH2 = document.querySelector(".outcome-bridge__copy h2");
  if (bridgeH2) bridgeH2.innerHTML = `${t.bridge.title}<br>${t.bridge.titleLine2}`;
  const bridgeP = document.querySelector(".outcome-bridge__copy p");
  if (bridgeP) bridgeP.textContent = t.bridge.body;
  const bridgeStrong = document.querySelector(".outcome-bridge__copy strong");
  if (bridgeStrong) bridgeStrong.textContent = t.bridge.strong;

  // Compare
  const compEyebrow = document.querySelector(".compare-title span");
  if (compEyebrow) compEyebrow.textContent = t.compare.eyebrow;
  const compH2 = document.querySelector(".compare-title h2");
  if (compH2) compH2.innerHTML = `${t.compare.title}<br><em>${t.compare.titleEm}</em>`;
  const compP = document.querySelector(".compare-title p");
  if (compP) compP.textContent = t.compare.body;
  const labelOthers = document.querySelector(".muted-side small");
  if (labelOthers) labelOthers.textContent = t.compare.labelOthers;
  const labelVoomi = document.querySelector(".voomi-side small");
  if (labelVoomi) labelVoomi.textContent = t.compare.labelVoomi;
  
  const othersList = document.querySelectorAll(".muted-side p");
  t.compare.others.forEach((txt, idx) => {
    if (othersList[idx]) othersList[idx].innerHTML = `<i>×</i>${txt}`;
  });
  const voomiList = document.querySelectorAll(".voomi-side p");
  t.compare.voomi.forEach((txt, idx) => {
    if (voomiList[idx]) voomiList[idx].innerHTML = `<i>✓</i>${txt}`;
  });
  const compQuote = document.querySelector(".compare blockquote");
  if (compQuote) compQuote.innerHTML = `${t.compare.quote}<br><em>${t.compare.quoteEm}</em>`;

  // Platform Creator Lab
  const platEyebrow = document.querySelector(".platform > .section-head span");
  if (platEyebrow) platEyebrow.textContent = t.platform.eyebrow;
  const platH2 = document.querySelector(".platform > .section-head h2");
  if (platH2) platH2.innerHTML = `${t.platform.title}<br><em>${t.platform.titleEm}</em>`;
  const platP = document.querySelector(".platform > .section-head p");
  if (platP) platP.textContent = t.platform.body;

  const creatorChip = document.querySelector(".creator__copy .chip");
  if (creatorChip) creatorChip.textContent = t.platform.creator.chip;
  const creatorH3 = document.querySelector(".creator__copy h3");
  if (creatorH3) creatorH3.innerHTML = `${t.platform.creator.title}<br><em>${t.platform.creator.titleEm}</em>`;
  const creatorP = document.querySelector(".creator__copy-details p");
  if (creatorP) creatorP.textContent = t.platform.creator.body;
  const creatorBullets = document.querySelectorAll(".creator__copy-details ul li");
  t.platform.creator.bullets.forEach((b, idx) => {
    if (creatorBullets[idx]) creatorBullets[idx].textContent = b;
  });

  // Gallery
  const galEyebrow = document.querySelector(".creation-gallery__head span");
  if (galEyebrow) galEyebrow.textContent = t.platform.gallery.eyebrow;
  const galH3 = document.querySelector(".creation-gallery__head h3");
  if (galH3) galH3.innerHTML = `${t.platform.gallery.title}<br><em>${t.platform.gallery.titleEm}</em>`;
  const galP = document.querySelector(".creation-gallery__head p");
  if (galP) galP.textContent = t.platform.gallery.body;

  // Tour
  const tourEyebrow = document.querySelector(".product-tour-heading span");
  if (tourEyebrow) tourEyebrow.textContent = t.platform.tour.eyebrow;
  const tourH3 = document.querySelector(".product-tour-heading h3");
  if (tourH3) tourH3.innerHTML = `${t.platform.tour.title} <em>${t.platform.tour.titleEm}</em>`;
  const tourTop = document.querySelector(".product-tour__topline strong");
  if (tourTop) tourTop.textContent = t.platform.tour.topline;
  const tourTopSub = document.querySelector(".product-tour__topline p");
  if (tourTopSub) tourTopSub.textContent = t.platform.tour.toplineSub;
  renderTourPanel();

  // Audience / Pra quem é
  const audEyebrow = document.querySelector(".for-you .section-head span");
  if (audEyebrow) audEyebrow.textContent = t.audience.eyebrow;
  const audH2 = document.querySelector(".for-you .section-head h2");
  if (audH2) audH2.textContent = t.audience.title;
  renderAudienceCards();
  const audFooterStrong = document.querySelector(".audience-clean__footer strong");
  if (audFooterStrong) audFooterStrong.textContent = t.audience.footerStrong;
  const audCta = document.querySelector(".audience-clean__footer .cta span");
  if (audCta) audCta.textContent = t.audience.cta;

  // Proofs
  const proofEyebrow = document.querySelector(".proof-wrap .section-head span");
  if (proofEyebrow) proofEyebrow.textContent = t.proof.eyebrow;
  const proofH2 = document.querySelector(".proof-wrap .section-head h2");
  if (proofH2) proofH2.innerHTML = `${t.proof.title}<br><em>${t.proof.titleEm}</em>`;
  const proofSummary = document.querySelector(".proof-wrap .proof-summary");
  if (proofSummary) proofSummary.innerHTML = `${t.proof.summary}<strong>${t.proof.summaryStrong}</strong>`;
  renderProofOrbit();

  // Tool Cost
  const costEyebrow = document.querySelector(".tool-cost__head span");
  if (costEyebrow) costEyebrow.textContent = t.toolCost.eyebrow;
  const costH2 = document.querySelector(".tool-cost__head h2");
  if (costH2) costH2.innerHTML = `${t.toolCost.title}<br><em>${t.toolCost.titleEm}</em>`;
  const costBody = document.querySelector(".tool-cost__head p");
  if (costBody) costBody.textContent = t.toolCost.body;
  renderToolCost();

  // Pricing
  const priceEyebrow = document.querySelector(".pricing .section-head span");
  if (priceEyebrow) priceEyebrow.textContent = t.pricing.eyebrow;
  const priceH2 = document.querySelector(".pricing .section-head h2");
  if (priceH2) priceH2.innerHTML = `${t.pricing.title}<br><em>${t.pricing.titleEm}</em>`;
  const priceBody = document.querySelector(".pricing .section-head p");
  if (priceBody) priceBody.textContent = t.pricing.body;
  renderPricingGrid();

  // FAQ
  const faqEyebrow = document.querySelector(".faq__intro span");
  if (faqEyebrow) faqEyebrow.textContent = t.faq.eyebrow;
  const faqH2 = document.querySelector(".faq__intro h2");
  if (faqH2) faqH2.innerHTML = `${t.faq.title}<br><em>${t.faq.titleEm}</em>`;
  const faqBody = document.querySelector(".faq__intro p");
  if (faqBody) faqBody.textContent = t.faq.body;
  renderFAQList();

  // Final
  const finalChip = document.querySelector(".final .chip");
  if (finalChip) finalChip.textContent = t.final.chip;
  const finalH2 = document.querySelector(".final h2");
  if (finalH2) finalH2.innerHTML = `${t.final.title}<br><em>${t.final.titleEm}</em>`;
  const finalP = document.querySelector(".final__content > p");
  if (finalP) finalP.textContent = t.final.body;
  const finalH3 = document.querySelector(".final h3");
  if (finalH3) finalH3.innerHTML = `${t.final.question}<br><strong>${t.final.answer}</strong>`;
  const finalCta = document.querySelector(".final .cta span");
  if (finalCta) finalCta.textContent = t.final.cta;
  const finalMicro = document.querySelector(".final small");
  if (finalMicro) finalMicro.innerHTML = `${t.final.micro[0]} <i></i> ${t.final.micro[1]} <i></i> ${t.final.micro[2]}`;

  // Footer
  const footerTagline = document.querySelector(".footer p");
  if (footerTagline) footerTagline.textContent = t.footer.tagline;
  const footerRights = document.querySelector(".footer span");
  if (footerRights) footerRights.textContent = t.footer.rights;
}

// 1. Language Toggle
function initLanguage() {
  document.querySelectorAll(".nav__lang button").forEach(btn => {
    btn.addEventListener("click", () => {
      const targetLang = btn.getAttribute("data-lang");
      if (targetLang && targetLang !== state.lang) {
        state.lang = targetLang;
        renderAll();
      }
    });
  });
}

// 2. Mobile Menu Toggle
function initMobileMenu() {
  const menuBtn = document.querySelector(".menu");
  const navLinks = document.querySelector(".nav__links");
  if (!menuBtn || !navLinks) return;

  menuBtn.addEventListener("click", () => {
    state.menuOpen = !state.menuOpen;
    navLinks.classList.toggle("is-open", state.menuOpen);
    menuBtn.setAttribute("aria-expanded", String(state.menuOpen));
  });

  navLinks.querySelectorAll("a").forEach(a => {
    a.addEventListener("click", () => {
      state.menuOpen = false;
      navLinks.classList.remove("is-open");
      menuBtn.setAttribute("aria-expanded", "false");
    });
  });
}

// 3. Pain Carousel
function renderPainCards() {
  const t = getT();
  const grid = document.querySelector(".pain-grid");
  if (!grid) return;
  grid.style.transform = `translate3d(-${state.painIndex * 100}%, 0, 0)`;

  const dotsContainer = document.querySelector(".pain-controls > div");
  if (dotsContainer) {
    dotsContainer.innerHTML = t.pains.items.map((_, i) => `
      <button type="button" class="${state.painIndex === i ? "is-active" : ""}" aria-label="${interpolate(t.a11y.goToPain, { n: i + 1 })}"></button>
    `).join("");

    dotsContainer.querySelectorAll("button").forEach((btn, idx) => {
      btn.addEventListener("click", () => {
        state.painIndex = idx;
        renderPainCards();
      });
    });
  }
}

function initPainCarousel() {
  const carousel = document.querySelector(".pain-carousel");
  const prevBtn = document.querySelector(".pain-controls button:first-of-type");
  const nextBtn = document.querySelector(".pain-controls button:last-of-type");
  const t = getT();

  if (prevBtn) {
    prevBtn.addEventListener("click", () => {
      const len = t.pains.items.length;
      state.painIndex = (state.painIndex - 1 + len) % len;
      renderPainCards();
    });
  }
  if (nextBtn) {
    nextBtn.addEventListener("click", () => {
      const len = t.pains.items.length;
      state.painIndex = (state.painIndex + 1) % len;
      renderPainCards();
    });
  }

  if (carousel) {
    let touchStartX = 0;
    let touchStartY = 0;

    carousel.addEventListener("touchstart", e => {
      touchStartX = e.touches[0].clientX;
      touchStartY = e.touches[0].clientY;
    }, { passive: true });

    carousel.addEventListener("touchend", e => {
      const dx = e.changedTouches[0].clientX - touchStartX;
      const dy = e.changedTouches[0].clientY - touchStartY;
      if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy)) {
        const len = t.pains.items.length;
        if (dx < 0) {
          state.painIndex = (state.painIndex + 1) % len;
        } else {
          state.painIndex = (state.painIndex - 1 + len) % len;
        }
        renderPainCards();
      }
    }, { passive: true });

    carousel.addEventListener("wheel", e => {
      if (Math.abs(e.deltaY) > Math.abs(e.deltaX) && Math.abs(e.deltaY) > 25) {
        const len = t.pains.items.length;
        if (e.deltaY > 0 && state.painIndex < len - 1) {
          state.painIndex++;
          renderPainCards();
        } else if (e.deltaY < 0 && state.painIndex > 0) {
          state.painIndex--;
          renderPainCards();
        }
      }
    }, { passive: true });
  }
}

// 4. Product Tour
function renderTourPanel() {
  const t = getT();
  const curMod = MODULES[state.tourIndex];
  const curDemo = t.platform.tour.demos[state.tourIndex];
  if (!curMod || !curDemo) return;

  // Tabs
  const tabs = document.querySelectorAll(".product-tour__tabs button");
  tabs.forEach((tab, idx) => {
    tab.classList.toggle("is-active", idx === state.tourIndex);
    tab.setAttribute("aria-selected", String(idx === state.tourIndex));
    const small = tab.querySelector("small");
    if (small && t.platform.tour.demos[idx]) {
      small.textContent = t.platform.tour.demos[idx].title;
    }
  });

  // Screenshot image
  const img = document.querySelector(".product-tour__image img");
  if (img) {
    img.src = curMod.image;
    img.alt = curDemo.imageAlt;
  }

  // Counter
  const countEl = document.querySelector(".product-tour__screen-nav p b");
  if (countEl) countEl.textContent = `0${state.tourIndex + 1}`;

  // Guide Aside
  const guideHeaderSpan = document.querySelector(".product-tour__guide header span");
  if (guideHeaderSpan) guideHeaderSpan.textContent = `0${state.tourIndex + 1} / 0${MODULES.length} · ${curMod.tag}`;
  const guideH3 = document.querySelector(".product-tour__guide header h3");
  if (guideH3) guideH3.textContent = curDemo.title;
  const guideP = document.querySelector(".product-tour__guide header p");
  if (guideP) guideP.textContent = curDemo.description;

  const solvesLabel = document.querySelector(".product-tour__capabilities small");
  if (solvesLabel) solvesLabel.textContent = t.platform.tour.labelSolves;

  const ul = document.querySelector(".product-tour__capabilities ul");
  if (ul) {
    ul.innerHTML = curDemo.benefits.map((b, i) => `
      <li><i>0${i + 1}</i><span>${b}</span></li>
    `).join("");
  }

  const outcomeSpan = document.querySelector(".product-tour__outcome span");
  if (outcomeSpan) outcomeSpan.textContent = t.platform.tour.labelOutcome;
  const outcomeP = document.querySelector(".product-tour__outcome p");
  if (outcomeP) outcomeP.textContent = curDemo.outcome;
}

function initProductTour() {
  document.querySelectorAll(".product-tour__tabs button").forEach((btn, idx) => {
    btn.addEventListener("click", () => {
      state.tourIndex = idx;
      renderTourPanel();
    });
  });

  document.querySelectorAll(".product-tour__arrow--previous, .product-tour__screen-nav button:first-of-type").forEach(btn => {
    btn.addEventListener("click", () => {
      state.tourIndex = (state.tourIndex - 1 + MODULES.length) % MODULES.length;
      renderTourPanel();
    });
  });

  document.querySelectorAll(".product-tour__arrow--next, .product-tour__screen-nav button:last-of-type").forEach(btn => {
    btn.addEventListener("click", () => {
      state.tourIndex = (state.tourIndex + 1) % MODULES.length;
      renderTourPanel();
    });
  });
}

// 5. Creator Lab Video
function initCreatorLabVideo() {
  const video = document.querySelector(".creator-pipeline__card--result video");
  const soundBtn = document.querySelector(".creator-pipeline__sound");
  if (!video || !soundBtn) return;

  soundBtn.addEventListener("click", () => {
    video.muted = false;
    video.volume = 1;
    state.videoSoundActive = true;
    soundBtn.style.display = "none";
    video.play().catch(() => {});
  });
}

// 6. Audience Cards
function renderAudienceCards() {
  const t = getT();
  const cards = document.querySelectorAll(".audience-card");
  t.audience.items.forEach((item, idx) => {
    const c = cards[idx];
    if (c) {
      const h3 = c.querySelector("h3");
      if (h3) h3.textContent = item.title;
      const p = c.querySelector(".card-solution p");
      if (p) p.textContent = item.body;
      const small = c.querySelector("small");
      if (small) small.textContent = `0${idx + 1}`;
    }
  });
}

// 7. Story Rails & Video Lightbox Trigger
function initStoryRails() {
  // Lazy play videos on hover or view
  document.querySelectorAll(".story-rail .story-video").forEach((btn, idx) => {
    btn.addEventListener("click", () => {
      const videoData = STORY_VIDEOS[idx % STORY_VIDEOS.length];
      if (videoData) {
        openLightbox(videoData.src, videoData.poster);
      }
    });
  });
}

// 8. Proof Orbit
function renderProofOrbit() {
  const t = getT();
  const shots = document.querySelectorAll(".proof-orbit__shot");
  const len = PROOFS.length;

  shots.forEach((shot, idx) => {
    let r = idx - state.proofIndex;
    let offset = r > len / 2 ? r - len : r < -len / 2 ? r + len : r;
    shot.style.setProperty("--offset", offset);
    shot.classList.toggle("is-active", offset === 0);
  });

  const readoutMetric = document.querySelector(".proof-orbit__readout strong");
  const readoutP = document.querySelector(".proof-orbit__readout p");
  if (readoutMetric) readoutMetric.textContent = t.proof.shots[state.proofIndex]?.metric || "";
  if (readoutP) readoutP.textContent = t.proof.shots[state.proofIndex]?.label || "";

  const dots = document.querySelectorAll(".proof-orbit__dots button");
  dots.forEach((d, idx) => {
    d.classList.toggle("is-active", idx === state.proofIndex);
  });
}

function initProofOrbit() {
  const prev = document.querySelector(".proof-orbit__readout span button:first-of-type");
  const next = document.querySelector(".proof-orbit__readout span button:last-of-type");
  const len = PROOFS.length;

  if (prev) {
    prev.addEventListener("click", () => {
      state.proofIndex = (state.proofIndex - 1 + len) % len;
      renderProofOrbit();
    });
  }
  if (next) {
    next.addEventListener("click", () => {
      state.proofIndex = (state.proofIndex + 1) % len;
      renderProofOrbit();
    });
  }

  document.querySelectorAll(".proof-orbit__dots button").forEach((d, idx) => {
    d.addEventListener("click", () => {
      state.proofIndex = idx;
      renderProofOrbit();
    });
  });

  document.querySelectorAll(".proof-orbit__shot").forEach((shot, idx) => {
    shot.addEventListener("click", () => {
      state.proofIndex = idx;
      renderProofOrbit();
    });
  });
}

// 9. Tool Cost Breakdown
function renderToolCost() {
  const t = getT();
  const articles = document.querySelectorAll(".tool-cost__list article");
  TOOLS.forEach((tool, idx) => {
    const a = articles[idx];
    if (a) {
      const purp = a.querySelector("div span");
      if (purp) purp.textContent = t.toolCost.purposes[idx];
      const small = a.querySelector("b small");
      if (small) small.textContent = t.toolCost.perMonth;
    }
  });

  const asideEyebrow = document.querySelector(".tool-cost__voomi > span");
  if (asideEyebrow) asideEyebrow.textContent = t.toolCost.voomiEyebrow;
  const asideH3 = document.querySelector(".tool-cost__voomi h3");
  if (asideH3) asideH3.innerHTML = `${t.toolCost.voomiTitle}<br>${t.toolCost.voomiTitleLine2}`;

  const asideBullets = document.querySelectorAll(".tool-cost__voomi ul li");
  t.toolCost.voomiBullets.forEach((b, idx) => {
    if (asideBullets[idx]) asideBullets[idx].innerHTML = `<i>✓</i> ${b}`;
  });

  const note = document.querySelector(".tool-cost__note");
  if (note) note.textContent = t.toolCost.note;
}

// 10. Pricing Grid & Creator Coupon System
function renderPricingGrid() {
  const t = getT();
  const prices = state.activeCoupon ? PRICING_CREATOR : PRICING_STANDARD;
  const isCreator = !!state.activeCoupon;

  const cards = document.querySelectorAll(".pricing-card");
  if (cards.length >= 3) {
    // 1. Monthly
    const cMonthly = cards[0];
    cMonthly.querySelector(".pricing-card__head small").textContent = t.pricing.monthly.eyebrow;
    cMonthly.querySelector(".pricing-card__head h3").textContent = t.pricing.monthly.name;
    cMonthly.querySelector(".pricing-card__head p").textContent = t.pricing.monthly.description;
    cMonthly.querySelector(".pricing-card__price strong").textContent = formatCurrency(prices.monthly);
    cMonthly.querySelector(".pricing-card__price small").textContent = t.pricing.monthly.cycle;
    cMonthly.querySelector(".pricing-card__cta span").textContent = t.pricing.monthly.cta;
    cMonthly.querySelector(".pricing-card__cta").href = DEFAULT_LINKS.monthly;

    // 2. Annual (Featured)
    const cAnnual = cards[1];
    cAnnual.querySelector(".pricing-card__head small").textContent = t.pricing.annual.eyebrow;
    cAnnual.querySelector(".pricing-card__head h3").textContent = t.pricing.annual.name;
    cAnnual.querySelector(".pricing-card__head p").textContent = t.pricing.annual.description;
    cAnnual.querySelector(".pricing-card__price b").textContent = t.pricing.installmentsPrefix;
    cAnnual.querySelector(".pricing-card__price strong").textContent = formatCurrency(calculateInstallment(prices.annual));
    cAnnual.querySelector(".pricing-card__cash").textContent = interpolate(t.pricing.cash, { v: formatCurrency(prices.annual) });
    cAnnual.querySelector(".pricing-card__cta span").textContent = t.pricing.annual.cta;
    cAnnual.querySelector(".pricing-card__cta").href = DEFAULT_LINKS.annual;

    if (isCreator) {
      const compareEl = cAnnual.querySelector(".pricing-card__compare");
      if (compareEl) {
        compareEl.style.display = "flex";
        compareEl.innerHTML = `<s>R$ ${formatCurrency(calculateInstallment(PRICING_STANDARD.annual))}</s> <em>-42% OFF</em>`;
      }
    } else {
      const compareEl = cAnnual.querySelector(".pricing-card__compare");
      if (compareEl) compareEl.style.display = "none";
    }

    // 3. Lifetime / Special
    const cLife = cards[2];
    cLife.querySelector(".pricing-card__head small").textContent = t.pricing.lifetime.eyebrow;
    cLife.querySelector(".pricing-card__head h3").textContent = t.pricing.lifetime.name;
    cLife.querySelector(".pricing-card__head p").textContent = t.pricing.lifetime.description;
    cLife.querySelector(".pricing-card__price b").textContent = t.pricing.installmentsPrefix;
    cLife.querySelector(".pricing-card__price strong").textContent = formatCurrency(calculateInstallment(prices.lifetime));
    cLife.querySelector(".pricing-card__cash").textContent = interpolate(t.pricing.cash, { v: formatCurrency(prices.lifetime) });
    cLife.querySelector(".pricing-card__cta span").textContent = t.pricing.lifetime.cta;
    cLife.querySelector(".pricing-card__cta").href = DEFAULT_LINKS.lifetime;

    if (isCreator) {
      const compareEl = cLife.querySelector(".pricing-card__compare");
      if (compareEl) {
        compareEl.style.display = "flex";
        compareEl.innerHTML = `<s>R$ ${formatCurrency(calculateInstallment(PRICING_STANDARD.lifetime))}</s> <em>-50% OFF</em>`;
      }
    } else {
      const compareEl = cLife.querySelector(".pricing-card__compare");
      if (compareEl) compareEl.style.display = "none";
    }
  }

  // Guarantee Note
  const noteStrong = document.querySelector(".pricing-note strong");
  if (noteStrong) noteStrong.textContent = t.pricing.noteStrong;
  const noteBody = document.querySelector(".pricing-note span");
  if (noteBody) noteBody.textContent = t.pricing.noteBody;
}

function initCouponSystem() {
  const form = document.querySelector(".coupon-box");
  const input = document.querySelector(".coupon-box input");
  const button = document.querySelector(".coupon-box button");
  const errorP = document.querySelector(".coupon-box__error");
  const t = getT();

  if (!form || !input) return;

  form.addEventListener("submit", e => {
    e.preventDefault();
    const code = input.value.trim().toUpperCase();
    if (!code) return;

    button.disabled = true;
    button.textContent = t.pricing.coupon.checking;

    setTimeout(() => {
      button.disabled = false;
      button.textContent = t.pricing.coupon.apply;

      // Allow creator coupons (e.g. TIKTOK, CREATOR, VOOMI, DESCONTO, VIP)
      if (code.length >= 3) {
        state.activeCoupon = code;
        renderPricingGrid();
        showCouponApplied(code);
      } else {
        if (errorP) {
          errorP.style.display = "block";
          errorP.textContent = t.pricing.coupon.invalid;
        }
      }
    }, 600);
  });
}

function showCouponApplied(code) {
  const t = getT();
  const form = document.querySelector(".coupon-box");
  if (!form) return;

  const aside = document.createElement("aside");
  aside.className = "creator-offer";
  aside.innerHTML = `
    <span class="chip">⚡ ${t.pricing.coupon.eyebrow}</span>
    <h3>${t.pricing.coupon.title}<br><em>@${code.toLowerCase()}</em></h3>
    <p>${t.pricing.coupon.body}</p>
    <div class="creator-offer__code">
      <small>${t.pricing.coupon.applied}</small>
      <strong>${code}</strong>
    </div>
    <ul>
      <li><i>%</i><span>${interpolate(t.pricing.coupon.discount, { v: "42" })}</span></li>
      <li><i>⚡</i><span>${t.pricing.coupon.unlimited}</span></li>
      <li><i>👥</i><span>${interpolate(t.pricing.coupon.remaining, { n: "18" })}</span></li>
    </ul>
    <button type="button" class="creator-offer__remove">${t.pricing.coupon.remove}</button>
  `;

  form.parentNode.replaceChild(aside, form);

  aside.querySelector(".creator-offer__remove").addEventListener("click", () => {
    state.activeCoupon = null;
    renderPricingGrid();
    aside.parentNode.replaceChild(form, aside);
  });
}

// 11. FAQ Accordion
function renderFAQList() {
  const t = getT();
  const items = document.querySelectorAll(".faq__list article");
  t.faq.items.forEach((item, idx) => {
    const art = items[idx];
    if (art) {
      const b = art.querySelector("button b");
      if (b) b.textContent = item.q;
      const p = art.querySelector("div p");
      if (p) p.textContent = item.a;
    }
  });
}

function initFAQ() {
  const articles = document.querySelectorAll(".faq__list article");
  articles.forEach((art, idx) => {
    const btn = art.querySelector("button");
    if (!btn) return;
    btn.addEventListener("click", () => {
      const isOpen = art.classList.contains("open");
      articles.forEach(a => {
        a.classList.remove("open");
        const icon = a.querySelector("button i");
        if (icon) icon.textContent = "+";
      });

      if (!isOpen) {
        art.classList.add("open");
        const icon = art.querySelector("button i");
        if (icon) icon.textContent = "−";
      }
    });
  });
}

// 12. Video Lightbox
function initLightbox() {
  const lightbox = document.querySelector(".video-lightbox");
  if (!lightbox) return;

  const closeBtn = lightbox.querySelector("button");
  if (closeBtn) {
    closeBtn.addEventListener("click", closeLightbox);
  }

  lightbox.addEventListener("click", e => {
    if (e.target === lightbox) closeLightbox();
  });

  document.addEventListener("keydown", e => {
    if (e.key === "Escape") closeLightbox();
  });
}

function openLightbox(src, poster) {
  const lightbox = document.querySelector(".video-lightbox");
  const video = lightbox ? lightbox.querySelector("video") : null;
  if (!lightbox || !video) return;

  video.src = src;
  if (poster) video.poster = poster;
  lightbox.style.display = "grid";
  document.body.style.overflow = "hidden";
  video.currentTime = 0;
  video.muted = false;
  video.play().catch(() => {});
}

function closeLightbox() {
  const lightbox = document.querySelector(".video-lightbox");
  const video = lightbox ? lightbox.querySelector("video") : null;
  if (!lightbox) return;

  lightbox.style.display = "none";
  document.body.style.overflow = "";
  if (video) {
    video.pause();
    video.src = "";
  }
}

// 13. Scroll Reveal Animations
function initScrollReveal() {
  const revealEls = document.querySelectorAll("[data-reveal]");
  if (!("IntersectionObserver" in window)) {
    revealEls.forEach(el => el.classList.add("is-visible"));
    return;
  }

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        obs.unobserve(entry.target);
      }
    });
  }, { rootMargin: "0px 0px -10% 0px" });

  revealEls.forEach(el => observer.observe(el));
}

// 14. Mouse Glow on Cards
function initMouseGlow() {
  const cards = document.querySelectorAll(".pain-card, .audience-card");
  cards.forEach(card => {
    const glow = document.createElement("div");
    glow.className = "card-glow";
    card.style.position = "relative";
    card.prepend(glow);

    card.addEventListener("mousemove", e => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      glow.style.left = `${x - 130}px`;
      glow.style.top = `${y - 130}px`;
    });
  });
}
"""

with open("/Users/raypires/.gemini/antigravity/scratch/voomi-clone/app.js", "w") as f:
    f.write(app_content)

print("Generated app.js, size:", len(app_content))
