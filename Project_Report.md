# PROJECT WORK

## TITLE OF THE DISSERTATION
# AI COMPANY VERIFICATION SYSTEM

**Bonafide Work Done by**  
`[STUDENT NAME]`  
**REG. NO.** `[YOUR REG NUMBER]`

Dissertation submitted in partial fulfillment of the requirements for the award of  
**B.Sc Data Science**  
of Bharathiar University, Coimbatore-46.

`[College Logo Here]`

**Signature of the Guide** _________________  
**Signature of the HOD** _________________  

Submitted for the Viva-Voce Examination held on _____________

**Internal Examiner** _________________  
**External Examiner** _________________

**Month – Year**  
`[Month, Year]`

---

# CONTENTS
**Acknowledgement**  
**Synopsis**  
1. **Introduction**  
   1.1 Organization Profile  
   1.2 System Specification  
       1.2.1 Hardware Configuration  
       1.2.2 Software Specification  
2. **System Study**  
   2.1 Existing System  
       2.1.1 Drawbacks  
   2.2 Proposed System  
       2.2.1 Features  
3. **System Design and Development**  
   3.1 File Design  
   3.2 Input Design  
   3.3 Output Design  
   3.4 Database Design  
   3.5 System Development  
       3.5.1 Description of Modules  
4. **Testing and Implementation**  
5. **Conclusion, Bibliography, Appendices**  
   A. Data Flow Diagram  
   B. Table Structure  
   C. Sample Coding  
   D. Sample Input  
   E. Sample Output  

---

# ACKNOWLEDGEMENT
I would like to express my sincere gratitude to my guide, `[Guide Name]`, and the Head of the Department for their continuous support and encouragement throughout this project.

# SYNOPSIS
The **AI Company Verification System** is an advanced application engineered natively using Python and Data Science frameworks to combat the rising complexity of fictitious corporate entities. By implementing robust string-similarity algorithms and deeply mapping data structures from local storage, it actively constructs an Originality Percentage for any queried business. Additionally, the system provides visual dashboards breaking down geographic hotspots and fake vs. registered business ratios.

---

# 1. Introduction

## 1.1 Organization Profile
This capstone project is developed as partial fulfillment for the B.Sc Data Science degree. The project leverages statistical analytics and artificial intelligence-driven data matching algorithms to classify unverified company records efficiently.

## 1.2 System Specification

### 1.2.1 Hardware Configuration
- **Processor:** Intel Core i3 / AMD Ryzen equivalent or above
- **RAM:** Minimum 8 GB
- **Storage:** Minimum 256 GB SSD
- **Network Interface:** Active internet connection mandated for retrieving dynamic API avatars and web evidence footprints.

### 1.2.2 Software Specification
- **Operating System:** Windows 10/11, Linux, or macOS Environment
- **Core Programming Language:** Python 3.9+
- **Front-End Framework:** Streamlit (`v1.x`)
- **Data Engineering Engine:** Pandas (`pd`)
- **Visual Analytics:** Plotly Express (`px`)
- **Fuzzy AI Matching algorithm:** RapidFuzz

---

# 2. System Study

## 2.1 Existing System
The existing mechanism for scrutinizing organizations strictly revolves around fragmented manual processes. Individuals must verify the registry portals manually, cross-reference external consumer reviews independently, and compile metadata into isolated Excel sheets for statistical reporting.
### 2.1.1 Drawbacks
- Exhaustive time requirement drastically delaying security protocols.
- Extremely high margin of human error in verifying data sets.
- Lack of centralized analytical intelligence to automatically interpret patterns or duplicates.

## 2.2 Proposed System
The proposed paradigm shift unifies the analysis via a sophisticated Single Page Application logic mechanism running an autonomous validation engine over local datasets. 
### 2.2.1 Features
- **Dynamic Originality Scoring:** Synthesizes multiple data factors seamlessly into a 0% - 100% authenticity confidence score.
- **Fuzz Logic Mapping:** Accurately suggests "Possible Matches" for similarly registered names, defeating basic spoofing tactics.
- **Interactive Analytics:** Generates real-time visual Pi-charts and geographic distribution scales via Plotly.
- **Integrated AI Help Agent:** A fully contained Chatbot directly interacting with users to guide system navigation.

---

# 3. System Design and Development

## 3.1 File Design
The source code relies on Streamlit's multi-page directory routing system allowing for clean isolation of business logic. Secure credentials filter through `app.py`, which invokes subsequent features stored in the `pages/` directory. Sub-routines are effectively decoupled logically into the `utils/` environment.

## 3.2 Input Design
Data intake is thoroughly constrained and formatted properly. E.g., The primary gateway enforces an `@gmail.com` protocol alongside non-empty character validations prior to triggering state progression.

## 3.3 Output Design
Outputs rely profoundly on heavily styled UI Cards integrating dynamic string-parsing, HTML, custom inline-CSS shadows, conditional colors based on validity statuses (Red - Suspicious, Green - Verified), and simulated avatar rendering.

## 3.4 Database Design
The backbone resides in `final_dataset.csv`. Key table fields leveraged:
- `COMPANY_NAME`
- `WEBSITE`
- `LOCATION`
- `RATING` / `REVIEWS`
- `INDUSTRY`
- `FRAUD_LABEL`

## 3.5 System Development
### 3.5.1 Description of Modules (Detailed Explanation)
1. **Authentication Gateway (`app.py`):** Initiates session variables explicitly barring bypasses and renders the Chatbot Welcome Screen.
2. **Dashboard Analytics (`pages/3_dashboard.py`):** Ingests raw data via `pandas` caching protocols and renders complex filtering capabilities allowing macro and micro drill-downs.
3. **Deep Verification Engine (`pages/2_verification.py` & `utils/verify.py`):** Acts as the core computational unit wrapping the `process.extractOne` library functions alongside conditional Originality calculations prioritizing high reviews.
4. **Visual Explorer (`pages/4_categories.py`):** Translates dataset categories seamlessly into clickable HTTP-sourced glassmorphic cards.

---

# 4. Testing and Implementation
The platform was locally executed and tested vigorously for performance, edge cases, and runtime exceptions. Modules passed simulated URL matches and blank queries by correctly reverting to error states. The MPA routing effectively restricts navigation context accurately simulating enterprise session persistence.

---

# 5. Conclusion, Bibliography, Appendices

### Conclusion
The successful deployment of the AI Company Verification System validates the immense potential of Data Science architectures applied towards corporate security. Integrating fuzzy matching and live interactive analytics fundamentally bypasses manual delays resulting in an incredibly efficient verification utility.

### Bibliography
- Streamlit Documentation: https://docs.streamlit.io/
- Pandas Library Reference: https://pandas.pydata.org/docs/
- Plotly Graphing Libraries: https://plotly.com/python/
- RapidFuzz Framework: https://rapidfuzz.github.io/RapidFuzz/

---

### Appendices

#### A. Data Flow Diagram
*(A block-diagram representation outlining the User Login Flow -> Web Interface -> Database Interaction -> AI Analysis Results output is required to be drawn here before binding).*

#### B. Table Structure
| Feature Field | Syntax Type | Example Mapping |
|-------------|-------------|---------------|
| `COMPANY_NAME` | `String` | "Tata Consultancy" |
| `RATING` | `Float` | `4.2` |
| `FRAUD_LABEL` | `Integer` | `1` (Suspicious) |

#### C. Sample Coding
```python
def verify_company(name, df):
    name = name.lower().strip()
    companies = df["COMPANY_NAME"].dropna().tolist()
    matches = process.extract(name, companies, limit=5)
    if matches and matches[0][1] > 80:
        score = matches[0][1]
        best_match = matches[0][0]
        return "POSSIBLE MATCH", score
```

#### D. Sample Input
- **Query Type:** URL Validation
- **Input Text:** *Flipkart.com*

#### E. Sample Output
- **Title:** ✔ Verified Original
- **Originality Score:** 🟩 **87%**
- **Location & Founder Metrics Generated successfully.**
