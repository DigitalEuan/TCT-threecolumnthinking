import Lake
open Lake DSL
package tct_maudlin where
  moreServerArgs := #["-DwarningAsError=false"]
lean_lib TCT where
@[default_target] lean_exe «check» where
  root := «Main»
