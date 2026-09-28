import os
import urllib.request
import urllib.error

BASE_URL = "https://voomi.app.br"
SUPABASE_STORAGE = "https://omlwqrtqivqcgrrlrlzf.supabase.co/storage/v1/object/public/landing-media"
DEST_DIR = "/Users/raypires/.gemini/antigravity/scratch/voomi-clone"

ASSETS = [
    # Favicons and manifest
    "/favicon.svg",
    "/favicon-32x32.png",
    "/favicon-16x16.png",
    "/apple-touch-icon.png",
    "/site.webmanifest",
    
    # Fonts
    "/assets/bebas-neue-latin-400-normal-9mHNbWWO.woff2",
    "/assets/space-grotesk-latin-400-normal-CJ-V5oYT.woff2",
    "/assets/space-grotesk-latin-500-normal-lFbtlQH6.woff2",
    "/assets/space-grotesk-latin-600-normal-DjKNqYRj.woff2",
    "/assets/space-grotesk-latin-700-normal-RjhwGPKo.woff2",
    
    # Avatars & Hero
    "/lp/avatar-02.webp",
    "/lp/avatar-05.webp",
    "/lp/avatar-ai-01.webp",
    "/lp/avatar-ai-02.webp",
    "/lp/avatar-ai-03.webp",
    
    # Creator Lab
    "/lp/creator-lab-scenario.webp",
    "/lp/creator-lab-product.webp",
    "/lp/creator-lab-avatar.webp",
    "/lp/creator-lab-result-poster.jpg",
    
    # Modules
    "/lp/module-motion-full.webp",
    "/lp/module-radar-full.webp",
    "/lp/module-boost-full.webp",
    "/lp/module-avatar-full.webp",
    "/lp/module-studio-full.webp",
    
    # Outcome Bridge
    "/lp/voomi-outcome-product.webp",
    "/lp/voomi-outcome-avatar.webp",
    "/lp/proof-tiktok-shop-results.webp",
    
    # Tools
    "/lp/tools/canva.ico",
    "/lp/tools/capcut.ico",
    "/lp/tools/chatgpt.svg",
    "/lp/tools/heygen.ico",
    "/lp/tools/minea.png",
    
    # Video posters
    "/lp/voomi-video-01-poster.webp",
    "/lp/voomi-video-02-poster.webp",
    "/lp/voomi-video-04-poster.jpg",
    "/lp/voomi-video-05-poster.jpg",
    "/lp/videos/voomi-testimonial-07-poster.webp",
    "/lp/videos/voomi-testimonial-08-poster.webp",
    "/lp/videos/creation-gallery-cookware-poster.webp",
    "/lp/videos/creation-gallery-01-poster.webp",
    "/lp/videos/creation-gallery-02-poster.webp",
    "/lp/videos/creation-gallery-03-poster.webp",
    "/lp/videos/creation-gallery-04-poster.webp",
    "/lp/videos/creation-gallery-05-poster.webp",
    "/lp/videos/creation-gallery-06-poster.webp",
    
    # Proofs
    "/lp/proofs/proof-primeira-venda.webp",
    "/lp/proofs/proof-512-vinte-vendas.webp",
    "/lp/proofs/proof-feedback-tenis.webp",
    "/lp/proofs/proof-374-seis-vendas.webp",
    "/lp/proofs/proof-mil-24-vendas.webp",
    "/lp/proofs/proof-primeira-venda-euro.webp",
    
    # Sounds
    "/sounds/cash.mp3",
    "/sounds/coin.mp3",
    "/sounds/ding.mp3",
    "/sounds/money.mp3",
    "/sounds/success.mp3",
]

VIDEOS = [
    "voomi-video-01.mp4",
    "voomi-video-02.mp4",
    "voomi-video-04.mp4",
    "voomi-video-05.mp4",
    "voomi-testimonial-07.mp4",
    "voomi-testimonial-08.mp4",
    "creation-gallery-cookware.mp4",
    "creation-gallery-01.mp4",
    "creation-gallery-02.mp4",
    "creation-gallery-03.mp4",
    "creation-gallery-04.mp4",
    "creation-gallery-05.mp4",
    "creation-gallery-06.mp4",
    "creator-lab-result.mp4",
]

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

print("=== Downloading static assets from voomi.app.br ===")
success = 0
failed = []

for rel_path in ASSETS:
    local_path = os.path.join(DEST_DIR, rel_path.lstrip("/"))
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    
    url = BASE_URL + rel_path
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read()
            with open(local_path, "wb") as f:
                f.write(content)
            print(f"[OK] {rel_path} ({len(content)} bytes)")
            success += 1
    except Exception as e:
        print(f"[ERR] {rel_path}: {e}")
        failed.append(rel_path)

print(f"\nDownloaded {success} assets, {len(failed)} failed.")

print("\n=== Downloading videos from Supabase storage ===")
video_success = 0
for v in VIDEOS:
    url = f"{SUPABASE_STORAGE}/{v}"
    local_path = os.path.join(DEST_DIR, "lp/videos", v)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            content = resp.read()
            with open(local_path, "wb") as f:
                f.write(content)
            print(f"[OK] Video {v} ({len(content)} bytes)")
            video_success += 1
    except Exception as e:
        print(f"[ERR] Video {v}: {e}")

print(f"\nDownloaded {video_success} videos.")
