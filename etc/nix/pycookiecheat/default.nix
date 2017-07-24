{ stdenv, fetchFromGitHub, pythonPackages }:

pythonPackages.buildPythonPackage rec {
  pname = "pycookiecheat";
  version = "0.4.3";
  name = "${pname}-${version}";

  src = fetchFromGitHub {
    owner  = "n8henrie";
    repo   = "pycookiecheat";
    rev    = "ec85113cdebf66cf28588454a5051cbee6a4fe5f";
    sha256 = "0282nsbdai7g9zblwbkdg3lin5qr3v4nryx78nwkdawf9567b8m3";
  };

  patches = [ ./jailbreak.patch ];


  doCheck = false;

  buildInputs = with pythonPackages; [ tox pytest pylint pep8 flake8 ];

  propagatedBuildInputs = with pythonPackages; [ pycrypto keyring ];

  meta = with stdenv.lib; {
    description = "Get cookies from chrome tore";
    homepage = "https://github.com/n8henrie/pycookiecheat";
    license = licenses.mit;
    maintainers = with maintainers; [ jb55 ];
  };
}
