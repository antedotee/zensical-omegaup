#!/usr/bin/env python3
"""
Script to copy all documentation from omegaup repository to zensical-omegaup
"""
import os
import shutil
from pathlib import Path

# Base paths
OMEGAUP_ROOT = Path("/Users/kartikyadav/Desktop/New type orgs/omegaup")
ZENSICAL_ROOT = Path("/Users/kartikyadav/Desktop/New type orgs/zensical-omegaup")

def copy_file(src, dst):
    """Copy a file, creating parent directories if needed"""
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    print(f"Copied: {src} -> {dst}")

def main():
    # Copy main documentation files
    docs_src = OMEGAUP_ROOT / "frontend/www/docs"
    docs_dst = ZENSICAL_ROOT / "docs/main"
    
    if docs_src.exists():
        for md_file in docs_src.glob("*.md"):
            copy_file(md_file, docs_dst / md_file.name)
    
    # Copy root level docs
    root_docs = ["README.md", "CODE_OF_CONDUCT.md"]
    for doc in root_docs:
        src = OMEGAUP_ROOT / doc
        if src.exists():
            copy_file(src, ZENSICAL_ROOT / doc)
    
    # Copy frontend docs
    frontend_docs = [
        ("frontend/README.md", "frontend/README.md"),
        ("frontend/server/README.md", "frontend/server/README.md"),
        ("frontend/tests/README.md", "frontend/tests/README.md"),
        ("frontend/database/ACLs.md", "frontend/database/ACLs.md"),
    ]
    
    for src_rel, dst_rel in frontend_docs:
        src = OMEGAUP_ROOT / src_rel
        if src.exists():
            copy_file(src, ZENSICAL_ROOT / dst_rel)
    
    # Copy privacy policy docs
    privacy_src = OMEGAUP_ROOT / "frontend/privacy"
    privacy_dst = ZENSICAL_ROOT / "privacy"
    
    if privacy_src.exists():
        for privacy_dir in privacy_src.iterdir():
            if privacy_dir.is_dir():
                for lang_file in privacy_dir.glob("*.md"):
                    dst_dir = privacy_dst / privacy_dir.name / lang_file.name
                    copy_file(lang_file, dst_dir)
    
    # Copy GitHub issue templates
    github_src = OMEGAUP_ROOT / ".github/ISSUE_TEMPLATE"
    github_dst = ZENSICAL_ROOT / "github-issue-templates"
    
    if github_src.exists():
        for template_file in github_src.glob("*.md"):
            copy_file(template_file, github_dst / template_file.name)
    
    print("\n✅ Documentation copy completed!")

if __name__ == "__main__":
    main()

