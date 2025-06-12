============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-8.4.0, pluggy-1.6.0
rootdir: /projects/whitespace-stego2
configfile: pyproject.toml
plugins: html-4.1.1, metadata-3.1.1, cov-6.2.1, md-report-0.7.0
collected 313 items

tests/test_charset.py ...                                                [  0%]
tests/test_cli.py ............                                           [  4%]
tests/test_crypto.py ...                                                 [  5%]
tests/test_decode.py .....                                               [  7%]
tests/test_encode.py ....                                                [  8%]
tests/test_encode_decode.py ......                                       [ 10%]
tests/test_stego.py .................................................... [ 27%]
........................................................................ [ 50%]
........................................................................ [ 73%]
........................................................................ [ 96%]
............                                                             [100%]

================================ tests coverage ================================
_______________ coverage: platform linux, python 3.12.3-final-0 ________________

Name                                 Stmts   Miss  Cover   Missing
------------------------------------------------------------------
whitespace_stego/__init__.py             3      0   100%
whitespace_stego/cli.py                 57      1    98%   144
whitespace_stego/common/charset.py      13      0   100%
whitespace_stego/crypto.py              42      0   100%
whitespace_stego/decode.py              33      0   100%
whitespace_stego/encode.py              22      0   100%
------------------------------------------------------------------
TOTAL                                  170      1    99%
---- Generated html report: file:///projects/whitespace-stego2/report.html -----
============================= 313 passed in 6.53s ==============================
|          filepath           | [92m$$\textcolor{#23d18b}{\tt{passed}}$$[0m | SUBTOTAL |
| --------------------------- | --------------------------------: | -------: |
[48;2;32;32;32m|[0m[48;2;32;32;32m[92m $$\textcolor{#23d18b}{\tt{tests/test\\_charset.py}}$$ [0m[48;2;32;32;32m|[0m[48;2;32;32;32m[92m   $$\textcolor{#23d18b}{\tt{3}}$$ [0m[48;2;32;32;32m|[0m[48;2;32;32;32m[92m $$\textcolor{#23d18b}{\tt{3}}$$ [0m[48;2;32;32;32m|[0m
[40m|[0m[40m[92m $$\textcolor{#23d18b}{\tt{tests/test\\_cli.py}}$$ [0m[40m|[0m[40m[92m  $$\textcolor{#23d18b}{\tt{12}}$$ [0m[40m|[0m[40m[92m $$\textcolor{#23d18b}{\tt{12}}$$ [0m[40m|[0m
[48;2;32;32;32m|[0m[48;2;32;32;32m[92m $$\textcolor{#23d18b}{\tt{tests/test\\_crypto.py}}$$ [0m[48;2;32;32;32m|[0m[48;2;32;32;32m[92m   $$\textcolor{#23d18b}{\tt{3}}$$ [0m[48;2;32;32;32m|[0m[48;2;32;32;32m[92m $$\textcolor{#23d18b}{\tt{3}}$$ [0m[48;2;32;32;32m|[0m
[40m|[0m[40m[92m $$\textcolor{#23d18b}{\tt{tests/test\\_decode.py}}$$ [0m[40m|[0m[40m[92m   $$\textcolor{#23d18b}{\tt{5}}$$ [0m[40m|[0m[40m[92m $$\textcolor{#23d18b}{\tt{5}}$$ [0m[40m|[0m
[48;2;32;32;32m|[0m[48;2;32;32;32m[92m $$\textcolor{#23d18b}{\tt{tests/test\\_encode.py}}$$ [0m[48;2;32;32;32m|[0m[48;2;32;32;32m[92m   $$\textcolor{#23d18b}{\tt{4}}$$ [0m[48;2;32;32;32m|[0m[48;2;32;32;32m[92m $$\textcolor{#23d18b}{\tt{4}}$$ [0m[48;2;32;32;32m|[0m
[40m|[0m[40m[92m $$\textcolor{#23d18b}{\tt{tests/test\\_encode\\_decode.py}}$$ [0m[40m|[0m[40m[92m   $$\textcolor{#23d18b}{\tt{6}}$$ [0m[40m|[0m[40m[92m $$\textcolor{#23d18b}{\tt{6}}$$ [0m[40m|[0m
[48;2;32;32;32m|[0m[48;2;32;32;32m[92m $$\textcolor{#23d18b}{\tt{tests/test\\_stego.py}}$$ [0m[48;2;32;32;32m|[0m[48;2;32;32;32m[92m $$\textcolor{#23d18b}{\tt{280}}$$ [0m[48;2;32;32;32m|[0m[48;2;32;32;32m[92m $$\textcolor{#23d18b}{\tt{280}}$$ [0m[48;2;32;32;32m|[0m
[48;2;0;0;0m|[0m[48;2;0;0;0m[92m $$\textcolor{#23d18b}{\tt{TOTAL}}$$ [0m[48;2;0;0;0m|[0m[48;2;0;0;0m[92m $$\textcolor{#23d18b}{\tt{313}}$$ [0m[48;2;0;0;0m|[0m[48;2;0;0;0m[92m $$\textcolor{#23d18b}{\tt{313}}$$ [0m[48;2;0;0;0m|[0m
