{
  pkgs ? import <nixpkgs> { },
}:

let
  pythonPackages = pkgs.python312Packages;
in
pkgs.mkShell {
  buildInputs = with pkgs; [
    (python312.withPackages (
      ps: with ps; [
        pip
        pygame
        poetry-core
      ]
    ))
    SDL2
    SDL2_image
    SDL2_mixer
    SDL2_ttf
    zlib
    pkg-config
  ];

  shellHook = ''
    export LD_LIBRARY_PATH="${
      pkgs.lib.makeLibraryPath [
        pkgs.SDL2
        pkgs.SDL2_image
        pkgs.SDL2_mixer
        pkgs.SDL2_ttf
        pkgs.zlib
      ]
    }"
    export PYTHONPATH="${pythonPackages.pygame}/${pythonPackages.python.sitePackages}:$PYTHONPATH"
  '';
}
