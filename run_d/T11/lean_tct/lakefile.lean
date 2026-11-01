import Lake
open Lake DSL
package tct_T11 where
  moreServerArgs := #["-DwarningAsError=false"]
@[default_target]
lean_lib TCT where
  globs := #[.one `TCT.Basic]
