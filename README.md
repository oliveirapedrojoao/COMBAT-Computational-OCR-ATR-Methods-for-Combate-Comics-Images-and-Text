# COMBAT — Computational Machine Reading of Combate: Comics, Images and Text through OCR/ATR

## 📄 Overview

**Combate** is a historical newspaper characterized by its unique blend of comic-style illustrations and handwritten news articles. Comprising **51 issues**, each averaging **8 to 9 pages**, the collection totals **487 pages** in `.pdf` format. Although digitally available through the **National Library of Portugal**, the quality of digitization is notably subpar, posing significant challenges for computational processing and analysis.

---

## 📚 Dataset Description

- **Total Issues**: 51  
- **Average Pages per Issue**: 8–9  
- **Total Page Count**: 487 
- **Format**: PDF (easily convertible to other document formats)  
- **File Sizes**: 2,621 KB to 4,858 KB  
- **Access**:  
  - **Digital**: [National Library of Portugal](https://www.bnportugal.gov.pt)  
  - **Physical**: Available at the National Library of Portugal

---

## ⚠️ Quality of Digitization

The digitized versions of *Combate* suffer from various issues:

- Lack of clarity, refinement, and cleanliness
- Inconsistent quality across issues
- Smudged illustrations with darkened areas and blurred borders
- Poor legibility of both text and handwritten content
- Comics and captions often lose definition, complicating interpretation

These factors significantly degrade the readability of the content and hinder digital analysis.

---

## 🗞️ Layout Characteristics

*Combate* diverges from traditional journalistic formats:

- No adherence to professional editorial guidelines
- Layout is chaotic and highly irregular
- Articles and comic-style drawings are interspersed throughout pages
- Prioritizes message over structure, aligning with its motto:  
  > “A newspaper for the people, by the people, for the working people”

This lack of design consistency impedes automated processing and layout detection.

---

## 🧠 OCR & Machine Learning Challenges

Applying Optical Character Recognition (OCR) to *Combate* is particularly complex due to:

- Unstructured and inconsistent layouts
- Presence of handwriting and visual elements
- Low-quality scans and visual noise

### Recommendations:
- Use of **custom-trained OCR/HTR models**
- Preprocessing steps such as:
  - Noise reduction
  - Contrast enhancement
  - Region segmentation

Without these adaptations, OCR tools will exhibit a high error rate.

---

## 🔍 Research Potential

Despite the technical limitations, *Combate* remains a valuable resource for:

- Historical and political analysis of grassroots media
- Training datasets for OCR under adverse conditions
- Studies in digital preservation and archival practices
- Exploration of alternative visual and textual communication models

---

## 🏛️ Acknowledgments

Access to the *Combate* collection is provided by the **Biblioteca Nacional de Portugal** (National Library of Portugal). Researchers are encouraged to consult the physical archive for verification due to the poor quality of digital scans.

---
