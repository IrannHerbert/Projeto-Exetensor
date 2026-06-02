## Repositório destinado ao Projeto Extensor.

Este repositório foi desenvolvido com o objetivo de aplicar, de forma prática, os conhecimentos acadêmicos relacionados às metodologias ágeis, com foco especial na metodologia Scrum. Por motivos pessoais, não há planejamento para futuras atualizações no código deste projeto, além daquelas já previstas no planejamento inicial.

## Notas de Atualizações

# Nota da Sprint Review - 01/06/2026

Foi apresentada a primeira versão do projeto: uma calculadora que conta com funções básicas, como divisão, multiplicação, subtração e soma. Todas as operações funcionam por meio de um menu interativo, proporcionando maior praticidade e facilidade de uso.

Para a implementação do menu, foi utilizado um modelo de loop, juntamente com funções específicas para cada operação matemática e para o próprio gerenciamento do menu.

Todo esse conteúdo está disponível no arquivo `calculadora.py`, localizado neste mesmo diretório.

Todas as funcionalidades foram testadas e tiveram seu funcionamento verificado com sucesso, concluindo assim esta etapa do projeto.

A partir de agora, o projeto passa para a próxima fase, que contará com novas funcionalidades, como o cálculo para determinar se compensa abastecer com álcool ou gasolina e a implementação do cálculo de promoções do tipo "3 por 1".

# Nota de Update - 02/06/2026

Foi apresentada uma nova versão do projeto: uma calculadora em Python estruturada com foco em organização, reutilização de código e maior robustez na interação com o usuário.

Nesta atualização, foi implementada uma função dedicada à leitura dos valores informados pelo usuário (`ler_numeros`), responsável por capturar e validar entradas numéricas. Essa melhoria reduziu a repetição de código nas operações matemáticas e aumentou a consistência do programa.

Também foi criada a função principal (`main`), responsável por centralizar o fluxo de execução da aplicação. A partir dela, o programa controla o menu interativo e direciona o usuário para as diferentes funcionalidades disponíveis, seguindo uma estrutura mais organizada e modular.

Outra melhoria importante foi a adição de tratamento de exceções (`try/except`) na leitura da opção do menu, evitando que o programa seja encerrado caso o usuário insira um valor inválido. Dessa forma, o sistema passa a lidar melhor com entradas incorretas, mantendo a execução contínua da calculadora.

Além das operações matemáticas básicas já existentes (divisão, multiplicação, subtração e soma), o menu foi expandido para incluir novas funcionalidades em desenvolvimento, como:

* Verificação de custo-benefício entre álcool e gasolina;
* Cálculo de promoções do tipo “3 por 1”;
* Cálculo de Índice de Massa Corporal (IMC);
* Cálculo de juros compostos.

Essas funcionalidades foram adicionadas ao menu principal como parte do planejamento da próxima fase do projeto, estando atualmente em etapa de implementação.

Todas as alterações foram revisadas e testadas, mantendo o funcionamento correto das operações já existentes e consolidando uma base mais estruturada para futuras expansões do sistema.

Com isso, esta versão representa uma evolução significativa do projeto, tornando a calculadora mais organizada, escalável e preparada para novas funcionalidades.


## PLanejamento para o projeto

| ID   | História de Usuário                                        | Prioridade |
| ---- | ---------------------------------------------------------- | ---------- |
| US01 | Como usuário, quero somar dois números                     | Alta       |
| US02 | Como usuário, quero dividir números                        | Alta       |
| US03 | Como usuário, quero sair do sistema pelo menu              | Alta       |
| US04 | Como motorista, quero saber se compensa álcool ou gasolina | Média      |
| US05 | Como consumidor, quero calcular promoções 3 por 1          | Média      |
| US06 | Como usuário, quero calcular IMC                           | Baixa      |
| US07 | Como usuário, quero calcular juros compostos               | Baixa      |
