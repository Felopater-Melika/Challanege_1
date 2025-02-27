{
  description = "Python Class";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = {
    self,
    nixpkgs,
  }: {
    devShells.x86_64-linux.default = let
      pkgs = nixpkgs.legacyPackages.x86_64-linux;
    in
      pkgs.mkShell {
        name = "Class";
        buildInputs = [
          (pkgs.python312.withPackages (ps: [
            ps.requests
            ps.python-dotenv
            ps.pandas
          ]))
        ];
      };
  };
}
