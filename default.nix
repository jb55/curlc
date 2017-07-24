{ stdenv, fetchFromGitHub, python35Packages }:

let
  pythonPackages = python35Packages;
  pycookiecheat = import ./etc/nix/pycookiecheat {
    inherit stdenv pythonPackages fetchFromGitHub;
  };
in
pythonPackages.buildPythonPackage rec {
  pname = "curlc";
  version = "0.2.1";
  name = "${pname}-${version}";

  src = ./.;

  propagatedBuildInputs = with pythonPackages; [ pycookiecheat ];

  meta = with stdenv.lib; {
    description = "";
    homepage = "https://github.com/jb55/youtube-sheet-scraper";
    license = licenses.mit;
    maintainers = with maintainers; [ jb55 ];
  };
}

