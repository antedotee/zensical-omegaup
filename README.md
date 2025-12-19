# omegaUp Documentation Site

This is a documentation site for omegaUp built with Zensical.

## Quick Start

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

1. Install dependencies:
```bash
uv sync
```

### Running Locally

To run the documentation site locally with hot-reload:

```bash
uv run zensical serve
```

This will:
- Start a development server at `http://localhost:8000`
- Automatically reload when you make changes to documentation files
- Watch for file changes in the `docs/` directory

### Building for Production

To build the static site:

```bash
uv run zensical build
```

The generated site will be in the `site/` directory.

### Configuration

The site configuration is in `zensical.toml`. You can customize:
- Site name, description, and metadata
- Navigation structure
- Theme settings
- Color schemes
- And more

## Documentation Structure

All documentation files are in the `docs/main/` directory. The navigation structure is defined in `zensical.toml`.

## GitHub Pages Deployment

This site is configured to automatically deploy to GitHub Pages using GitHub Actions.

### Setup Instructions

1. **Enable GitHub Pages** in your repository settings:
   - Go to Settings → Pages
   - Under "Source", select "GitHub Actions"

2. **Push your code** to the `main` or `master` branch:
   ```bash
   git add .
   git commit -m "Initial documentation site"
   git push origin main
   ```

3. **The workflow will automatically**:
   - Build the documentation site
   - Deploy it to GitHub Pages
   - Your site will be available at `https://<username>.github.io/<repository>`

### Manual Deployment

If you want to deploy manually, you can also:

1. Build the site locally:
   ```bash
   uv run zensical build
   ```

2. Push the `site/` directory to the `gh-pages` branch (if using that method)

The GitHub Actions workflow (`.github/workflows/docs.yml`) handles automatic deployment on every push to the main branch.

