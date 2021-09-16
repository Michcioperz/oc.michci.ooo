{ pkgs ? import <nixpkgs> {} }:
pkgs.stdenv.mkDerivation {
  pname = "oc-michciooo";
  version = "0.1.0";
  src = ./.;
  buildInputs = [ pkgs.gomplate pkgs.optipng ];
  buildPhase = ''
    optipng oc/*.png
    gomplate -d oc=./oc.json -f ./index.html.tpl >oc/index.html
  '';
  installPhase = ''
    mkdir -p $out/share/project
    cp -r oc $out/share/project/oc
  '';
}
