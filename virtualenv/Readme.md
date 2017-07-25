# Virtualenv e VirtualenvWrapper

O virtualenvwrapper, como o seu nome sugere, é um wrapper para o virtualenv, adicionando algumas funcionalidades para facilitar a vida dos Pythonistas.

Uma ferramenta simples e muito interessante que disponibiliza as seguintes funcionalidades:

1. Organiza todos os seus ambientes virtuais em um único lugar.
2. Adiciona funções de create, delete e copy.
3. Troca de ambiente com um único comando.
4. Permite a criação de hooks para todas as suas operações.

## 1 Instalando Virtualenv:
'virtualenv' é uma ferramenta para criar ambientes Python isolados. 

Um dos grandes problemas solucionados através do virtualenv é o caso de versionamento de dependência. Supondo que você tenha 2 aplicações, uma chamada carro e outra chamada caminhão. Carro precisa de roda 1.0 instalada no sistema , enquanto que caminhão só roda com a versão 2.0 do pacote roda. Ou seja, em uma máquina ou você roda carro, ou você roda caminhão, mas não consegue rodar os 2 simultaneamente, porque ao atulizar a versão do pacote roda e 1.0 para 2.0, carro deixará de funcionar...


### 1.1 Instalando suporte a ambiente virtual no ubuntu/debian/devuan:
#### 1.1.1 Instalando o virtualenv para python 2.7.x
```{bash virtualenv2, echo=FALSE}
sudo apt-get install python-virtualenv
```
#### 1.1.2 Instalando o virtualenv para python 3.x
```{bash virtualenv3, echo=FALSE}
sudo apt-get install python3-virtualenv
```
## 2 Instalando virtualenvwrapper:
Já o virtualenvwrapper serve para organizar todos os ambientes virtualenv que você criar. Supondo que você tenha vários ambientes virtualenv dispersos no disco rígido, vai ficar um tanto difícil gerenciar todos eles ao passo que o número de ambientes aumente. Então entra em cena o virtualenvwrapper. Tudo isso se faz setando uma variável de ambiente chamada 'WORKON_HOME'.
### 2.1 Instalando o virtualenvwrapper

```bash
sudo apt-get install virtualenvwrapper

# agora você deve definir a variável de ambiente WORKON_HOME em tempo de carga do sistema
# faça isso por exemplo deixando ela fixa no .bash_profile do diretório do usuário
# e em seguida mande o bash ler e carregar o conteudo do arquivo **virtualenvwrapper.sh**

cat <<FDA >> greetings.txt
export WORKON_HOME=~/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
FDA

# Por ultimo, mas não menos importante, faça o 'pip' sempre instalar os pacotes e as respectivas atualizações dos mesmos dentro de ambientes virtualenv, ao invés de instalar-los direto no sistema operacional. Afinal acho que você vai gostar de manter seu sistema operacional **puro-sangue** permitindo apenas os pacotes python vindos originários dos apt-get da vida.

export PIP_REQUIRE_VIRTUALENV=true 

```
## 3 Testando ambientes com o virtualenvwrapper:
Agora vamos testar criando o ambiente 'abacaxi':

```bash
mkvirtualenv abacaxi
```
Agora instale por exemplo, o Django no ambiente 'abacaxi':
```bash
(abacaxi) $ pip install django
```
ok, agora vamos desativar o ambiente 'abacaxi':
```bash
(abacaxi) $ deactivate
```

Agora vamos ativar o ambiente 'abacaxi':
```bash
$ workon abacaxi
```

Feito. Agora você tem um abiente python organizado.


Bibliografia:
http://klauslaube.com.br/2015/07/23/virtualenvwrapper-o-basico-para-um-bom-ambiente-de-desenvolvimento-python.html
