# Codex Editoris EHJIMP: DEITY Principles Stack

This document organizes the technology stack according to The Adimension's DEITY Framework principles, serving as both a documentation standard and implementation guide for human-machine interoperability in scientific publishing. Each section includes both the conceptual framework and concrete implementation evidence from the codebase.

## DATA - Bridging Human-Machine Collaboration

### Concept
Central to bridging human and machine collaboration, enabling the generation, segmentation, and transformation of actionable datasets through modular data preparation, sharing, and continuous updates.

### Implementation Evidence

#### Data Retrieval & Transformation
- **Europe PMC API Integration**: 
  ```javascript
  const apiUrl = `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=JOURNAL%3A"Eur%20Heart%20J%20Imaging%20Methods%20Pract"&resultType=core&pageSize=${userPageSize}&sort=P_PDATE_D%20desc&format=json`;
  ```

- **Citation Network Mapping**:
  ```javascript
  async function fetchCitations(pmid) {
    try {
      const response = await fetch(`https://www.ebi.ac.uk/europepmc/webservices/rest/MED/${pmid}/citations/1/5/json`);
      const data = await response.json();
      return data;
    } catch (error) {
      console.error(`Error fetching citations for PMID ${pmid}:`, error);
      return { citationList: { citation: [], totalCitations: 0 } };
    }
  }
  ```

- **Metrics Aggregation**:
  ```javascript
  function getSelectedFields() {
    const checkboxes = document.querySelectorAll('#field-selection-form input[name="fields"]');
    const selected = [];
    checkboxes.forEach(cb => {
      if (cb.type === 'hidden' || cb.checked) {
        selected.push(cb.value);
      }
    });
    return selected;
  }
  ```

#### Data Transfer & Sharing
- **Clipboard Integration**:
  ```javascript
  function copyToClipboard(text) {
    if (navigator.clipboard) {
      navigator.clipboard.writeText(text)
        .then(() => {
          showToast('Copied to clipboard!');
        })
        .catch(() => {
          showToast('Failed to copy to clipboard. Please try again.');
        });
    }
  }
  ```

- **CSV Export Functionality**:
  ```javascript
  function exportArticlesToCSV() {
    // Get the currently filtered articles
    const articles = getCurrentFilteredArticles();
    
    if (articles.length === 0) {
      showToast('No articles to export', 'warning');
      return;
    }
    
    // Define CSV headers
    const headers = ['Title', 'Authors', 'Journal', 'Year', 'PMID', 'DOI', 'Abstract'];
    
    // Create CSV content
    let csvContent = headers.join(',') + '\n';
    
    articles.forEach(article => {
      // Process each field, properly escaping quotes and commas
      const row = [
        `"${(article.title || '').replace(/"/g, '""')}"`,
        `"${(article.authorString || '').replace(/"/g, '""')}"`,
        `"${(article.journalTitle || '').replace(/"/g, '""')}"`,
        article.pubYear || '',
        article.pmid || '',
        article.doi || '',
        `"${(article.abstractText || '').replace(/"/g, '""')}"`
      ];
      csvContent += row.join(',') + '\n';
    });
    
    // Create a download link and trigger the download
    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.setAttribute('href', url);
    link.setAttribute('download', `EHJIMP-Articles-${new Date().toISOString().slice(0,10)}.csv`);
    link.style.display = 'none';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }
  ```

#### Dynamic Data Updates
- **Configurable Refresh**:
  ```javascript
  // PageSize is dynamically set via user input in the display options bar
  const userPageSize = document.getElementById('articles-count').value || 10;
  ```

- **External Service Integration**:
  ```javascript
  async function loadBadgeScripts(selectedFields) {
    try {
      const promises = [];
      
      if (selectedFields.includes("dimensions")) {
        promises.push(loadScript("https://badge.dimensions.ai/badge.js"));
      }
      if (selectedFields.includes("altmetric")) {
        window._altmetric_embed_init_called = false;
        promises.push(loadScript("https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js"));
      }
      // Additional badge loading logic...
      
      await Promise.all(promises);
      console.log("All badge scripts loaded successfully");
    } catch (err) {
      console.error("Error loading badge scripts:", err);
    }
  }
  ```

## ETHICS - Integrity & Trustworthiness

### Concept
Ensures the integrity and trustworthiness of the system by prioritizing transparency, user control, and appropriate attribution through preference management, source citation, and explanatory elements.

### Implementation Evidence

#### User Control & Transparency
- **User-controlled Preferences**:
  ```javascript
  // User can control which metrics to display
  const fieldSelectionForm = document.getElementById('field-selection-form');
  fieldSelectionForm.addEventListener('change', function(e) {
    if (e.target.type === 'checkbox') {
      generateHTML();
    }
  });
  ```

- **Clear Data Source Attribution**:
  ```html
  <div class="citation-container">
    <small class="text-muted">Data from Europe PMC</small>
    <a href="https://europepmc.org/article/MED/${article.pmid}" target="_blank" rel="noopener">
      View on Europe PMC <i class="fas fa-external-link-alt fa-xs"></i>
    </a>
  </div>
  ```

#### Privacy Considerations
- **Preference Storage Management**:
  ```javascript
  function saveCurrentSettings() {
    try {
      // Only save preferences that don't contain personal data
      const settings = {
        selectedFields: getSelectedFields(),
        articlesCount: document.getElementById('articles-count').value
      };
      
      localStorage.setItem('codexEditorisSettings', JSON.stringify(settings));
      console.log('Settings saved to localStorage');
    } catch (e) {
      console.warn('Failed to save settings to localStorage:', e);
    }
  }
  ```

- **Proper Attribution**:
  ```html
  <footer>
    <div class="container">
      <div class="row align-items-center g-0">
        <div class="col-8 text-md-start text-start">
          <p class="m-0">The Adimension | Codex Editoris #EHJIMP. <br><strong>To AïA</strong> | S. Anwer © The Adimension 2025.</p>
        </div>
        <!-- Logo and attribution -->
      </div>
    </div>
  </footer>
  ```

#### Educational Elements
- **Metrics Explanation**:
  ```javascript
  function showMetricsExplanation() {
    const explanationHTML = `
      <div class="metrics-explanation p-3">
        <h5>About the Metrics</h5>
        <ul class="list-unstyled">
          <li><strong>Altmetric:</strong> Measures online attention including social media, news, and policy documents.</li>
          <li><strong>PlumX:</strong> Tracks usage, captures, mentions, social media, and citations.</li>
          <li><strong>Scite:</strong> Shows supporting, contradicting, and mentioning citations.</li>
          <li><strong>Dimensions:</strong> Provides citation counts and access metrics.</li>
        </ul>
      </div>
    `;
    
    // Display the explanation in a modal or toast
    const explanationToast = new bootstrap.Toast(document.getElementById('metrics-explanation-toast'));
    document.getElementById('metrics-explanation-toast-body').innerHTML = explanationHTML;
    explanationToast.show();
  }
  ```

## INFORMATICS - Data into Knowledge

### Concept
Converts raw data into actionable insights through visualization, analysis tools, and interactive displays that enable researchers to gain meaningful understanding from publication data.

### Implementation Evidence

#### Publication Metrics Visualization
- **Citation Context Display**:
  ```html
  <div class="scite-badge" data-doi="${article.doi}" data-tooltip-placement="right"></div>
  ```

- **Multi-dimensional Metrics**:
  ```javascript
  function renderMetricsBadges(article, container, selectedFields) {
    if (!article || !container) return;
    
    const badgesContainer = document.createElement('div');
    badgesContainer.className = 'badges-container d-flex flex-wrap gap-2 mt-2';
    
    // Dimensions badge
    if (selectedFields.includes('dimensions') && article.doi) {
      const dimensionsContainer = document.createElement('div');
      dimensionsContainer.className = '__dimensions_badge_embed__';
      dimensionsContainer.dataset.doi = article.doi;
      dimensionsContainer.dataset.style = 'small_circle';
      badgesContainer.appendChild(dimensionsContainer);
    }
    
    // Altmetric badge
    if (selectedFields.includes('altmetric') && article.doi) {
      const altmetricContainer = document.createElement('div');
      altmetricContainer.className = 'altmetric-embed';
      altmetricContainer.dataset.badgeType = 'donut';
      altmetricContainer.dataset.badgePopover = 'right';
      altmetricContainer.dataset.doi = article.doi;
      badgesContainer.appendChild(altmetricContainer);
    }
    
    // Additional badges...
    
    container.appendChild(badgesContainer);
  }
  ```

#### Cross-Platform Adaptability
- **Responsive Design**:
  ```css
  @media (max-width: 767px) {
    .app-header h1 {
      font-size: 1.3rem;
    }
    .app-header .lead {
      font-size: 0.8rem;
      display: block !important;
    }
  }
  
  @media (max-width: 576px) {
    .app-header h1 {
      font-size: 1.1rem;
    }
    .app-header .lead {
      font-size: 0.75rem;
    }
  }
  ```

#### Service Reliability & Fallbacks
- **Dependency Handling with Fallbacks**:
  ```javascript
  // Function to load the Scite script with rate limit handling
  function loadSciteScript(retryDelay = 2000) {
    return new Promise((resolve, reject) => {
      // Don't retry if we've hit max retries
      if (window._sciteRetryCount >= window._sciteMaxRetries) {
        console.warn(`Reached maximum Scite API retries (${window._sciteMaxRetries}). Will not attempt further requests.`);
        const badges = document.querySelectorAll('.scite-badge');
        badges.forEach(badge => {
          const doi = badge.getAttribute('data-doi');
          badge.innerHTML = `<p class="text-danger"><i class="fas fa-exclamation-circle"></i> Rate limited by Scite API.</p>
          <a href="https://scite.ai/reports/${doi}" target="_blank" rel="noopener" class="btn btn-sm btn-outline-primary mt-2">View on Scite.ai instead</a>`;
        });
        return resolve();
      }
      
      // Load script with exponential backoff...
    });
  }
  ```

## TECHNOLOGY - Infrastructure & Integration

### Concept
Powers the application through adaptive, efficient systems that optimize performance and resource usage while enabling seamless integration of multiple data sources and services.

### Implementation Evidence

#### Structured Data Management
- **Publication Data Modeling**:
  ```javascript
  // Structured article data representation
  const articleData = {
    title: article.title,
    authors: article.authorString,
    journal: article.journalTitle,
    year: article.pubYear,
    pmid: article.pmid,
    doi: article.doi,
    abstract: article.abstractText,
    publicationDate: article.firstPublicationDate,
    metrics: {
      citations: article.citationCount,
      // Other metrics aggregated from various sources
    }
  };
  ```

#### Asynchronous Processing
- **Non-blocking Data Retrieval**:
  ```javascript
  async function fetchArticles(selectedFields, page = 1) {
    const userPageSize = document.getElementById('articles-count').value || 10;
    const apiUrl = `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=JOURNAL%3A"Eur%20Heart%20J%20Imaging%20Methods%20Pract"&resultType=core&pageSize=${userPageSize}&sort=P_PDATE_D%20desc&format=json`;
    
    try {
      console.log(`Fetching ${userPageSize} articles...`);
      
      // Pre-load badge scripts before rendering articles 
      await loadBadgeScripts(selectedFields);
      
      const response = await fetch(apiUrl);
      if (!response.ok) {
        throw new Error(`API error: ${response.status} ${response.statusText}`);
      }
      
      const data = await response.json();
      // Process and render articles...
    } catch (error) {
      console.error('Error fetching articles:', error);
      // Handle errors...
    }
  }
  ```

#### Resource Optimization
- **Conditional Script Loading**:
  ```javascript
  function loadScript(src) {
    return new Promise((resolve, reject) => {
      // Check if the script is already loaded
      const existingScript = document.querySelector(`script[src="${src}"]`);
      if (existingScript) {
        return resolve();
      }
      
      const script = document.createElement('script');
      script.async = true;
      script.src = src;
      script.charset = "utf-8";
      script.onload = () => resolve();
      script.onerror = (e) => reject(e);
      document.head.appendChild(script);
    });
  }
  ```

#### Progressive Enhancement
- **Layered Functionality**:
  ```javascript
  // Core functionality works without JavaScript, but is enhanced with it
  document.addEventListener('DOMContentLoaded', function() {
    // Load saved settings
    loadSavedSettings();
    
    // Set up event listeners
    setupEventListeners();
    
    // Generate initial HTML based on default or saved settings
    generateHTML();
  });
  ```

## YOU - The Human & The Machine Partnership

### Concept
Places both human users and computational systems at the core of the design, ensuring researcher needs drive the interface while automation handles complex data retrieval and processing.

### Implementation Evidence

#### Researcher-focused Interface
- **Research-oriented Controls**:
  ```html
  <!-- Filter bar designed for researcher workflows -->
  <div id="sticky-filter-bar" class="filter-bar d-none">
    <div class="container">
      <div class="row g-2 py-2">
        <div class="col-12 mb-1 d-flex justify-content-between align-items-center">
          <h6 class="mb-0 text-muted"><i class="fas fa-filter me-1"></i>Filter Articles</h6>
          <div class="text-end">
            <button type="button" class="btn btn-sm btn-success me-2" onclick="exportArticlesToCSV()" title="Export filtered articles to CSV">
              <i class="fas fa-file-export me-1"></i><span class="d-none d-sm-inline">Export CSV</span>
            </button>
            <button type="button" class="btn btn-sm btn-outline-secondary me-1" onclick="resetFilters()" title="Reset filters">
              <i class="fas fa-undo me-1"></i><span class="d-none d-sm-inline">Reset</span>
            </button>
            <button type="button" class="btn btn-sm btn-primary" onclick="applyFilters()">
              <i class="fas fa-check me-1"></i><span class="d-none d-sm-inline">Apply</span>
            </button>
          </div>
        </div>
        <!-- Filter inputs optimized for research workflows -->
      </div>
    </div>
  </div>
  ```

#### Academic Workflow Support
- **Citation Generation**:
  ```javascript
  // Citation tools for researchers
  function generateCitation(article, format = 'apa') {
    if (!article) return '';
    
    let citation = '';
    const authors = article.authorString || 'No authors listed';
    const title = article.title || 'No title';
    const journal = article.journalTitle || 'Unknown journal';
    const year = article.pubYear || 'n.d.';
    const volume = article.journalVolume || '';
    const issue = article.issue || '';
    const pages = article.pageInfo || '';
    const doi = article.doi || '';
    
    switch(format.toLowerCase()) {
      case 'apa':
        citation = `${authors}. (${year}). ${title}. ${journal}`;
        if (volume) citation += `, ${volume}`;
        if (issue) citation += `(${issue})`;
        if (pages) citation += `, ${pages}`;
        if (doi) citation += `. https://doi.org/${doi}`;
        break;
      // Other citation formats...
    }
    
    return citation;
  }
  ```

#### Interactive Feedback
- **User Notifications**:
  ```javascript
  function showToast(message, type = 'success') {
    const toastContainer = document.getElementById('toast-container');
    if (!toastContainer) return;
    
    const toast = document.createElement('div');
    toast.className = `toast align-items-center text-white bg-${type} border-0`;
    toast.setAttribute('role', 'alert');
    toast.setAttribute('aria-live', 'assertive');
    toast.setAttribute('aria-atomic', 'true');
    
    toast.innerHTML = `
      <div class="d-flex">
        <div class="toast-body">
          ${message}
        </div>
        <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
      </div>
    `;
    
    toastContainer.appendChild(toast);
    const bsToast = new bootstrap.Toast(toast, { autohide: true, delay: 3000 });
    bsToast.show();
    
    // Remove toast from DOM after it's hidden
    toast.addEventListener('hidden.bs.toast', function() {
      toastContainer.removeChild(toast);
    });
  }
  ```

> **Note:** For detailed implementation checklists, please refer to the separate [DEITY_CHECKLIST.md](DEITY_CHECKLIST.md) document. 