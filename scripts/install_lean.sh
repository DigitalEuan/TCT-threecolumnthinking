#!/bin/bash
# Install elan + Lean 4 stable toolchain into the project (re-created after recycle).
set -x
DIST=/home/z/my-project/tct_work/lean_dist
mkdir -p "$DIST/elan" "$DIST/dl"
cd "$DIST/dl"
curl -sL -o elan.tar.gz https://github.com/leanprover/elan/releases/latest/download/elan-x86_64-unknown-linux-gnu.tar.gz || { echo "ELAN_DOWNLOAD_FAILED"; exit 1; }
tar -xzf elan.tar.gz || { echo "ELAN_EXTRACT_FAILED"; exit 1; }
export ELAN_HOME="$DIST/elan"
./elan-init -y --no-modify-path --default-toolchain leanprover/lean4:stable > /home/z/my-project/tct_work/lean_install.log 2>&1
echo "init_exit=$?"
PATH="$DIST/elan/bin:$PATH" lean --version
PATH="$DIST/elan/bin:$PATH" lake --version
echo "LEAN_INSTALL_DONE"
