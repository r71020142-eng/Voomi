import json
import re

# Read aux_dump.js to get su
with open("/Users/raypires/.gemini/antigravity/brain/9fc1d89e-e22c-44e8-823b-a8e1f6e34e59/scratch/aux_dump.js") as f:
    aux = f.read()

idx_pt = aux.find("su={pt:{")
if idx_pt == -1: idx_pt = aux.find("var su={pt:{")
idx_end = aux.find(",cu=e=>e===`pt`")
if idx_end == -1: idx_end = aux.find(";function uu(")

su_js = aux[idx_pt:idx_end]
if su_js.startswith("var "):
    su_js = su_js[4:]

# Clean up JS object to make it executable in JS
app_js_header = f"""/**
 * Voomi.app.br - 100% Faithful Recreated Engine
 * Full Bilingual Support, Interactive Modules, Carousels, Video Lightbox, and Pricing Engine
 */

const {su_js};

const MODULES = [
  {{ id: "motion", tag: "MOTION", image: "/lp/module-motion-full.webp" }},
  {{ id: "radar", tag: "RADAR", image: "/lp/module-radar-full.webp" }},
  {{ id: "boost", tag: "BOOST", image: "/lp/module-boost-full.webp" }},
  {{ id: "avatar", tag: "AVATAR", image: "/lp/module-avatar-full.webp" }},
  {{ id: "studio", tag: "STUDIO", image: "/lp/module-studio-full.webp" }}
];

const TOOLS = [
  {{ logo: "/lp/tools/minea.png", name: "Minea Starter", price: "R$ 255,01" }},
  {{ logo: "/lp/tools/heygen.ico", name: "HeyGen Creator", price: "R$ 150,92" }},
  {{ logo: "/lp/tools/chatgpt.svg", name: "ChatGPT Plus", price: "R$ 104,09" }},
  {{ logo: "/lp/tools/capcut.ico", name: "CapCut Pro", price: "R$ 104,03" }},
  {{ logo: "/lp/tools/canva.ico", name: "Canva Pro", price: "R$ 62,45" }}
];

const STORY_VIDEOS = [
  {{ src: "/lp/videos/voomi-video-01.mp4", poster: "/lp/voomi-video-01-poster.webp", testimonial: false }},
  {{ src: "/lp/videos/voomi-video-02.mp4", poster: "/lp/voomi-video-02-poster.webp", testimonial: false }},
  {{ src: "/lp/videos/voomi-video-04.mp4", poster: "/lp/voomi-video-04-poster.jpg", testimonial: false }},
  {{ src: "/lp/videos/voomi-video-05.mp4", poster: "/lp/voomi-video-05-poster.jpg", testimonial: false }},
  {{ src: "/lp/videos/voomi-testimonial-07.mp4", poster: "/lp/videos/voomi-testimonial-07-poster.webp", testimonial: true }},
  {{ src: "/lp/videos/voomi-testimonial-08.mp4", poster: "/lp/videos/voomi-testimonial-08-poster.webp", testimonial: true }}
];

const GALLERY_VIDEOS = [
  {{ src: "/lp/videos/creation-gallery-cookware.mp4", poster: "/lp/videos/creation-gallery-cookware-poster.webp" }},
  {{ src: "/lp/videos/creation-gallery-01.mp4", poster: "/lp/videos/creation-gallery-01-poster.webp" }},
  {{ src: "/lp/videos/creation-gallery-02.mp4", poster: "/lp/videos/creation-gallery-02-poster.webp" }},
  {{ src: "/lp/videos/creation-gallery-03.mp4", poster: "/lp/videos/creation-gallery-03-poster.webp" }},
  {{ src: "/lp/videos/creation-gallery-04.mp4", poster: "/lp/videos/creation-gallery-04-poster.webp" }},
  {{ src: "/lp/videos/creation-gallery-05.mp4", poster: "/lp/videos/creation-gallery-05-poster.webp" }},
  {{ src: "/lp/videos/creation-gallery-06.mp4", poster: "/lp/videos/creation-gallery-06-poster.webp" }}
];

const PROOFS = [
  "/lp/proofs/proof-primeira-venda.webp",
  "/lp/proofs/proof-512-vinte-vendas.webp",
  "/lp/proofs/proof-feedback-tenis.webp",
  "/lp/proofs/proof-374-seis-vendas.webp",
  "/lp/proofs/proof-mil-24-vendas.webp",
  "/lp/proofs/proof-primeira-venda-euro.webp"
];

const DEFAULT_LINKS = {{
  monthly: "https://checkout.applyfy.com.br/checkout/cmoj54j7f0czv1rqrkgh7lk7y?offer=FYN96AM",
  annual: "https://checkout.applyfy.com.br/checkout/cmok3u6hj0cwh1rqqhzivg0c9?offer=R9VNPCI",
  lifetime: "https://checkout.applyfy.com.br/checkout/cmok3u6hj0cwh1rqqhzivg0c9?offer=R9VNPCI"
}};

const PRICING_STANDARD = {{ monthly: 297, annual: 597, lifetime: 697 }};
const PRICING_CREATOR  = {{ monthly: 147, annual: 347, lifetime: 347 }};
const INSTALLMENT_FACTOR = 1.2786;

function formatCurrency(val) {{
  return val.toLocaleString("pt-BR", {{ minimumFractionDigits: 2, maximumFractionDigits: 2 }});
}}

function calculateInstallment(total) {{
  return (total * INSTALLMENT_FACTOR) / 12;
}}

function interpolate(tpl, vars) {{
  return tpl.replace(/\\{{(\\w+)\\}}/g, (_, k) => String(vars[k] ?? `\\{{${{k}}\\}`));
}}
"""

with open("/Users/raypires/.gemini/antigravity/scratch/voomi-clone/app_header.js", "w") as f:
    f.write(app_js_header)

print("Generated app_header.js successfully")
