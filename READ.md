Plataforma TDB - Responde

Sistema de Gestão de Atendimentos e Interações de Saúde Bucal

Integrantes:

Alisson Kawan Evangelista Silva (RM: 567598)

Marcos Vinicius de Jesus Almeida (RM: 567214)

Descrição

A Plataforma TDB - Responde é um sistema em Python desenvolvido para gerenciar atendimentos odontológicos, consultas e manifestações de pacientes (reclamações, elogios e sugestões). O sistema permite o cadastro de pacientes, registro de dentistas voluntários, remarcação e cancelamento de consultas, além do registro de feedback dos usuários.

O armazenamento de dados é feito em memória, utilizando listas de dicionários.

Funcionalidades

Cadastro de Paciente
Permite registrar informações do paciente como nome, CPF e telefone.

Registro de Dentista Voluntário
Permite registrar dentistas voluntários, incluindo nome, CRO, telefone e especialidade.

Remarcar Consulta
Permite alterar a data de uma consulta previamente cadastrada.

Cancelar Consulta
Permite remover uma consulta existente do sistema.

Fazer uma Reclamação
Permite que o paciente registre uma reclamação.

Fazer um Elogio
Permite que o paciente registre um elogio.

Fazer uma Sugestão
Permite que o paciente registre uma sugestão para melhorar o atendimento.

Sair do Sistema
Encerra a execução do programa.

Estrutura do Código

O código é organizado da seguinte forma:

Listas de armazenamento em memória:

pacientes: armazena informações dos pacientes.

voluntarios: armazena informações dos dentistas voluntários.

consultas: armazena informações das consultas agendadas.

manifestacoes: armazena reclamações, elogios e sugestões.

Loop principal:

Exibe o menu principal com opções de interação.

Recebe a escolha do usuário e executa a funcionalidade correspondente.

Utiliza tratamento de exceções para entradas inválidas.

Dicionários:

Cada paciente, voluntário e manifestação é armazenado como um dicionário dentro da lista correspondente.

Como Executar

Certifique-se de ter o Python 3.x instalado.

Salve o arquivo com a extensão .py, por exemplo tdb_responde.py.

Execute o arquivo no terminal ou prompt de comando:

python tdb_responde.py


Siga as instruções exibidas no menu.

Observações

O sistema não possui persistência de dados. Todas as informações são armazenadas em memória e serão perdidas ao encerrar o programa.

Para cada operação, o sistema solicita a confirmação ou informações necessárias para concluir a ação.

É recomendado digitar apenas números válidos para navegar no menu.