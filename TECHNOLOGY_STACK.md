# Codex Editoris EHJIMP: Technology Stack & Unique Qualities

## Comprehensive Technology Stack & Resources

### Programming Languages
- HTML5
- CSS3
- JavaScript (ES6+)

### Frontend Framework
- Bootstrap 5 (UI components, responsive layout)
- Font Awesome (icon library)

### Scientific Metrics Services
- Altmetric (social media engagement & news coverage)
- PlumX (usage statistics, captures, and citations)
- Scite.ai (supporting, contradicting, mentioning citations)
- Dimensions.ai (citation counts and access metrics)

### External APIs
- Europe PMC API (publication data retrieval)
- Europe PMC Citation API (citation data)
- Altmetric API (via embed script)
- PlumX API (via widget script)
- Scite.ai API (via badge script)
- Dimensions API (via badge script)

### Browser APIs
- DOM API (document manipulation)
- Fetch API (asynchronous data retrieval)
- Web Storage API (localStorage for preferences)
- Clipboard API (citation copying)
- Web Share API (mobile sharing)

### UI Components
- Toast notifications
- Responsive article cards
- Filter bar with date & keyword search
- Field selection switches
- Loading indicators

### Data Processing
- JSON parsing and manipulation
- CSV generation for export
- Date filtering
- Keyword searching
- Citation formatting

### Performance Techniques
- Asynchronous loading (async/await)
- Rate limiting and retry logic for Scite API
- Conditional script loading
- Error handling with fallbacks

### External Scripts
- https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js
- https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css
- https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js (Altmetric)
- https://cdn.plu.mx/widget-summary.js (PlumX)
- https://cdn.scite.ai/badge/scite-badge-latest.min.js (Scite)
- https://badge.dimensions.ai/badge.js (Dimensions)

## Unique Qualities of Codex Editoris EHJIMP

### Scientific Publishing Focus
- Specialized in academic publication visualization from a single journal (EHJIMP)
- Complete integration of four major scientific impact metrics in one interface
- Citation context awareness through Scite integration

### Technical Implementation
- Framework-free architecture (vanilla JavaScript)
- Sophisticated error handling for third-party services
- Exponential backoff for rate-limited APIs
- Persistent user preferences for display options

### User Experience
- Streamlined research workflow for academic users
- Mobile-responsive design for on-the-go literature review
- Comprehensive filtering by date ranges and keywords
- One-click data export to CSV for further analysis

### Visual Design
- Clean, academic-focused UI with minimal distractions
- Consistent branding with The Adimension visual language
- Accessibility considerations with proper contrast and labeling

## Distinctive Differences from Codex Editoris Vitae

### Focus Differences
- EHJIMP is publication-centric (focusing on academic articles)
- Emphasizes citation metrics and alternative metrics
- Designed for literature review and discovery

### Technical Differences
- Implements more external badges and metrics services
- More complex API integration with multiple scientific services
- More sophisticated retry and rate-limiting logic

### Functional Differences
- Real-time data sourcing from Europe PMC
- Citation export functionality
- Social sharing capabilities
- More advanced filtering options 