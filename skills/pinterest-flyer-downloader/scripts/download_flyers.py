import os
import sys
import shutil
import hashlib
import argparse
import subprocess
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from PIL import Image

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

PYTHON_EXE = r"C:\Users\migue\AppData\Local\Python\pythoncore-3.14-64\python.exe"
DEFAULT_OUTPUT_DIR = Path(r"C:\Users\migue\Pictures\flyers pinterest")

# Predefined high-quality non-AI queries per domain
DOMAINS = {
    "01_Etudes_Formation": {
        "prefix": "etudes_formation",
        "queries": [
            "education flyer indesign template -ai",
            "university admission flyer brochure vector -ai",
            "academic training courses flyer template -ai",
            "study abroad flyer behance vector -ai"
        ]
    },
    "02_Pole_Technique_IT": {
        "prefix": "technique_it",
        "queries": [
            "tech conference poster flyer vector behance -ai",
            "IT software company flyer indesign template -ai",
            "engineering technology flyer print template -ai",
            "cybersecurity digital summit flyer vector -ai"
        ]
    },
    "03_Industrie_Manufacture": {
        "prefix": "industrie_manufacture",
        "queries": [
            "industrial manufacturing flyer indesign template -ai",
            "construction company flyer vector behance -ai",
            "engineering factory print flyer template -ai",
            "logistics energy industry flyer vector -ai"
        ]
    },
    "04_Agriculture_Agroalimentaire": {
        "prefix": "agriculture_agro",
        "queries": [
            "agriculture farming flyer indesign template -ai",
            "agribusiness organic farm market flyer vector -ai",
            "smart farming agronomy flyer design -ai",
            "farm produce harvest flyer template -ai"
        ]
    },
    "05_Business_Corporate": {
        "prefix": "business_corporate",
        "queries": [
            "corporate business flyer indesign vector template -ai",
            "finance consulting flyer template behance -ai",
            "marketing agency flyer layout template -ai",
            "startup business company flyer illustrator -ai"
        ]
    },
    "06_Sante_Medical": {
        "prefix": "sante_medical",
        "queries": [
            "medical clinic healthcare flyer indesign -ai",
            "dental hospital health flyer vector -ai",
            "pharmacy medical care flyer print template -ai",
            "doctor health clinic flyer behance -ai"
        ]
    },
    "07_Evenements_Conferences": {
        "prefix": "evenements_conferences",
        "queries": [
            "business summit conference flyer vector -ai",
            "seminar workshop event poster flyer indesign -ai",
            "tech exhibition expo flyer layout template -ai",
            "corporate gala event flyer behance -ai"
        ]
    },
    "08_Immobilier_Architecture": {
        "prefix": "immobilier_architecture",
        "queries": [
            "real estate architecture flyer template indesign -ai",
            "property sale architectural flyer vector -ai"
        ]
    },
    "09_Restauration_Alimentation": {
        "prefix": "restauration_alimentation",
        "queries": [
            "restaurant menu food flyer vector behance -ai",
            "cafe bakery food promotion flyer indesign -ai"
        ]
    }
}

def file_hash(path: Path) -> str:
    h = hashlib.md5()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def is_valid_flyer(file_path: Path, filter_ai: bool = True) -> bool:
    """Validate image resolution, aspect ratio, and remove common square AI artifacts."""
    try:
        with Image.open(file_path) as img:
            w, h = img.size
            if w < 300 or h < 300:
                return False
            
            if filter_ai:
                # Check EXIF/info metadata
                info_str = str(img.info).lower()
                if any(ai_term in info_str for ai_term in ["midjourney", "stable diffusion", "dall-e", "dalle", "novelai", "civitai", "generative"]):
                    return False
                
                # Standard flyer ratio check (predominantly portrait vertical)
                ratio = h / w
                if ratio < 1.02:
                    return False
            return True
    except Exception:
        return False

def clean_and_rename(category_dir: Path, prefix: str, filter_ai: bool = True):
    valid_exts = {".jpg", ".jpeg", ".png", ".webp"}
    seen_hashes = set()
    
    all_files = []
    for item in category_dir.rglob("*"):
        if item.is_file() and item.suffix.lower() in valid_exts:
            all_files.append(item)
            
    valid_files = []
    for f in all_files:
        if not is_valid_flyer(f, filter_ai=filter_ai):
            try:
                f.unlink()
            except Exception:
                pass
            continue
            
        fhash = file_hash(f)
        if fhash in seen_hashes:
            try:
                f.unlink()
            except Exception:
                pass
            continue
            
        seen_hashes.add(fhash)
        valid_files.append(f)
        
    # Remove empty subdirectories
    for root, dirs, _ in os.walk(category_dir, topdown=False):
        for d in dirs:
            p = Path(root) / d
            try:
                p.rmdir()
            except OSError:
                pass
                
    # Temp rename
    temp_files = []
    for i, f in enumerate(valid_files):
        ext = f.suffix.lower()
        if ext == ".jpeg":
            ext = ".jpg"
        tmp_name = category_dir / f"_tmp_{prefix}_{i+1:05d}{ext}"
        if f != tmp_name:
            try:
                shutil.move(str(f), str(tmp_name))
                temp_files.append(tmp_name)
            except Exception:
                pass
        else:
            temp_files.append(tmp_name)
            
    # Final rename
    for idx, tmp_f in enumerate(temp_files, 1):
        ext = tmp_f.suffix
        final_name = category_dir / f"{prefix}_flyer_{idx:03d}{ext}"
        try:
            if tmp_f != final_name:
                shutil.move(str(tmp_f), str(final_name))
        except Exception:
            pass
            
    return len(temp_files)

def download_query(output_folder: Path, query_or_url: str, count: int):
    if query_or_url.startswith("http://") or query_or_url.startswith("https://"):
        target_url = query_or_url
    else:
        encoded = query_or_url.replace(" ", "%20")
        target_url = f"https://www.pinterest.com/search/pins/?q={encoded}"

    cmd = [
        PYTHON_EXE,
        "-m", "gallery_dl",
        "--range", f"1-{count}",
        "--dest", str(output_folder),
        "--quiet",
        target_url
    ]
    try:
        subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    except Exception:
        pass

def download_domain(domain_name: str, domain_info: dict, base_dir: Path, count_per_query: int, filter_ai: bool):
    cat_dir = base_dir / domain_name
    cat_dir.mkdir(parents=True, exist_ok=True)
    prefix = domain_info["prefix"]
    
    for q in domain_info["queries"]:
        download_query(cat_dir, q, count_per_query)
        
    count = clean_and_rename(cat_dir, prefix, filter_ai=filter_ai)
    return domain_name, count

def main():
    parser = argparse.ArgumentParser(description="Skill CLI: Téléchargeur et organisateur de flyers Pinterest sans IA")
    parser.add_argument("query", nargs="?", default=None, help="Mots-clés de recherche personnalisés ou URL Pinterest")
    parser.add_argument("-d", "--domain", default=None, help="Nom du domaine (ex: '01_Etudes_Formation', 'all' pour tous)")
    parser.add_argument("-n", "--count", type=int, default=20, help="Nombre de flyers par requête/domaine (défaut: 20)")
    parser.add_argument("-o", "--output", default=str(DEFAULT_OUTPUT_DIR), help="Dossier de destination")
    parser.add_argument("--no-ai-filter", action="store_true", help="Désactiver le filtre strict anti-IA")

    args = parser.parse_args()
    dest = Path(args.output)
    dest.mkdir(parents=True, exist_ok=True)
    filter_ai = not args.no_ai_filter

    if args.domain == "all" or (args.domain is None and args.query is None):
        print(f"[*] Téléchargement multi-domaines vers : {dest}")
        total = 0
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [
                executor.submit(download_domain, d_name, d_info, dest, args.count, filter_ai)
                for d_name, d_info in DOMAINS.items()
            ]
            for f in as_completed(futures):
                d_name, count = f.result()
                print(f" [+] {d_name} : {count} flyers organisés")
                total += count
        print(f"\n[OK] TOTAL : {total} flyers téléchargés et classés.")
    elif args.query:
        print(f"[*] Téléchargement direct pour : '{args.query}' ({args.count} flyers)...")
        sub_folder = dest / "custom_search"
        sub_folder.mkdir(parents=True, exist_ok=True)
        download_query(sub_folder, args.query, args.count)
        count = clean_and_rename(sub_folder, "custom", filter_ai=filter_ai)
        print(f"[OK] {count} flyers enregistrés dans {sub_folder}")

if __name__ == "__main__":
    main()
