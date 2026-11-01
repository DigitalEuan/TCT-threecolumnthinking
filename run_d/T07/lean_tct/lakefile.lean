import Lake
open Lake DSL
package tct_T07 where
  moreServerArgs := #["-DwarningAsError=false"]
@[default_target]
lean_lib TCT where
  globs := #[.one `TCT.Basic]
