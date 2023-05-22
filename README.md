# Sobre o App Pomodoro

Aplicativo que fiz para uso pessoal por ter me frustrado bastante com outros aplicativos da play store relacionado a pomodoro. A interface é intencionalmente simples e única. Na pasta APLICATIVO_CELL se encontra o .pkg onde você pode baixar no seu telefone e utilizar a vontade o aplicativo. Conseguir transformar o main.py em um executavel .pkg foi muito mais difícil do que construir o própio aplicativo no python 😓(peguei diversas interfaces e contadores na internet e fui fazendo uma mistura até sair esse aplicativo), foram cerca de 9 horas tentando diversos metodos e configurando coisas muito especificas no arquivo .spec até realmente conseguir funcionar o .pkg  .Segue o vídeo e o site que mais ajudou: 

**Vídeo:** https://www.youtube.com/watch?v=GTkKul8sA-c

**Site:** https://towardsdatascience.com/3-ways-to-convert-python-app-into-apk-77f4c9cd55af

# Sobre o Kivy

**Como instalar biblioteca e documentação do pacote:** https://kivy.org/doc/stable/gettingstarted/installation.html
-------------------

# Utilizando o aplicativo

Como falei anteriormente criei para uso pessoal, então em vez de seguir o padrão do pomodoro normal de 25 min de trabalho e 5 de descanso com uma pausa longa de 15 minutos, esse Pomodoro é 50 minutos de trabalho com 10 de descanso e no final de 4 sessões de work temos um long break de 30 minutos. Sou mais produtivo com esse método por isso o utilizo (uma sessão inteira do pomodoro normal equivale a 2 horas, esse no total equivale a 4). A meta diária é zerar 2 sessões totalizando no total 8 horas. Agora vamos para o app:

**App:**

![image](https://user-images.githubusercontent.com/90096835/213074181-43d16d20-2f42-4d48-ae9f-de0f1d990e75.png)

**A imagem "go go go" equivale ao play, quando clicada o contador irá iniciar**

![image](https://user-images.githubusercontent.com/90096835/213075143-33ee8bb7-7105-427b-aa1b-f12a1466c309.png)

**Caso queira pausar o contador é só clicar no Gelado (fica frio ai)**

![image](https://user-images.githubusercontent.com/90096835/213075250-d3f20656-39b6-4a20-a604-d94b9d4b3a58.png)

**O botão de skip irá pular sua sessão atual, seja de work ou de descanso, irá para a próxima**

![image](https://user-images.githubusercontent.com/90096835/213075362-7d9cdd4b-c3eb-4430-ac1e-5550cae08a03.png)

**Caso queira resetar tudo clique no meme do botão**

![image](https://user-images.githubusercontent.com/90096835/213075497-59f9c7d0-aeaa-4a29-bf25-79f1ccffc12f.png)

**O pernalonga aparece quando o pomodoro não está iniciado, então não tem como resetar**

![image](https://user-images.githubusercontent.com/90096835/213075715-7402a17e-bc91-4ba9-86e2-4ee4b9a951ff.png)

**O número é o tempo restante, fazendo contagem regressiva. O Status é qual sessão atual você está [trabalho ou descanso]. O "Ciclos completados" é a contagem de ciclos que ja foi e que faltam para a long break. O zerou é quantos ciclos inteiros completos você já fez.**

![image](https://user-images.githubusercontent.com/90096835/213076263-a12d8288-87ef-4d8b-8076-5ff9b581ddac.png)

-------------
*Você saberá que acabou o work time quando o vector falar "aaaah éeee" e uma mensagem escrito CABOUCI! aparecer. Quando acabar o tempo de descanso também irá aparecer essa mensagem só que com o aúdio da bruxa do pica pal "e la vamos nós". Lembre-se de dar o play quando estiver pronto para o novo ciclo.*  
