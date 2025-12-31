# GitHub Pages Deployment Guide

## Quick Setup

### 1. Enable GitHub Pages

**Before pushing your code**, you must enable GitHub Pages:

1. Go to your repository on GitHub
2. Click **Settings** → **Pages** (in the left sidebar under "Code and automation")
3. Under "Build and deployment" → "Source", select **GitHub Actions**
4. Save the settings

⚠️ **Important:** If you don't do this first, the workflow will fail with an error about Pages not being enabled.

### 2. Push Your Code

```bash
git add .
git commit -m "Add documentation site"
git push origin main
```

### 3. Check Deployment

1. Go to the **Actions** tab in your repository
2. Wait for the "Documentation" workflow to complete
3. Once successful, your site will be live!

## Your Site URL

Your documentation site will be available at:

```
https://<your-username>.github.io/<repository-name>/
```

**Example:**
- Username: `kartikyadav`
- Repository: `zensical-omegaup`
- URL: `https://kartikyadav.github.io/zensical-omegaup/`

### How to Find Your URL

After the first successful deployment:

1. Go to **Settings** → **Pages**
2. You'll see: "Your site is live at `https://...`"
3. Or check the workflow run summary - it shows the deployment URL

## Troubleshooting

### Error: "Get Pages site failed"

**Cause:** GitHub Pages is not enabled

**Solution:**
1. Go to Settings → Pages
2. Select "GitHub Actions" as the source
3. Save
4. Re-run the workflow (or push a new commit)

### Workflow Fails

Check the Actions tab for detailed error messages. Common issues:

- **Build errors:** Check the "Build documentation" step logs
- **Permission errors:** Ensure Pages is enabled and you have admin access
- **Dependency errors:** Verify `pyproject.toml` is correct

### Site Not Updating

- Wait a few minutes after deployment
- Clear your browser cache
- Check the Actions tab to ensure the workflow completed successfully

## Custom Domain (Optional)

If you want to use a custom domain:

1. Add a `CNAME` file in your `docs/` directory with your domain
2. Configure DNS settings for your domain
3. Update `site_url` in `zensical.toml` to match your domain

For more details, see: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site



