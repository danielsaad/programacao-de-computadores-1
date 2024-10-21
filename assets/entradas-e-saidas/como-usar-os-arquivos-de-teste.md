# Como usar os arquivos de teste

Para cada problema, os testes estão na pasta `input/` do problema
enquanto as respostas esperadas estão na pasta `output/`

Suponha que você queira testar o seu programa, chamado de `exec`,
contra o caso de teste 30 do problema `fizz-buzz`. No terminal, você 
pode fazer:

`./exec < fizz-buzz/30`

Assim você não precisará digitar o caso de teste no teclado, pois ele
repassará o conteúdo do arquivo para o teclado através do operador
    de redirecionamento `<`


