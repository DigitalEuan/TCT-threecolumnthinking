#!/bin/bash
# Assemble the packaged repository and zip it.
set -e
R=/home/z/my-project/download/tct-skill-study
rm -rf "$R" /home/z/my-project/download/tct-skill-study.zip
mkdir -p "$R"/{paper,case_studies,run_d,skill,scripts}

# paper + case-study documents
cp /home/z/my-project/download/tct_paper.md /home/z/my-project/download/tct_paper.pdf "$R/paper/"
cp /home/z/my-project/download/tct_case_studies.md /home/z/my-project/download/tct_case_studies.pdf "$R/case_studies/"

# the quartet as shipped (clean of build residue) + audit logs + repaired copies
mkdir -p "$R/case_studies/quartet" "$R/case_studies/audit" "$R/case_studies/repaired"
for s in /home/z/my-project/case_studies/*/; do
  n=$(basename "$s"); cp -r "$s$n" "$R/case_studies/quartet/"
done
find "$R/case_studies/quartet" -name ".lake" -type d -exec rm -rf {} + 2>/dev/null || true
cp -r /home/z/my-project/tct_quartet_audit/* "$R/case_studies/audit/"
for d in /home/z/my-project/tct_work/repaired/*/; do
  n=$(basename "$d"); cp -r "$d" "$R/case_studies/repaired/$n"
  rm -rf "$R/case_studies/repaired/$n/.lake"
done

# the regenerated Run D bundle (strip build artifacts; sources + logs stay)
cp -r /home/z/my-project/tct_run_d/* "$R/run_d/"
find "$R/run_d" -name ".lake" -type d -exec rm -rf {} + 2>/dev/null || true
find "$R/run_d" -name "lakefile.lean.orig" -delete 2>/dev/null || true

# the evaluated skill + all driver scripts
cp /home/z/my-project/upload/SKILL.md "$R/skill/SKILL.md"
cp /home/z/my-project/scripts/*.py /home/z/my-project/scripts/*.sh /home/z/my-project/scripts/*.css "$R/scripts/" 2>/dev/null || true

echo "assembled:"; find "$R" -maxdepth 2 -type d | sort | sed 's|/home/z/my-project/download/||'
