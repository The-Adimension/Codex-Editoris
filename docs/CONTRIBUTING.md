# Contributing to Codex Editoris Vitae

Thank you for your interest in contributing to Codex Editoris Vitae! This document provides guidelines and instructions for contributing to this author-focused project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Process](#development-process)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Coordination with Codex Editoris](#coordination-with-codex-editoris)

## Code of Conduct

We are committed to providing a welcoming and inclusive environment for all contributors. Please be respectful and constructive in all interactions.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/codex-editoris-vitae.git
   cd codex-editoris-vitae
   ```
3. Open `src/index.html` in your browser to verify the application works

## How to Contribute

There are many ways to contribute:

1. **Report Bugs**: Open an issue if you find a bug
2. **Suggest Enhancements**: Submit feature requests as issues
3. **Improve Documentation**: Documentation improvements are always welcome
4. **Submit Code Changes**: Fix bugs or implement new features
5. **Author Profile Enhancements**: Improve how author information is displayed

## Development Process

Since this is an HTML/JS application with no build steps, development is straightforward:

1. Make your changes in the `src/` directory
2. Test by opening `src/index.html` in a browser
3. Make sure your changes are responsive and work on different screen sizes
4. Test with different author search scenarios

## Pull Request Process

1. Ensure any install or build dependencies are removed before the PR
2. Update the README.md with details of changes if appropriate
3. The PR should work in all major browsers (Chrome, Firefox, Safari, Edge)
4. Your PR will be reviewed by at least one maintainer, who may request changes

## Coding Standards

We use the following standards:

### HTML
- Use semantic HTML5 elements
- Keep indentation consistent (2 spaces)
- Include appropriate accessibility attributes

### CSS
- Prefer CSS custom properties for colors and repeated values
- Use meaningful class names that describe purpose, not appearance
- Maintain responsive design principles

### JavaScript
- Follow ES6+ syntax and practices
- Use descriptive variable and function names
- Document complex functions with comments
- Avoid jQuery or other dependencies

## Commit Guidelines

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

Types include:
- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that do not affect the meaning of the code
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **perf**: A code change that improves performance
- **test**: Adding or correcting tests
- **chore**: Changes to the build process or auxiliary tools

For example:
```
feat(profiles): add author ORCID integration

This allows linking author profiles to their ORCID identifiers
for improved scholarly identity management.
```

## Coordination with Codex Editoris

Codex Editoris Vitae is a companion project to [Codex Editoris](https://github.com/the-adimension/codex-editoris). When making changes, consider:

1. **Shared Functionality**: Consider if your changes should also be implemented in the main Codex Editoris repository
2. **Consistent UX**: Maintain consistent design language between both projects
3. **Cross-Project Issues**: Tag issues that affect both repositories with the appropriate labels
4. **Code Reuse**: Identify opportunities for shared components or utilities

## DEITY Framework Considerations

When contributing, consider how your changes align with The Adimension's DEITY framework:

- **DATA**: Are we handling author data responsibly and accurately?
- **ETHICS**: Does this support ethical attribution and representation?
- **INFORMATICS**: Does it improve organization of author information?
- **TECHNOLOGY**: Is the implementation accessible and efficient?
- **YOU**: How does this improve the researcher experience?

Thank you for contributing to Codex Editoris Vitae! 