# Maratona Linux

## O que é?

O *Maratona Linux* é uma tecnologia desenvolvida e mantida pelo [prof. Bruno Ribas (UnB-FCTE)](https://www.brunoribas.com.br/),
 que é utilizada amplamente nas Maratonas de Programação da SBC e em diversas universidades para fins didáticos.
Ao gravá-la em um pendrive, ela viabiliza a utilização de um sistema Ubuntu GNU/Linux com várias ferramentas para desenvolvimento de software.

## O que não é?

Não é uma imagem do tipo live CD, o *Maratona Linux* efetivamente utiliza alguma partição do seu disco para ser instalado.

## Por que utilizar o Maratona Linux?

O *Maratona Linux* facilita imensamente a instalação de um ambiente de desenvolvimento sem causar dor de cabeça para o usuário. Não é necessário
formatar ou particionar discos. Ele automaticamente detecta alguma partição livre no seu sistema e o instala por lá. Antigamente ele era conhecido
como **Nutella Boot** justamente por esse motivo, pois qualquer *nutella* consegue utilizá-lo.

## Instalação

1. Faça o download da imagem do *Maratona Linux* através deste [link](https://nutellaboot.naquadah.com.br/disk-extra/maratonalinux-bootdisk-tete2204.raw.gz)
2. Descompacte o arquivo. Ao final do processo, você deverá obter uma imagem com a extensão `raw`.
3. Grave a imagem em um pendrive. Isso pode ser feito utilizando o [`etcher`](https://etcher.balena.io/) ou o comando `dd` do Linux.
4. Coloque o pendrive em alguma porta USB e configure na BIOS do seu computador para ele bootar pelo pendrive.
5. Espere a mágica acontecer.

**Observações**: 

- Sempre que quiser utilizar o *Maratona Linux*, você precisará bootar pelo pendrive.
- É necessário ter conexão com a Internet.

## Utilização

O *Maratona Linux* possui diversas IDEs e programas para desenvolvimento das linguagens

- `C`
- `C++`
- `Java`
- `Python`
- `Kotlin`


