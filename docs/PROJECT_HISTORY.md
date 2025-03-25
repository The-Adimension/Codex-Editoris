# Codex Editoris Vitae: Project Evolution History

This document chronicles the development history of Codex Editoris Vitae, which emerged as a specialized offshoot of the main Codex Editoris project, focusing on author-centered exploration of academic publications.

## The Birth of Author-Focused Exploration

While Codex Editoris was initially developed for journal-based article discovery, it became clear during development that there was a parallel need for author-focused exploration. This realization led to the creation of Codex Editoris Vitae as a dedicated application for researcher profiles and publication collections.

## Timeline Overview

1. **Shared Origins with Codex Editoris** (January 2024)
2. **First Author-Focused Experiments** (January 2024)
3. **Dedicated Author Interface Development** (February 2024)
4. **Research and Refinement** (March 2024)
5. **Final Implementation** (March 2024)

## Phase 1: Shared Origins (January 2024)

Codex Editoris Vitae shares its foundations with the original Codex Editoris project:
- Python-based data collection from EuroPMC API
- Core processing of academic article metadata
- Social media post generation functionality

The key Python files from this period that influenced both projects:
- `CodexEditorisEHJIMP.py` - Contained early author data processing
- `Codex_Editoris_API-ATOM.py` - API interaction that retrieved author information
- `Codex_Editoris_Platform.py` - GUI platform with author data display capabilities

## Phase 2: First Author-Focused Experiments (January 2024)

The first dedicated author-focused implementation appeared as a variant of the main project:
- `Codex-Editoris SE Petersen.html` - HTML output focused on a specific author's publications

This early version demonstrated the potential value of organizing content around authors rather than journals, but still used the static HTML generation approach of the original project.

## Phase 3: Dedicated Author Interface Development (February 2024)

February 2024 saw the emergence of a dedicated author-centered interface:
- `CE-Vitae.html` - First comprehensive author-focused prototype

This prototype included:
- Author profile card design
- Publication listing by author
- Social media links for author profiles
- Visual design tailored to researcher portfolios

## Phase 4: Research and Refinement (March 2024)

The Jupyter notebook stage included specific research for the author-focused application:
- `In_recognition_of_the_digital_YOU!_CG_edition.ipynb` - Deep exploration of author metadata and presentation options

This research phase explored:
- Author identification systems (ORCID, Scopus Author ID, etc.)
- Academic network integration possibilities
- Citation metrics for authors
- Optimization of author search functionality

## Phase 5: Final Implementation (March 2024)

The culmination of this specialized development track is the current HTML/JS application:
- `The Adimension _ Codex Editoris Vitae.html` - Production author-focused version

The final implementation features:
- Author search functionality
- Complete publication listings by author
- Academic profile visualization
- Co-author network exploration
- Social media integration for researcher profiles
- Journal filtering within author collections

## Unique Aspects of Codex Editoris Vitae

While sharing core technology with Codex Editoris, this project has several unique characteristics:

1. **Author-Centric Data Model**: Reorganizes the data model around researchers rather than publications

2. **Academic Identity Focus**: Emphasizes the researcher's identity and body of work

3. **Career Trajectory Visualization**: Shows publication patterns over time for individual researchers

4. **Collaboration Network**: Highlights co-author relationships and institutional connections

5. **Portfolio Generation**: Enables creation of shareable academic portfolios

## Why a Separate Repository?

The decision to maintain Codex Editoris Vitae as a separate repository from the main Codex Editoris project was made for several reasons:

1. **Distinct Use Case**: While sharing technical foundations, the author-focused and journal-focused applications serve different primary audiences and use cases

2. **Specialized Features**: The author-focused version requires features not needed in the journal-focused version

3. **Independent Deployment**: Allows for separate deployment cycles and versioning

4. **Focused Development**: Enables contributors to focus on either author-centric or journal-centric enhancements

5. **Clearer User Journeys**: Provides distinct entry points for users with different research goals

## Shared Code and Collaboration

Despite being separate repositories, Codex Editoris and Codex Editoris Vitae maintain close collaboration:

- Core data processing utilities are shared when appropriate
- UI design language remains consistent across both applications
- Bug fixes that affect both codebases are coordinated
- Feature enhancements that benefit both are implemented in parallel

## Future Directions

The future development of Codex Editoris Vitae will focus on enhancing researcher profiles:

- Academic social graph visualization
- Citation metrics and impact analysis
- Institutional affiliation tracking
- Research topic classification
- Integration with academic identity systems (ORCID, Google Scholar, etc.)
- CV/resume generation functionality

## Repository History

For those interested in examining the developmental progression, the historical prototypes and research materials are preserved in the `historical/` directory of this repository. 