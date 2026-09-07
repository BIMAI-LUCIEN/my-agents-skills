---
name: pinterest-flyer-downloader
description: >-
  Expert flyer scraper, curator, and organizer for Pinterest. Automatically downloads,
  filters out AI-generated content/artifacts, categorizes flyers by professional domains
  (Education, IT, Industry, Agriculture, Corporate, Healthcare, Events, Real Estate, Food),
  and standardizes file naming with clean sequential numbering.
---

# Pinterest Flyer Downloader & Curator Skill

This skill provides an automated workflow to scrape, filter, categorize, and organize high-resolution flyers from Pinterest while strictly avoiding AI-generated images and poor quality outputs.

## Capabilities
1. **Multi-Domain Automated Scraping**: Parallel fetching across 9+ professional categories:
   - `01_Etudes_Formation` (University, admissions, courses, study abroad)
   - `02_Pole_Technique_IT` (Tech summit, software engineering, cybersecurity)
   - `03_Industrie_Manufacture` (Factories, manufacturing, energy, construction)
   - `04_Agriculture_Agroalimentaire` (Agribusiness, farming, organic market)
   - `05_Business_Corporate` (Marketing agency, finance, consulting)
   - `06_Sante_Medical` (Clinics, hospitals, pharmacy, dental)
   - `07_Evenements_Conferences` (Summits, exhibitions, galas)
   - `08_Immobilier_Architecture` (Real estate, modern architecture)
   - `09_Restauration_Alimentation` (Menus, bakery, cafe promotion)

2. **Strict Non-AI Quality Filtering**:
   - Focuses search queries on authentic human graphic design sources (`indesign template`, `illustrator vector`, `canva print layout`, `behance vector flyer`).
   - Appends negative prompt operators (`-ai`, `-midjourney`, `-diffusion`, `-flux`).
   - Strips non-flyer aspect ratios (removes square 1:1 AI images; preserves portrait ratios ~1.15 to 2.2).
   - Removes duplicates using cryptographic MD5 hashes.

3. **Standardized Organization & Naming**:
   - Flattens all nested folders created by scrapers into clean category root folders.
   - Applies uniform 3-digit sequential naming: `<domain_prefix>_flyer_001.jpg`, `<domain_prefix>_flyer_002.png`, etc.

---

## Usage

### Run via Script
Execute the integrated Python script located in `scripts/download_flyers.py`:

```powershell
# Download across all domains (200-500 flyers)
python "C:\Users\migue\.gemini\config\skills\pinterest-flyer-downloader\scripts\download_flyers.py" --domain all -n 25

# Download a custom search or specific Pinterest board URL
python "C:\Users\migue\.gemini\config\skills\pinterest-flyer-downloader\scripts\download_flyers.py" "music festival flyer template -ai" -n 20 -o "C:\Users\migue\Pictures\flyers pinterest\Festival"
```

### Destination
Default target directory: `C:\Users\migue\Pictures\flyers pinterest\`
