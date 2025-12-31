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

### Step-by-Step Setup Instructions

**IMPORTANT:** You must enable GitHub Pages **before** pushing your code, otherwise the workflow will fail.

1. **Enable GitHub Pages** in your repository settings:
   - Go to your repository on GitHub
   - Click on **Settings** (in the repository navigation bar)
   - In the left sidebar, under "Code and automation", click **Pages**
   - Under "Build and deployment", find the **Source** section
   - Select **GitHub Actions** (NOT "Deploy from a branch")
   - Click **Save** (if there's a save button)

   ⚠️ **Note:** If you see an error about Pages not being enabled, make sure:
   - Your repository is public (or you have GitHub Pro/Team)
   - You have admin/maintainer permissions
   - You've verified your email address

2. **Push your code** to the `main` or `master` branch:
   ```bash
   git add .
   git commit -m "Initial documentation site"
   git push origin main
   ```

3. **Monitor the deployment**:
   - Go to the **Actions** tab in your repository
   - You should see a workflow run called "Documentation"
   - Wait for it to complete (usually takes 1-2 minutes)

4. **Access your site**:
   - Once the workflow completes successfully, your site will be available at:
     - `https://<username>.github.io/<repository-name>/`
   - For example: `https://kartikyadav.github.io/zensical-omegaup/`
   - The URL will also be shown in the workflow run summary

### Finding Your Site URL

After the first successful deployment:

1. Go to your repository **Settings** → **Pages**
2. You'll see: "Your site is live at `https://<username>.github.io/<repository>/`"
3. Or check the workflow run - it will show the deployment URL in the job summary

### Troubleshooting

**Error: "Get Pages site failed"**
- This means GitHub Pages isn't enabled yet
- Follow Step 1 above to enable it
- Make sure you select **GitHub Actions** as the source, not a branch

**Workflow fails**
- Check the Actions tab for error details
- Common issues:
  - Missing dependencies (check `pyproject.toml`)
  - Build errors (check the build step logs)
  - Permission issues (ensure Pages is enabled)

### Manual Deployment

If you want to deploy manually, you can also:

1. Build the site locally:
   ```bash
   uv run zensical build
   ```

2. The GitHub Actions workflow (`.github/workflows/docs.yml`) handles automatic deployment on every push to the main branch.

