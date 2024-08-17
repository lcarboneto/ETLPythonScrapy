@echo off
REM Muda para o diretório do projeto
cd "C:\Users\lcarb\OneDrive\Documentos\Projetos Python\VSCode\ETLPythonScrapy"
IF %ERRORLEVEL% NEQ 0 (
    echo Erro ao mudar para o diretório do projeto.
    pause
    exit /b %ERRORLEVEL%
)
echo Diretório do projeto encontrado.

REM Ativa o ambiente virtual
call .venv\Scripts\activate
IF %ERRORLEVEL% NEQ 0 (
    echo Erro ao ativar o ambiente virtual.
    pause
    exit /b %ERRORLEVEL%
)
echo Ambiente virtual ativado.

REM Muda para o diretório 'src'
cd src
IF %ERRORLEVEL% NEQ 0 (
    echo Erro ao mudar para o diretório 'src'.
    pause
    exit /b %ERRORLEVEL%
)
echo Diretório 'src' encontrado.

REM Executa o scrapy
scrapy crawl mercadolivre -o ../data/data02.csv
IF %ERRORLEVEL% NEQ 0 (
    echo Erro ao executar o scrapy.
    pause
    exit /b %ERRORLEVEL%
)
echo Scrapy executado com sucesso.

pause

REM Muda para o diretório 'transformação' (verifique o nome do diretório)
cd "C:\Users\lcarb\OneDrive\Documentos\Projetos Python\VSCode\ETLPythonScrapy\transformacao\"
IF %ERRORLEVEL% NEQ 0 (
    echo Erro ao mudar para o diretório de transformacao.
    pause
    exit /b %ERRORLEVEL%
)
echo Diretório de transformacao encontrado.

REM Executa o script Python
python main.py
IF %ERRORLEVEL% NEQ 0 (
    echo Erro ao executar o script Python.
    pause
    exit /b %ERRORLEVEL%
)
echo Script Python executado com sucesso.

pause

REM Muda para o diretório 'dashboard'
cd "C:\Users\lcarb\OneDrive\Documentos\Projetos Python\VSCode\ETLPythonScrapy\dashboard\"
IF %ERRORLEVEL% NEQ 0 (
    echo Erro ao mudar para o diretório do dashboard.
    pause
    exit /b %ERRORLEVEL%
)
echo Diretório do dashboard encontrado.

REM Executa o Streamlit
streamlit run app.py
IF %ERRORLEVEL% NEQ 0 (
    echo Erro ao executar o Streamlit.
    pause
    exit /b %ERRORLEVEL%
)
echo Streamlit executado com sucesso.

pause
