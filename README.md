# python_lembretes
Lembretes da liguagem Python

Conceitos gerais de **herança**, **encapsulamento**, **sobrecarga** e **polimorfismo**.

## Que ferramenta eu uso para compilar e executar meus projetos ?

### Eclipse - versão Red Hat - Jboss Developer Studio

Você pode utilizar uma ide tradicional para desenvolver suas aplicações ou testar os softwares.
Recomendo o Eclipse versão 4.6 - codinome **neon**, mas aquele distribuido via Red Hat.

[JBoss Developer Studio - Eclipse da Red Hat](http://developers.redhat.com/products/devstudio/download/?referrer=jbd)

A versão **10** do  **JBoss Developer Studio** equivale ao **eclipse** versão **4.6**. 

Após baixar e instalar o eclipse do site da RedHat, instale o plugin/interface de python do eclipse, 
que é chamada de **PyDev** .

Você pode usar o instalador do eclipse inserindo o site do repositório do plugin python, mais conhecido como **p2**:

[endereço do repositorio plugin PyDev versão 5.3  ](http://www.pydev.org/updates)
![Instalador Eclipse 4.6 - inserindo endereço](http://download.eclipse.org/errors/content/eclipse-software-install-win10-v1.png)


Depois de instalado o plugin, considerando que **você já tem o python instaldo**, seja o python versão **2.7**, seja o python versão **3.5**, você deve fazer o eclipse reconhecer onde estão os executáveis do interpretador python no seu sistema.
Você pode ( e deve até ) 'ter várias versões de python' disponibilizados para o eclipse utilizar, conforme mostrado na figura abaixo:
[Configurando interpretador Python](http://www.pydev.org/manual_101_interpreter.html)

![Local do executável do interpretador Python](http://www.pydev.org/images/interpreter_mac.png)
![Local no eclipse onde você configura o interpretador](http://www.pydev.org/images/interpreter.png)

Nota: 
Opcional: **IronPython** é uma versão de python para usar o .net Framework da Microsoft. Eu nem uso...
Opcional: **Jython** é uma proposta de usar Python pela máquina virtual JAVA. Também precisa de interpretador específico.


