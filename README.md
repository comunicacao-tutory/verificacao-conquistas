# Verificação de Conquistas Tutory

Pagina publica para conferir a autenticidade de um certificado do
Programa de Reconhecimento Tutory Mentoria. O link vai dentro do PDF
do certificado.

## Como funciona

A pagina nao tem servidor. Cada certificado e um arquivo em `dados/`
cujo nome e o SHA-256 do sal mais o codigo normalizado. A pagina
calcula o hash do que a pessoa digita e busca esse arquivo. Se nao
existir, o codigo e invalido.

Isso importa: se os certificados ficassem numa lista dentro da pagina,
qualquer pessoa abriria o codigo-fonte e teria o nome de todos os
mentores premiados, com codigo e data. Do jeito atual o fonte nao
revela nenhum.

O codigo aceita qualquer forma: `TUT-OURO-0125`, `tut ouro 0125` e
`TUTOURO0125` abrem o mesmo certificado.

## Cadastrar um certificado

    python3 gerar-certificado.py "TUT-OURO-0126" \
        --mentor "Nome Completo" \
        --mentoria "Nome da Mentoria" \
        --data "22/10/2026"

O script grava o arquivo em `dados/`. Faca commit e push: a Vercel
publica sozinha.

## Nunca coloque dado sensivel

Os arquivos em `dados/` ficam publicos para quem tem o codigo. Nome do
mentor, nome da mentoria, conquista e data sao o que o certificado ja
mostra. **CPF, e-mail e telefone nao entram.**

## Link direto

`?codigo=TUT-OURO-0125` na URL ja abre o resultado, sem a pessoa
precisar digitar. Util para o QR Code do certificado.
